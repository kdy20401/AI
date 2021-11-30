import os
import random


class State:
    def __init__(self, num, size):
        self.actions = [-1234567890 for i in range(4)]
        self.valid = []
        x = int((num - 1) / size)
        y = (num - 1) % size

        if x > 0:
            self.valid.append(0) # up
        if x < size - 1:
            self.valid.append(1) # down
        if y > 0:
            self.valid.append(2) # right
        if y < size - 1:
            self.valid.append(3) # left

        for v in self.valid:
            self.actions[v] = 0


def main():
    UP      = 0
    DOWN    = 1
    LEFT    = 2
    RIGHT   = 3

    cwd = os.path.dirname(os.path.realpath(__file__))
    f = open(cwd + '/input.txt', 'r')
    lines = f.readlines()
    f.close()

    N = len(lines)
    total_states = goal_state = N * N

    # initialize array rewards[1...N*N]
    rewards = []
    rewards.append(None)
    for line in lines:
        for char in line:
            if char == 'P' or char == 'S':
                reward = 0
                rewards.append(reward)
            elif char == 'T':
                reward = 20
                rewards.append(reward)
            elif char == 'G':
                reward = 100
                rewards.append(reward)
            elif char == 'B':
                reward = -100
                rewards.append(reward)

    # initilize object array states[1...N*N]
    states = []
    states.append(None)
    for i in range(1, total_states + 1):
        states.append(State(i, N))

    # Q learning
    explorations = 1000000
    steps = 1000

    while explorations > 0:
        step = 0
        current_state = 1

        while step < steps:
            if current_state == goal_state or rewards[current_state] == -100:
                break

            direction = random.choice(states[current_state].valid)

            if direction == UP:
                next_state = current_state - N
            elif direction == DOWN:
                next_state = current_state + N
            elif direction == LEFT:
                next_state = current_state - 1
            elif direction == RIGHT:
                next_state = current_state + 1
            
            next_state_q_values = []
            for v in states[next_state].valid:
                next_state_q_values.append(states[next_state].actions[v])
                
            states[current_state].actions[direction] = rewards[next_state] + 0.9 * max(next_state_q_values)
            current_state = next_state
            step += 1

        explorations -= 1

    start_state_q_value = max(states[1].actions)

    # start path finding
    path = []
    current_state = 1

    while current_state != goal_state:
        path.append(current_state)
        
        q_values = []
        for v in states[current_state].valid:
            q_values.append(states[current_state].actions[v])
        max_q_value = max(q_values)
        direction = states[current_state].actions.index(max_q_value)

        if direction == UP:
            next_state = current_state - N
        elif direction == DOWN:
            next_state = current_state + N
        elif direction == LEFT:
            next_state = current_state - 1
        elif direction == RIGHT:
            next_state = current_state + 1
        
        current_state = next_state

    path.append(goal_state)

    # write the result to file
    route = str()
    for state in path:
        route += str(state - 1) + ' '
    route = route[:-1] + '\n'
    q_value = str(start_state_q_value)
    
    cwd = os.path.dirname(os.path.realpath(__file__))
    f = open(cwd + '/output.txt', 'w')
    f.write(route)
    f.write(q_value)
    f.close()

if __name__ == '__main__':
    main()

'''
<maze success to learn>
SPPPB
BTPPB
PPBPT
PPPPP
BBPBG

SBPPP
PBPBP
PBPBP
PPPBP
BBBBG
'''