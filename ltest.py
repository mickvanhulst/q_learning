__author__ = 'philippe & Mick'
from World import World
import threading
import time

def init_vars(game_world):
    discount = 0.3
    actions = game_world.ACTIONS
    states = []
    Q = {}

    for i in range(game_world.AXIS_X):
        for j in range(game_world.AXIS_Y):
            states.append((i, j))

    for state in states:
        temp = {}
        for action in [item[0] for item in actions]:
            temp[action] = 0.1
        Q[state] = temp

    for (i, j, c, w) in game_world.SPECIALS:
        for action in [item[0] for item in actions]:
            Q[(i, j)][action] = w

    return discount, actions, states, Q

def do_action(action, game_world, actions):
    s = game_world.Player
    r = -game_world.score
    coords = [i for i in actions if i[0] == action]

    AXIS_X, AXIS_Y = coords[0][1:]
    game_world.try_move(AXIS_X, AXIS_Y)

    s2 = game_world.Player
    r += game_world.score
    return s, action, r, s2


def max_Q(s, Q):
    val = max(list(Q[s].values()))
    pos = [AXIS_X for AXIS_X in Q[s].items() if val == AXIS_X[1]]
    act, val = pos[0]
    
    return act, val

def inc_Q(s, a, alpha, inc, Q):
    Q[s][a] *= 1 - alpha
    Q[s][a] += alpha * inc

def render_game(game_world):
    game_world.render_grid()
    game_world.board.grid(row=0, column=0)

    game_world.me = game_world.board.create_rectangle(game_world.Player[0]*game_world.WIDTH+game_world.WIDTH*2/10, game_world.Player[1]*game_world.WIDTH+game_world.WIDTH*2/10,
        game_world.Player[0]*game_world.WIDTH+game_world.WIDTH*8/10, game_world.Player[1]*game_world.WIDTH+game_world.WIDTH*8/10, fill="orange", width=1, tag="me")


def run(discount, game_world, Q, actions):
    time.sleep(1)
    alpha = 1
    t = 1
    while True:
        # render grid
        render_game(game_world)
        
        # Pick the right action
        s = game_world.Player
        max_act, max_val = max_Q(s, Q)
        (s, a, r, s2) = do_action(max_act, game_world, actions)

        # Update Q
        max_act, max_val = max_Q(s2, Q)
        inc_Q(s, a, alpha, r + discount * max_val, Q)

        # Check if the game has restarted
        t += 1.0
        if game_world.has_restarted():
            game_world.restart_game()
            time.sleep(0.01)
            t = 1.0

        # Update the learning rate
        alpha = pow(t, -0.1)

        # MODIFAXIS_y THIS SLEEP IF THE GAME IS GOING TOO FAST.
        time.sleep(0.1)

def main(): 
    # Init game_world
    game_world = World(100, 5, 5)
    
    # Init vars
    discount, actions, states, Q = init_vars(game_world)
    
    # Start game
    t = threading.Thread(target=run, args=(discount, game_world, Q, actions))
    t.daemon = True
    t.start()
    game_world.start_game()
    

if __name__ == '__main__':
    main() 