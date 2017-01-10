__author__ = 'philippe & Mick'
from World import World
import threading
import time

def init_world():
    World = World(100, 5, 5)
    discount = 0.3
    actions = World.ACTIONS
    states = []
    Q = {}

    for i in range(World.AXIS_X):
        for j in range(World.AXIS_Y):
            states.append((i, j))

    for state in states:
        temp = {}
        for action in [item[0] for item in actions]:
            temp[action] = 0.1
        Q[state] = temp

    for (i, j, c, w) in World.SPECIALS:
        for action in [item[0] for item in actions]:
            Q[(i, j)][action] = w

    return World, discount, actions, states, Q

def do_action(action):
    s = World.Player
    r = -World.score
    coords = [i for i in actions if i[0] == action]

    AXIS_X, AXIS_Y = coords[0][1:]
    World.try_move(AXIS_X, AXIS_Y)

    s2 = World.Player
    r += World.score
    return s, action, r, s2


def max_Q(s):
    val = max(list(Q[s].values()))
    pos = [AXIS_X for AXIS_X in Q[s].items() if val == AXIS_X[1]]
    act, val = pos[0]
    
    return act, val

def inc_Q(s, a, alpha, inc):
    Q[s][a] *= 1 - alpha
    Q[s][a] += alpha * inc

def render_game():
    World.render_grid()
    World.board.grid(row=0, column=0)

    World.me = World.board.create_rectangle(World.Player[0]*World.WIDTH+World.WIDTH*2/10, World.Player[1]*World.WIDTH+World.WIDTH*2/10,
        World.Player[0]*World.WIDTH+World.WIDTH*8/10, World.Player[1]*World.WIDTH+World.WIDTH*8/10, fill="orange", width=1, tag="me")


def run(discount):
    time.sleep(1)
    alpha = 1
    t = 1
    while True:
        # render grid
        render_game()
        
        # Pick the right action
        s = World.Player
        max_act, max_val = max_Q(s)
        (s, a, r, s2) = do_action(max_act)

        # Update Q
        max_act, max_val = max_Q(s2)
        inc_Q(s, a, alpha, r + discount * max_val)

        # Check if the game has restarted
        t += 1.0
        if World.has_restarted():
            World.restart_game()
            time.sleep(0.01)
            t = 1.0

        # Update the learning rate
        alpha = pow(t, -0.1)

        # MODIFAXIS_y THIS SLEEP IF THE GAME IS GOING TOO FAST.
        time.sleep(1)
        render_game()

def main(): 
    # init world
    World, discount, actions, states, Q = init_world()

    t = threading.Thread(target=run(discount))
    t.daemon = True
    t.start()

    #World.start_game()
    ##World.board.grid(row=0, column=0)
    #World.render_grid()

if __name__ == '__main__':
    main() 