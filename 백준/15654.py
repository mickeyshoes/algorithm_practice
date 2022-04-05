import sys
input = sys.stdin.readline

N,M = map(int, input().rstrip('\n').split())
items = list(map(int, input().rstrip('\n').split()))
items.sort()
stack = []
visited = [False] * N

def DFS():
    if len(stack) == M:
        print(*stack)
        return

    for i in range(len(items)):

        if not visited[i]:
            visited[i] = True
            stack.append(items[i])
            DFS()
            visited[i] = False
            stack.pop()

DFS()