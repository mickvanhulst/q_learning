Introduction
==========================
The challenge was to build a Q-learning algorithm by using existing code (which I referenced in the credits). The header mprovements describes which improvements I made.

Run
==========================
Run  'Python3 Learner.py'

Improvements
==========================
I improved the code by changing the following:
- Replace unnececary functions/code (LOTS of code cleaning).
- Optimize by using list comprehension (loads of for loops were used, while this wasn't neccecary in all cases)
- Use of classes ('World' is now a class, which in my opinion is a cleaner way of coding)
- Merged walls/specials to objects variable.
- Walls give a negative result of -1 to discourage the bot to go near. I could have used a very high value,
but I believe we want the bot to totally avoid the red square and avoid (as much as possible) the walls.
If we tell the player that there is a huge loss for touching the wall, then the bot won't go near the walls anymore,
which is a problem since there are lots of them. We want the bot to know that it shouldn't go near the walls,
but it should also know that there is a higher loss for going near the red squares.
- After every reset the player position is changed so that the Q-matrix get initialized quicker. This way we have a higher chance that every cell is touched.
- Extra function so that player/green square is not initialized on an already exisiting object position
- Dynamic generation of matrix (user can give in his/her own dimensions).

I thought about generating a random matrix everytime the game restarts. However this wouldn't make much sense,
since you're trying to find the optimal path and by changing the matrix, the optimal path would change. So I decided
to not make that change.

# Example
Below is an example of a randomly generated matrix (10x10). This is however not the max. The user can give in any
value he/she wants.
![sample_grid_q_learning](https://github.com/mickvanhulst/q_learning/blob/master/example_grid.jpg)


Summary
==========================
Simple Reinforcement learning example, based on the Q-function.
- Rules: The agent (yellow box) has to reach one of the goals to end the game (green or red cell).
- Rewards: Each step gives a negative reward of -0.04. The red cell gives a negative reward of -5. The green one gives a positive reward of +5. The black walls give a negative reward of -1.
- States: Each cell is a state the agent can be.
- Actions: There are only 4 actions. Up, Down, Right, Left.

Credits
===========
Credit for the vast majority of code here goes to [PhilippeMorere](https://github.com/PhilippeMorere). 

Credits for being awesome go to @[Sirajology](https://www.youtube.com/sirajology) for enabling us to learn so much about ML!
