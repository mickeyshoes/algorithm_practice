import sys
input = sys.stdin.readline

N,M = map(int, input().rstrip('\n').split())
items = list(map(int, input().rstrip('\n').split()))
items.sort()
stack = []

def DFS():
    if len(stack) == M:
        print(*stack)
        return

    for i in range(len(items)):
        stack.append(items[i])
        DFS()
        stack.pop()

DFS()