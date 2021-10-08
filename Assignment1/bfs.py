from collections import deque


def isGoalState(n, state):
    chessBoard = [[0] * n for i in range(n)]

    for i, num in enumerate(state):
        chessBoard[num - 1][i] = 1

    for i, num in enumerate(state):
        queenX, queenY = num - 1, i
        
        #right-up
        x, y = queenX, queenY
        while x >= 1 and y <= n - 2:
            if chessBoard[x - 1][y + 1] == 1:
                return False
            x -= 1
            y += 1
        
        #right
        x, y = queenX, queenY
        while y <= n - 2:
            if chessBoard[x][y + 1] == 1:
                return False
            y += 1

        #right-down
        x, y = queenX, queenY
        while x <= n - 2 and y <= n - 2:
            if chessBoard[x + 1][y + 1] == 1:
                return False
            x += 1
            y += 1
    
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
        else:
            checkedState.add(tuple(state))

        for i in range(len(state)):
            if state[i] + 1 <= n:
                nextState = state[:]
                nextState[i] += 1
                Q.append(nextState)

    # no solution
    return []