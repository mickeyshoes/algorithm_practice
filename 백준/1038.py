import sys
input= sys.stdin.readline
N = int(input().rstrip('\n'))
temp=[0]

def DFS(stack:list, limit:int, idx:int)->None:

    if len(stack) == limit:
        print(*stack)
        return

    for i in range(idx,-1,-1):
        stack.append(i)
        DFS(stack, limit, i)
        stack.pop()

DFS([], 1, 0)