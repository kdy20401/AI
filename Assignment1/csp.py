from collections import deque
import copy


def eliminate_illegal_value(N, n, state, pool):
    Q = deque()
    updatedPool = copy.deepcopy(pool)

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

    # updates pool
    while len(Q) > 0:
        coord = Q.popleft()
        row, col = coord[1], coord[0] # watch out order!
        updatedPool[row][col] = -1
    
    return updatedPool


def is_empty(values):
    for value in values:
        if value != -1:
            return False
    
    return True


def forward_check(N, n, state, pool):
    # value is assigned to all variable in state
    if n == 0:
        return True

    # target values are like pool[0], pool[1], pool[2],,,
    # which are queen1's, queen2's, queen3's,, possible values
    targetValues = pool[N - n]

    # if there is no possible values, backtracking!
    if is_empty(targetValues):
        return False

    for value in targetValues:
        # value is not allowed to be assigned
        if value == -1:
            continue
            
        # NOTE: state is stored in reverse order
        state[n - 1] = value
        updatedPool = eliminate_illegal_value(N, n, state, pool)

        ret = forward_check(N, n - 1, state, updatedPool)

        if ret == True:
            return True
    
    return False


def generate_value_pool(n):
    pool = []

    for i in range(n):
        values = []
        for j in range(n):
            values.append(j + 1)
        pool.append(values)

    return pool


def csp(n):
    N = n
    state = [0] * n
    pool = generate_value_pool(n)

    ret = forward_check(N, n, state, pool)

    if ret == True:
        return state[::-1]
    else:
        return []


'''
N-Queens Problem Explanation


<3x3 chess board>
     -  *  -         '*': a queen
     *  -  -         '-': an empty sapce
     -  -  *
     q1 q2 q3 
if queens' locations are like this, the coordinate of 
queen1 is [1,0]
queen2 is [0,1]
queen3 is [2,2].
and state representing this chess board is [3, 1, 2].
so reverse of state which is [2, 1, 3] shows the current layout of queens.
this is not a goal state because queen1 can attack queen2.


<4x4 chess board>
   *  -  -  -
   -  -  -  -
   -  -  -  -
   -  -  -  -
   q1 q2 q3 q4
if queens' locations are like this, the coordinate of
queen1 is [1,0]
queen2 is undefined
queen3 is undefined
queen4 is undefined.
by the characteristic of N-queens problem, chess board becomes

<4x4 chess board>
   *  x  x  x
   -  x  -  -
   -  -  x  -
   -  -  -  x
   q1 q2 q3 q4
like this. queen is not allowed to be at x where another queens can be attacked.
at this moment, the state is [0, 0, 0, 1].
so, reverse of state array shows the current layout of queens.
that is, reverse of state is [1, 0, 0, 0] which means queen1 is located at [0,0].
and pool(legal values for each queen) is

pool = [
    [1, 2, 3, 4],   # queen1  
    [-1, -1, 3, 4], # queen2
    [-1, 2, -1, 4], # queen3
    [-1, 2, 3, -1]  # queen4
]
like this.

pool[1] = [-1, -1, 3, 4] means queen2 can have 3 or 4 for state value
pool[2] = [-1, 2, -1, 4] means queen2 can have 2 or 4 for state value
pool[3] = [-1, 2, 3, -1] means queen3 can have 2 or 3 for state value
as state changes, pool is updated.

if reverse of state is [2, 4, 1, 3], chess board is like
<4x4 chess board>
     -  -  *  -
     *  -  -  -
     -  -  -  *
     -  *  -  -
     q1 q2 q3 q4
'''