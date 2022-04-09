import sys
input = sys.stdin.readline

N,M = map(int, input().rstrip('\n').split())
items = sorted(list(map(int, input().rstrip('\n').split())))
stack = []

def DFS(idx:int)->None:

    if len(stack) == M:
        print(*stack)
        return
    
    overlap = -1
    for i in range(idx, N):
        if overlap != items[i]:
            stack.append(items[i])
            DFS(i)
            overlap = stack.pop()

DFS(0)