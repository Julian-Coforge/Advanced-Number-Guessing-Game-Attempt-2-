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

print("\nYou can choose: \n[1] Classic mode (limited attempts) \n[2] Time Challenge mode (limited time)\n")

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

# ---------- Guess loop ----------
# Goal: keep asking for guesses until the player wins, runs out of attempts, or runs out of time.

# ---------- End of round ----------
# Goal: show the result that matches how the round ended.