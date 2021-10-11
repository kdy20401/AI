import random

RESTART_CNT = 30
MAXSTUCK_CNT = 5

# return the next state with the lowest heuristic function value
# and that value
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


# returns the number of pairs of queen attacking each other
def heuristic_func(n, state, chessBoard):
    cnt = 0

    for i, num in enumerate(state):
        queenX, queenY = num - 1, i
        
        # attack to the right-up direction 
        x, y = queenX, queenY
        while x >= 1 and y <= n - 2:
            if chessBoard[x - 1][y + 1] == -1:
                cnt += 1
            x -= 1
            y += 1
        
        # attack to the right direction 
        x, y = queenX, queenY
        while y <= n - 2:
            if chessBoard[x][y + 1] == -1:
                cnt += 1
            y += 1

        # attack to the right-down direction 
        x, y = queenX, queenY
        while x <= n - 2 and y <= n - 2:
            if chessBoard[x + 1][y + 1] == -1:
                cnt += 1
            x += 1
            y += 1
    
    return cnt


def create_chessBoard(n, state):
    chessBoard = [[0] * n for i in range(n)]
    # mark queens' locations
    for i, num in enumerate(state):
        chessBoard[num - 1][i] = -1

    return chessBoard


# hill climbing method
def hc(n):
    global RESTART_CNT, MAXSTUCK_CNT
    restartCnt = RESTART_CNT
    stuckCnt = h0 = h1 = 0

    # to avoid the heuristic function value stucks at local minimum, do random restarts
    while restartCnt > 0:
        currentState = [random.randrange(1, n + 1) for i in range(n)]
        chessBoard = create_chessBoard(n, currentState) 

        h0 = heuristic_func(n, currentState, chessBoard)
        if h0 == 0:
            return currentState

        # expand states until the value of heuristic function reaches global or local minimum
        while h0 >= h1 and stuckCnt <= MAXSTUCK_CNT:
            nextState, h1 = get_next_state(n, currentState, chessBoard)
            # global minimum value
            if h1 == 0:
                return nextState

            if h0 == h1:
                stuckCnt += 1
            else:
                stuckCnt = 0

            h0 = h1
            currentState = nextState
            # make a new chess board because state has been changed
            chessBoard = create_chessBoard(n, currentState)
                
        # initialize variables after reaching local minimum
        stuckCnt = h0 = h1 = 0
        restartCnt -= 1

    return []
