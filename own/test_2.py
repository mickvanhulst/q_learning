import numpy as np
import time

def test(matrix_q, pos, path):
    # Loop till pos 5 is reached (end-point)
    while pos != 5:
        # get next_step
        next_step_index = np.where(matrix_q[pos,] == np.max(matrix_q[pos,]))[1]
        prev_index = next_step_index

        if next_step_index.shape[0] > 1:
            next_step_index = int(np.random.choice(next_step_index, size = 1))
        else:
            next_step_index = int(next_step_index)
    
        path.append(next_step_index)
        pos = next_step_index
        print(pos)

    return path

def training():
    # init params
    matrix_r, matrix_q, gamma = init_params()

    # Determine how many iterations to run to populate q-matrix.
    # while pos touched is untrue
    matrix_touch = np.copy(matrix_q)
    #while len(np.transpose(np.nonzero(matrix_touch))) < 36:
    for i in range(10000):
        print('---------a--------------')
        print(len(np.transpose(np.nonzero(matrix_touch))))
        #time.sleep(5)
        # Generate random current state
        current_state = np.random.randint(0, int(matrix_q.shape[0]))
        # Get available actions
        av_act = available_actions(current_state, matrix_r)
        #print(av_act)
        
        # Randomly select next action, if no action available, retrain with new matrix.
        n_action = next_action(av_act)
        #print(n_action)
        # Update q-matrix
        update(current_state, n_action, gamma, matrix_q, matrix_r, matrix_touch)

    # If q-matrix does not contain the value 100, then there is no optimal path.
    print(matrix_touch)
    return matrix_q

def update(state, action, gamma, matrix_q, matrix_r, matrix_touch):
    #print(action)
    max_index = np.where(matrix_q[action,] == np.max(matrix_q[action,]))[1]

    if max_index.shape[0] > 1:
        max_index = int(np.random.choice(max_index, size = 1))
    else:
        max_index = int(max_index)
    
    max_value = matrix_q[action, max_index]
    
    # Q learning formula
    matrix_q[state, action] = matrix_r[state, action] + gamma * max_value
    matrix_touch[state, action] = 1


def next_action(av_act):
    n_action = int(np.random.choice(av_act, 1))

    return n_action

def available_actions(state, matrix_r):
    # Get all available actions that have a reward that is >= 0
    current_state_row = matrix_r[state,]
    av_act = np.where(current_state_row >= 0)[1]
    
    return av_act

def gen_random_matrix(dimension_x, dimension_y):
    weights = [0.65, 0.35]
    choices = [-1, 0]
    matrix = np.matrix(np.zeros([dimension_x, dimension_y]))

    # Edit matrix with random values
    for y in range(dimension_y):
        row_x = []
        for x in range(dimension_x):
            row_x.append(np.random.choice(choices, p=weights))
        matrix[y] = row_x

    # Append one random 100 value to fifth row (which is the goal)
    x = np.random.choice(matrix.shape[1])
    matrix[5, x] = 100

    return matrix

def init_params():
    # -1 means that the program cannot move to that point. This can either be compared with a wall.
    # Reward matrix, states x actions
    matrix_r = gen_random_matrix(6, 6)

    # Q learning matrix.
    # Represents the memory of what the agent has learned through experience.
    matrix_q = np.matrix(np.zeros(matrix_r.shape))

    # init gamma (learning rate)
    gamma = 0.8

    return matrix_r, matrix_q, gamma

def main():
    # Train
    matrix_q = training()

    # Q-matrix is result of training
    print("Trained Q matrix:")
    #print(matrix_q/np.max(matrix_q)*100)
    print(matrix_q)

    # Test using start_pos 2
    start_pos = 2
    path = [start_pos]

    # Calculate optimal path
    #path = test(matrix_q, start_pos, path)

    print('Optimal path:')
    print(path)


if __name__ == '__main__':
    main()