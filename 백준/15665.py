import sys
input = sys.stdin.readline

N,M = map(int, input().rstrip('\n').split())
items = list(map(int, input().rstrip('\n').split()))
items.sort()
stack =[]

def DFS():
    if len(stack) == M:
        print(*stack)
        return
    overlap = -1
    for i in range(N):
        if items[i] != overlap:
            stack.append(items[i])
            DFS()
            overlap = stack.pop()
DFS()