Introduction
==========================
Simple Reinforcement learning example, based on the Q-function.
- Rules: The agent (yellow box) has to reach one of the goals to end the game (green or red cell).
- Rewards: Each step gives a negative reward of -0.04. The red cell gives a negative reward of -5. The green one gives a positive reward of +5. The black walls give a negative reward of -100
- States: Each cell is a state the agent can be.
- Actions: There are only 4 actions. Up, Down, Right, Left.


# Run
Run  'Python3 Learner.py'

Challenge
==========================
The challenge was to improve the original [code](https://github.com/llSourcell/q_learning_demo). I improved the code
by changing the following:
- Replace unnececary functions/code.
- Optimize by using list comprehension (loads of for loops were used, while this wasn't neccecary in all cases)
- Use of classes (the game world is now a class, which in my opinion is a cleaner way of coding)
- Merged walls/specials to objects variable.
- Walls give negative result of -100 to discourage the player to ever go there.
- After every reset the player position is changed so that the Q-matrix get initialized quicker. This way we have a higher chance that every cell is touched.
- Dynamic generation of matrix (user can give in his/her own dimensions).
