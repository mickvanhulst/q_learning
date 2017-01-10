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
- Extra function so that player/green square is not initialized on an already exisiting object position
- Dynamic generation of matrix (user can give in his/her own dimensions).

# Things that crossed my mind and why I didn't do them
I thought about generating a random matrix everytime the game restarts. However this wouldn't make much sense,
since you're trying to find the optimal path and by changing the matrix, the optimal path would change.

# Example
Below is an example of a randomly generated matrix (10x10). This is however not the max. The user can give in any
value he/she wants.
![sample_grid_q_learning](https://github.com/mickvanhulst/q_learning/blob/master/example_grid.jpg)

Credits
===========
Credit for the vast majority of code here goes to [PhilippeMorere](https://github.com/PhilippeMorere). 

Credits for being awesome go to @[Sirajology](https://www.youtube.com/sirajology) for enabling us to learn so much about ML!
