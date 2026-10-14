import random
import time

# ---------- Settings ----------
DEBUG_SECRET = None   # For testing, set to a number such as 42. Set back to None before your final commit.
TIME_LIMIT = 60       # Seconds allowed in Time Challenge mode

print("\nWelcome to the Number Guessing Game")

# ---------- Choose a level ----------
# Goal: keep asking until the player picks a valid level, then set the range and attempt limit.

def choose_level():
    print("\nYou can choose: \n[1] Easy (1-50, 10 attempts) \n[2] Medium (1-100, 8 attempts) \n[3] Hard (1-500, 10 attempts)\n")

    # Loop to catch non-integer inputs, printing error and repeating loop, break if within range
    while True:  
        try:
            level = int(input("Choose a level (1, 2, or 3): "))
            if 1 <= level <= 3:
                break
        except ValueError:
            print("\nInvalid choice. Please choose 1, 2, or 3.\n")
            continue

    # Select the range based on the chosen level
    if level == 1:
        chosen_range = 50
        attempts_left = 10
    elif level == 2:
        chosen_range = 100
        attempts_left = 8
    elif level == 3:
        chosen_range = 500
        attempts_left = 10

    return chosen_range, attempts_left

# ---------- Choose a mode ----------
# Goal: keep asking until the player picks Classic or Time Challenge.

def choose_mode():
    print("\nYou can choose: \n[1] Classic mode \n[2] Select a Difficulty\n[3] Time Challenge mode (limited time)\n")

    # Loop to catch non-integer inputs, printing error and repeating loop, break if within range
    while True: 
        try:
            mode = int(input("Choose a mode (1, 2, or 3): "))
            if 1 <= mode <= 3:
                break
        except ValueError:
            print("\nInvalid choice. Please choose 1, 2, or 3.\n")
            continue

    return mode

# ---------- Set up the round ----------
# Goal: pick the secret number (use DEBUG_SECRET when it is not None) and start the clock.

def choose_secret_number(mode: int):

    attempts_left = -1  # Default value for classic mode

    if mode == 1:
        while True: 
            try:
                chosen_range = int(input("\nChoose what the highest number should be: "))
                if chosen_range < 1:
                    print("\nPlease choose a number greater than 0.")
                    continue
                break
            except ValueError:
                print("\nInvalid choice. Please choose a number greater than 0.")
                continue
        
    elif mode == 2 or mode == 3:
        chosen_range, attempts_left = choose_level()
        print(f"\nYou will have {attempts_left} attempts to guess a number between 1 and {chosen_range}.")
        
        
    secret_number = DEBUG_SECRET if DEBUG_SECRET is not None else random.randint(1, chosen_range)
    return secret_number, attempts_left, mode


# ---------- Guess loop ----------
# Goal: keep asking for guesses until the player wins, runs out of attempts, or runs out of time.


def guess_loop(secret_number: int, attempts_left: int, mode: int):
    attempt = 0
    guess = 0
    start_time = time.time()

    while guess != secret_number and attempts_left != 0:

        elapsed_time = time.time() - start_time
        if mode == 3 and elapsed_time > TIME_LIMIT:
            print("\nTime's up! You ran out of time.")
            break
        elif mode == 3:
            time_remaining = TIME_LIMIT - elapsed_time
            print(f"\nYou have {time_remaining:.2f} seconds left.")

        try:
            guess = int(input("Enter your guess: "))
            attempt += 1
            attempts_left -= 1
        except ValueError:
            print("\nInvalid input. Please enter a number.")

        if guess < secret_number:
            print("\nToo low!")
        elif guess > secret_number:
            print("\nToo high!")
        else:
            print(f"\nCongratulations! You've guessed the secret number in {attempt} attempts!")
            break

        if attempts_left > 0:
            print(f"You have {attempts_left} attempts left.")

    print(f"\nThe secret number was: {secret_number}")


# ---------- End of round ----------
# Goal: show the result that matches how the round ended.

def _main():
    mode = choose_mode()
    secret_number, attempts_left, mode = choose_secret_number(mode)
    guess_loop(secret_number, attempts_left, mode)
    print("\nThanks for playing!\n")

if __name__ == "__main__":
    _main()