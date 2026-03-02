# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

- During the first game, Attempts Left is 1 off. Attempts also shows 1.
- Score inconsistently decreases. Sometimes its -5 each turn, so -35 total. Other times, this becomes -25 total. I think the score goes down if its lower than the target, and it goes higher if its higher than the target.
- New Game changes the secret and attempts, but the "Game over. Start a new game to try again." error doesn't go away, keeping you from submitting new entries in the new game. The same happens even if you win.**
- New Game does not reset the score or history.
- Hints are wrong. Sometimes right at certain numbers like '9.'**
- History does not show what you submitted when you submit. It only shows the previous submission AFTER submitting the current one (this might not be a bug; could be intentional).
- Number of attempts should be highest on easy. But normal has 7 attempts and easy has 5. Range should be highest on hard. But normal has 1-100 while hard has 1-50.
- Numbers out of range are allowed to be guessed.

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  - GitHub Copilot
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  - I was wondering why the hints weren't purely inverted (instead of just saying the user needs to go higher if the number was greater than secret or vice versa, it would sometimes give the correct answer or the same answer would switch between turns) and also why there was a try/catch for type errors when comparing the secret value to the input. So, when I asked Copilot, it alerted me on other lines in the #codebase that showed that the secret would be converted to a string on every even turn, reversing the comparison order sometimes. It gave me an example: "11" < "2" since 1 comes before 2 in ASCII and strings compare bit by bit. This further helped me both eliminate complexity and fully resolve the error.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  - This didn't happen too often, but it gave me updated pytests for functions that I just asked to be refactored to logic_utils. Any time I refactored it would automatically do that, even though nothing had been fixed/modified in some of these functions. I briefly read through them but knew it wouldn't make much sense to accept the changes without modifying the functions first.

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  - I read through it, made sure it made sense, then accepted the changes. I used the AI-generated pytests and made sure those worked. Then, I ran my own manual tests on the actual site to also verify that it worked.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  - After changing the new_game session state status to "playing" when you click the "New Game" button, I tested it out manually. After losing, after winning, and during the game, when I clicked the button, it would all make the popup disappear, restart the attempts, and change the secret value. This helped me verify that the line of code was the correct change.
- Did AI help you design or understand any tests? How?
  - I asked AI to generate the pytests in the test_game_logic.py tests folder. It imported functions and built the tests as needed. And in the chat window, it was able to run those tests and give me the results and runtime.

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
