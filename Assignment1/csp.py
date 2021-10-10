from collections import deque
import copy


def isGoalState(N, state):
    cnt = 0
    chessBoard = [[0] * N for i in range(N)]

    for i, num in enumerate(state):
        chessBoard[num - 1][i] = -1

    for i, num in enumerate(state):
        queenX, queenY = num - 1, i
        
        #right-up
        x, y = queenX, queenY
        while x >= 1 and y <= N - 2:
            if chessBoard[x - 1][y + 1] == -1:
                return False
            x -= 1
            y += 1
        
        #right
        x, y = queenX, queenY
        while y <= N - 2:
            if chessBoard[x][y + 1] == -1:
                return False
            y += 1

        #right-down
        x, y = queenX, queenY
        while x <= N - 2 and y <= N - 2:
            if chessBoard[x + 1][y + 1] == -1:
                return False
            x += 1
            y += 1
    
    return True


def eliminate_illegal_value(n, state, values):
    Q = deque()
    fixedValues = copy.deepcopy(values)
    N = len(state)

    queenX, queenY = state[n - 1] - 1, N - n

    # right-up
    x, y = queenX, queenY
    while x >= 1 and y <= N - 2:
        Q.append([x - 1, y + 1])
        x -= 1
        y += 1
    
    # right
    x, y = queenX, queenY
    while y <= N - 2:
        Q.append([x, y + 1])
        y += 1

    # right-down
    x, y = queenX, queenY
    while x <= N - 2 and y <= N - 2:
        Q.append([x + 1, y + 1])
        x += 1
        y += 1

    # updates values
    while len(Q) > 0:
        coord = Q.popleft()
        row, col = coord[1], coord[0]
        fixedValues[row][col] = -1
    
    
    return fixedValues


def legal_value_exists(values):
    for value in values:
        if value != -1:
            return True
    
    return False


def forward_checking_recursive(n, state, values):
    N = len(state)

    if n == 0:
        print('reached!')
        return True

    if not legal_value_exists(values[N - n]):
        return False

    for value in values[N - n]:
        if value == -1:
            continue
            
        # state is stored in reverse order
        state[n - 1] = value
        print('state', state)
        fixedValues = eliminate_illegal_value(n, state, values)
        print('fixedValues', fixedValues)
        ret = forward_checking_recursive(n - 1, state, fixedValues)
        if ret == True:
            return True
        else:
            state[n - 1] = 0



def csp(n):
    state = [0] * n
    values = []

    for i in range(n):
        tmp = []
        for j in range(n):
            tmp.append(j + 1)
        values.append(tmp)

    forward_checking_recursive(n, state, values)
    state = state[::-1]

    if isGoalState(n, state):
        return state
    else:
        return []