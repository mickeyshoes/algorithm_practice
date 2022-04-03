import sys

N, M = map(int, sys.stdin.readline().rstrip('\n').split())
value_stack = []
visited = [False] * (N+1)

def DFS(start:int)->None:

    if len(value_stack) == M:
        print(*value_stack)
        return

    for i in range(start, N+1):
        if visited[i]:
            continue

        value_stack.append(i)
        visited[i] = True
        DFS(i+1)
        value_stack.pop()
        visited[i] = False

DFS(1)
