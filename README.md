# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
   - It is a simple number guessing game with 3 difficulties that vary in range of numbers to guess from and number of attempts.
- [ ] Detail which bugs you found.
   - During the first game, Attempts Left is 1 off. Attempts also shows 1.
   - Inconsistent scoring. If an input is higher than the secret number, it will alternate between increasing by 5 and decreasing by 5.
   - New Game changes the secret and attempts, but the "Game over. Start a new game to try again." error doesn't go away, keeping you from submitting new entries in the new game. The same happens even if you win.
   - New Game does not reset the score or history.
   - Hints are sometimes wrong. Sometimes right. Inconsistent hints.
   - Number of attempts should be highest on easy. But normal has 7 attempts and easy has 5. Range should be highest on hard. But normal has 1-100 while hard has 1-50.
   - Numbers out of range are allowed to be guessed.
   - Invalid inputs are still kept in history and still use attempts
   - Winning score started out as 80 instead of 100
- [ ] Explain what fixes you applied.
   - Attempts now starts at 0 from the beginning.
   - Score always decreases by 5 if higher or lower
   - New game button makes win/lose popups disappear and allows the game to restart
   - New game button resets score and history
   - Hints now make sense in relation to what secret is and the user's input
   - Number of attempts and number ranges now make sense with difficulty type
   - Numbers out of range are invalid
   - Invalid inputs don't count as attempts and are not kept in history
   - Winning score starts out as 100

## 📸 Demo

- [ ] [fixed, winning game](image.png)

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
