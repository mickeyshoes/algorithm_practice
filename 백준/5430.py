import sys
from collections import deque
input = sys.stdin.readline

def solution():
    command = input().rstrip('\n')
    arr_len = int(input().rstrip('\n'))
    arr = deque(input().lstrip('[').rstrip(']\n').split(','))

    if arr[0] == '':
        arr = deque()
    
    reverse = False
    for i in command:
        if i == 'R':
            reverse ^= True
        if i == 'D':
            try:
                if not reverse:
                    arr.popleft()
                else:
                    arr.pop()
            except IndexError:
                print('error')
                return

    a = len(arr)
    if reverse:
        arr.reverse()
    answer = '['
    for i in range(a):
        if i == a-1:
            answer += arr[i]
        else:
            answer += f'{arr[i]},'
    answer +=']'
    print(answer)

N = int(input().rstrip('\n'))
for _ in range(N):
    solution()