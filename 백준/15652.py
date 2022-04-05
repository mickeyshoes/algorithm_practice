import sys

N,M = map(int, sys.stdin.readline().rstrip('\n').split())
stack = []
visited = [False] * (N+1)

def DFS():
    if len(stack) == M:
        print(*stack)
        return

    for i in range(1, N+1):

        if stack:
            if stack[-1]>i:
                continue

        stack.append(i)
        DFS()
        stack.pop()

DFS()