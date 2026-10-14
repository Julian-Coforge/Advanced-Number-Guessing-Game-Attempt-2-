import random
import time

# ---------- Settings ----------
DEBUG_SECRET = None   # For testing, set to a number such as 42. Set back to None before your final commit.
TIME_LIMIT = 60       # Seconds allowed in Time Challenge mode

print("Welcome to the Number Guessing Game")

# ---------- Choose a level ----------
# Goal: keep asking until the player picks a valid level, then set the range and attempt limit.

def choose_level():
    print("You can choose: \n[1] Easy (1-50, 10 attempts) \n[2] Medium (1-100, 8 attempts) \n[3] Hard (1-500, 10 attempts)\n")

    # Loop to catch non-integer inputs, printing error and repeating loop, break if within range
    while True:  
        try:
            level = int(input("Choose a level (1, 2, or 3): "))
            if 1 <= level <= 3:
                break
        except ValueError:
            print("\nInvalid choice. Please choose 1, 2, or 3.\n")
            continue

    if level == 1:
        chosen_range = 50
    elif level == 2:
        chosen_range = 100
    elif level == 3:
        chosen_range = 500
        
    return chosen_range

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
    while True: 
        if mode == 1:
            try:
                chosen_range = int(input("Choose what the highest number should be: "))
                if chosen_range < 1:
                    print("\nPlease choose a number greater than 0.\n")
                    continue
                break
            except ValueError:
                print("\nInvalid choice. Please choose a number greater than 0.\n")
                continue
            
        elif mode == 2:
            chosen_range = choose_level()
        
    secret_number = DEBUG_SECRET if DEBUG_SECRET is not None else random.randint(1, chosen_range)
    return secret_number


# ---------- Guess loop ----------
# Goal: keep asking for guesses until the player wins, runs out of attempts, or runs out of time.

def guess_loop(secret_number: int):
    guess = 0
    while True:
        try:
            guess = int(input("Enter your guess: "))
            guess += 1
        except ValueError:
            print("Invalid input. Please enter a number.")

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print("Congratulations! You've guessed the secret number!")
            break

# ---------- End of round ----------
# Goal: show the result that matches how the round ended.

def _main():
    choose_mode()
    secret_number = choose_secret_number()
    guess_loop(secret_number)
    print("Thanks for playing!")

if __name__ == "__main__":
    _main()