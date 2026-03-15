# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

The bugs I encountered when I was playing it was:
1) The hints seem to be random and not reflecting what the input and how close it is to the correct number. 
2) when entering in 100, the system said to go higher despite 100 being the max
3) when entering a negative number, hints states to go lower despite it being lower than what should be accepted. 

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

I used Claude for this project. The first suggestion that AI was to fix the issue with the wrong hints. It gave a suggestion to add the same system to logic_utils.py due to the testing code. This code was misleading due to it not fixing the issue of the code. So I rebooted it, asking Claude once again to fix the issue with the system giving wrong hints, which is fixed it by fixing swapping the hints given and removing the coercion of secret on even attempts since it always pass the integer. This fixed the issue after I tested it multiple times. 

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I did multiple tests. First using the pytests made by Claude then I conducted multiple manual tests to make sure that it was made correctly and not something AI made to be easier for it to test. At first the changes made by Claude was very messy. It didn't fix the tests like it should and despite conducting its own tests, it didn't match mine. I had to restart the process again to have Claude fix the code correctly and did my own manual tests to find that it finally fixed the issues with the code. It helped me design the junit tests and showed me how they worked. 

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

The secret number kept changing in the original app is because streamlit was running it like an app using random() to get a random number. Streamlit works as a gateway for any interactive app using minimual code to make it work. The change I needed to make was to change how the hint system worked to make the game work. 

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

One habit I want to reuse is have the AI explain what's going on and if it gets something wrong, to reboot it. Since AI is still a new thing and gets things wrong, it's best to restart the system so it gives you the right answer. One thing I would do differently is the prompting of the AI and how I show it the files for the best efficiency of debugging the system.

From this project, I now view AI generated code as doing the basics of the coding it is assigned to them. It can be good, but must be checked for issues such as the hint system resulting in different system and the secret used for integers causing confusions in the code that needs to be checked by a human for quality checks. 
