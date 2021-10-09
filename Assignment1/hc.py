import random

RESTART_CNT = 30
MAXSTUCK_CNT = 5

def get_next_state(n, state, chessBoard):
    states = {}

    for i, num in enumerate(state):
        row = num - 1
        col = i

        for j in range(n):
            if j == row:
                continue
            
            chessBoard[row][col] = 0
            chessBoard[j][col] = -1
            tmpState = state[:]
            tmpState[col] = j + 1
            h = heuristic_func(n, tmpState, chessBoard)
            chessBoard[j][col] = h
            chessBoard[row][col] = -1

            states[tuple(tmpState)] = h

    states = dict(sorted(states.items(), key=lambda x: x[1], reverse=False))
    k = list(states.keys())[0]
    v = states[k]

    nextState = list(k)
    h = v
    return nextState, h 


def heuristic_func(n, state, chessBoard):
    cnt = 0

    for i, num in enumerate(state):
        queenX, queenY = num - 1, i
        
        #right-up
        x, y = queenX, queenY
        while x >= 1 and y <= n - 2:
            if chessBoard[x - 1][y + 1] == -1:
                cnt += 1
            x -= 1
            y += 1
        
        #right
        x, y = queenX, queenY
        while y <= n - 2:
            if chessBoard[x][y + 1] == -1:
                cnt += 1
            y += 1

        #right-down
        x, y = queenX, queenY
        while x <= n - 2 and y <= n - 2:
            if chessBoard[x + 1][y + 1] == -1:
                cnt += 1
            x += 1
            y += 1
    
    return cnt


def initialize_chessBoard(n, state):
    chessBoard = [[0] * n for i in range(n)]
    for i, num in enumerate(state):
        chessBoard[num - 1][i] = -1
    
    return chessBoard


def hc(n):
    global RESTART_CNT, MAXSTUCK_CNT
    restartCnt = RESTART_CNT
    stuckCnt = h = h1 = 0

    while restartCnt > 0:
        # generate random state
        state = [random.randrange(1, n + 1) for i in range(n)]
        chessBoard = initialize_chessBoard(n, state)
        
        while h >= h1 and stuckCnt <= MAXSTUCK_CNT:
            h = heuristic_func(n, state, chessBoard)
            if h == 0:
                return state

            nextState, h1 = get_next_state(n, state, chessBoard)
            if h1 == 0:
                return nextState

            if h == h1:
                stuckCnt += 1
            else:
                stuckCnt = 0

            # update state
            state = nextState
            chessBoard = initialize_chessBoard(n, state)
                
        restartCnt -= 1
        stuckCnt = h = h1 = 0


    return []
