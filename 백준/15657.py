import sys
input = sys.stdin.readline

N,M = map(int, input().rstrip('\n').split())
items = list(map(int, input().rstrip('\n').split()))
items.sort()
stack = []

def DFS(idx:int)->None:
    if len(stack) == M:
        print(*stack)
        return

    for i in range(idx, len(items)):
        stack.append(items[i])
        DFS(i)
        stack.pop()

DFS(0)