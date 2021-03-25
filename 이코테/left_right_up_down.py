square = int(input())

import sys

path = sys.stdin.readline().rstrip('\n').split()

state = [1,1]

left = [0,-1]
right = [0,1]
up = [-1,0]
down = [1,0]

turn = None

for i in path:

    if i == 'L':
        turn = left
    elif i == 'R':
        turn = right
    elif i == 'U':
        turn = up
    elif i == 'D':
        turn = down
        
    state = [k+j for k,j in zip(state,turn)]
    
    if state[0] == 0:
        state[0] = 1
    elif state[1] == 0:
        state[1] = 1
    elif state[0] > square:
        state[0] = square
    elif state[1] > square:
        state[1] = square

print(state)

