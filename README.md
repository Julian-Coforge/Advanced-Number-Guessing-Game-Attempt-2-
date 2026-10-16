# Advanced Number Guessing Game (Attempt 2)
Notes: I forgot to do feature branches when creating the first version, hence attempt 2
Additionally, I had intepreted Feature 1 (Classic Mode) 'The computer picks a random secret number in the chosen range.' as meaning the user selects the range, so I have one extra mode.. the Classic with Difficulty is Feature 2, and Timed Challenge is Feature 3.

To run the game:

python3 -m venv .venv

source .venv/bin/activate

python guess.py

| # | What I tested | What I did | Expected result | Actual result | Pass? |
|---|---------------|------------|-----------------|---------------|-------|
| 1 | How the level guess handles value errors (emtpy value, characters, etc. ) | Inputted any non-int instead of int into level guess | Repeats input question, catches errors | Repeated input question, no errors thrown | Yes |
| 2 | How the level guess handles values out of range | Inputted a value higher and lower than allowed | Repeats input question, doesn't allow value to be selected | Refuses to continue with out of range value, repeats question | Yes |
| 3 | If 'Too High/Low' is genuine when attempting the secret number | Printed the secret value at game start, then played through | Game correctly identifies Too High/Low | High/Low correctly identified | Yes |
| 4 | If invalid inputs count as an attempt | Listed attempt number throughout game, entered invalid input | Attempt number does not decrease | Attempt number did not decrease | Yes |
| 5 | If a correct guess shows the correct attempt number | Counted attempts throughout game, and listed final attempt number | Final attempt num matches count | Final attempt num matched count | Yes |
| 6 | If running out of attempts ends game and shows the number | Played through the difficulty select mode using 1 incorrect guess the whole time | Number is revealed and game ends | Number was revealed and game ends | Yes |
| 7 | During timed challenge, does the time get shown before each guess | Played the timed challenge mode | The amount of time left is show before each input | The amount of time was shown before each input | Yes |
| 8 | During the timed challenge, does the game end once time runs out (including last guess) | Set the timed challenge time to be 10s and played slowly | After time runs out, there is one more guess, even if that is right or wrong, says times up and reveals number | Time ran out after final guess, even when it was correct | Yes |
| 9 | Does a correct guess show the attempt number | Played the challenge mode on easy | Game shows attempt number when getting it correct | Correct answer shows the attempt as well | Yes |
| 10 | Does the level select work with the time challenge | Tested timed challenge and all 3 difficulty levels | 3 Levels show different ranges and number of attempts | All levels worked, having a value between their given ranges, and certain num of attempts | Yes |
