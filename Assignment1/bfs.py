from collections import deque
import copy


def isGoalState(n, state):
    queenCoord = set()

    for i, num in enumerate(state):
        queenCoord.add((num - 1, i))
    
    for i, num in enumerate(state):
        queenX, queenY = num - 1, i

        #up
        x, y = queenX, queenY
        while x >= 1:
            if (x - 1, y) in queenCoord:
                return False
            x -= 1

        #right-up
        x, y = queenX, queenY
        while x >= 1 and y <= n - 2:
            if (x - 1, y + 1) in queenCoord:
                return False
            x -= 1
            y += 1
        
        #right
        x, y = queenX, queenY
        while y <= n - 2:
            if (x, y + 1) in queenCoord:
                return False
            y += 1

        #right-down
        x, y = queenX, queenY
        while x <= n - 2 and y <= n - 2:
            if (x + 1, y + 1) in queenCoord:
                return False
            x += 1
            y += 1

        #down
        x, y = queenX, queenY
        while x <= n - 2:
            if (x + 1, y) in queenCoord:
                return False
            x += 1

        #left-down
        x, y = queenX, queenY
        while x <= n - 2 and y >= 1:
            if (x + 1, y - 1) in queenCoord:
                return False
            x += 1
            y -= 1

        #left
        x, y = queenX, queenY
        while y >= 1:
            if (x, y - 1) in queenCoord:
                return False
            y -= 1

        #left-up
        x, y = queenX, queenY
        while x >= 1 and y >= 1:
            if (x - 1, y - 1) in queenCoord:
                return False
            x -= 1
            y -= 1
    
    print('goal state found!')

    return True


def bfs(n):
    checkedState = set()
    Q = deque()

    startState = [1] * n
    Q.append(startState)

    while len(Q) > 0:
        state = Q.popleft()
        
        if isGoalState(n, state):
            return state

        if tuple(state) in checkedState:
            continue
        checkedState.add(tuple(state))

        for i in range(len(state)):
            nextState = copy.deepcopy(state)
            nextState[i] += 1

            if nextState[i] <= n and tuple(nextState) not in checkedState:
                Q.append(nextState)

    # no solution
    return []