from World import World
import threading
import time

def init_vars(game):
    discount = 0.3
    actions = game.ACTIONS
    states = []
    Q = {}

    # Create base for Q-matrix
    for i in range(game.AXIS_X):
        for j in range(game.AXIS_Y):
            states.append((i, j))

    for state in states:
        temp = {}
        for action in [item[0] for item in actions]:
            temp[action] = 0.1
        Q[state] = temp

    for (i, j, c, w) in game.OBJECTS:
        for action in [item[0] for item in actions]:
            Q[(i, j)][action] = w

    return discount, actions, Q

def do_action(action, game, actions):
    s = game.Player
    r = -game.score
    coords = [i for i in actions if i[0] == action]

    x, y = coords[0][1:]
    game.try_move(x, y)

    s2 = game.Player
    r += game.score
    return s, action, r, s2


def max_Q(s, Q):
    val = max(list(Q[s].values()))
    pos = [AXIS_X for AXIS_X in Q[s].items() if val == AXIS_X[1]]
    act, val = pos[0]
    
    return act, val

def inc_Q(s, a, alpha, inc, Q):
    Q[s][a] *= 1 - alpha
    Q[s][a] += alpha * inc

def render_game(game):
    game.render_grid()
    game.board.grid(row=0, column=0)
    base_1 = game.WIDTH+(game.WIDTH*0.2)
    base_2 = game.WIDTH+(game.WIDTH*0.8)
    
    game.me = game.board.create_rectangle(game.Player[0]*base_1, game.Player[1]*base_2,
        game.Player[0]*base_1, game.Player[1]*base_2, 
        fill="orange", width=1, tag="me")

def run(discount, game, Q, actions):
    time.sleep(1)
    alpha = 1
    t = 1
    while True:   
        # Pick the right action
        s = game.Player
        max_act, max_val = max_Q(s, Q)
        (s, a, r, s2) = do_action(max_act, game, actions)

        # Update Q
        max_act, max_val = max_Q(s2, Q)
        inc_Q(s, a, alpha, r + discount * max_val, Q)

        # Check if the game has restarted
        t += 1.0
        if game.has_restarted():
            game.restart_game()
            time.sleep(0.01)
            t = 1.0

        # Update the learning rate
        alpha = pow(t, -0.1)

        # MODIFAXIS_y THIS SLEEP IF THE GAME IS GOING TOO FAST.
        time.sleep(0.3)

        # render game
        render_game(game)

def main(): 
    # Init game -- input: width, x_axis & y_axis
    game = World(100, 5, 5)
    
    # Init vars
    discount, actions, Q = init_vars(game)
    
    # Start game
    t = threading.Thread(target=run, args=(discount, game, Q, actions))
    t.daemon = True
    t.start()
    game.start_game()
    
if __name__ == '__main__':
    main() 
