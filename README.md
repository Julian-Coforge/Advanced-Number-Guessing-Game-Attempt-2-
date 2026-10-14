# Advanced Number Guessing-Game (Attempt 2)
Note: I forgot to do feature branches when creating the first version, hence attempt 2

| # | What I tested | What I did | Expected result | Actual result | Pass? |
|---|---------------|------------|-----------------|---------------|-------|
| 1 | How the level guess handles value errors (emtpy value, characters, etc. ) | Inputted any non-int instead of int into level guess | Repeats input question, catches errors | Repeated input question, no errors thrown | Yes |
| 2 | How the level guess handles values out of range | Inputted a value higher and lower than allowed | Repeats input question, doesn't allow value to be selected | Refuses to continue with out of range value, repeats question | Yes |
| 3 | If 'Too High/Low' is genuine when attempting the secret number | Printed the secret value at game start, then played through | Game correctly identifies Too High/Low | High/Low correctly identified | Yes |
| 4 | If invalid inputs count as an attempt | Listed attempt number throughout game, entered invalid input | Attempt number does not decrease | Attempt number did not decrease | Yes |
| 5 | If a correct guess shows the correct attempt number | Counted attempts throughout game, and listed final attempt number | Final attempt num matches count | Final attempt num matched count | Yes |
| 6 | If running out of attempts ends game and shows the number | Played through the difficulty select mode using 1 incorrect guess the whole time | Number is revealed and game ends | Number was revealed and game ends | Yes |