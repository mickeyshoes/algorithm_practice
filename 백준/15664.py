import sys
input = sys.stdin.readline

N,M = map(int, input().rstrip('\n').split())
items = list(map(int, input().rstrip('\n').split()))
items.sort()
stack = []
visited = [False] * N

def DFS(idx:int)->None:
    if len(stack) == M:
        print(*stack)
        return

    prev_value = 0
    for i in range(idx, N):
        if not visited[i] and prev_value != items[i]:
            stack.append(items[i])
            visited[i] = True
            DFS(i+1)
            prev_value = stack.pop()
            visited[i] = False

DFS(0)