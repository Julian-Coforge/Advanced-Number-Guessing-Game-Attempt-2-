import random
import time

# ---------- Settings ----------
DEBUG_SECRET = None   # For testing, set to a number such as 42. Set back to None before your final commit.
TIME_LIMIT = 60       # Seconds allowed in Time Challenge mode

print("Welcome to the Number Guessing Game")

# ---------- Choose a level ----------
# Goal: keep asking until the player picks a valid level, then set the range and attempt limit.

# ---------- Choose a mode ----------
# Goal: keep asking until the player picks Classic or Time Challenge.

def choose_mode():
    print("\nYou can choose: \n[1] Classic mode \n[2] Select a Difficulty\n[3] Time Challenge mode (limited time)\n")

    # Loop to catch non-integer inputs, printing error and repeating loop, break if within range
    while True: 
        try:
            mode = int(input("Choose a mode (1 or 2): "))
            if 1 <= mode <= 2:
                break
        except ValueError:
            print("\nInvalid choice. Please choose 1 or 2.\n")
            continue

# ---------- Set up the round ----------
# Goal: pick the secret number (use DEBUG_SECRET when it is not None) and start the clock.

while True: 
    try:
        chosen_range = int(input("Choose what the highest number should be: "))
        if chosen_range < 1:
            print("\nPlease choose a number greater than 0.\n")
            continue
        break
    except ValueError:
        print("\nInvalid choice. Please choose 1 or 2.\n")
        continue

secret_number = DEBUG_SECRET if DEBUG_SECRET is not None else random.randint(1, chosen_range)


# ---------- Guess loop ----------
# Goal: keep asking for guesses until the player wins, runs out of attempts, or runs out of time.

guess = 0

while True:
    try:
        guess = int(input("Enter your guess: "))
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