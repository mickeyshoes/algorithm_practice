from re import L
import sys
input= sys.stdin.readline
N = int(input().rstrip('\n'))

items = list(range(10))
stack =[]

def DFS(idx:int, limit:int):
    if len(stack) == limit:
        print(*stack)
        return

    for i in range(idx):
        stack.append(items[i])
        DFS(i, limit)
        stack.pop()


for i in range(3):
    DFS(,i)
