import sys
input = sys.stdin.readline

N,M = map(int, input().rstrip('\n').split())
items = list(map(int, input().rstrip('\n').split()))
items.sort()
stack = []
visited =[False] * N

# permutation 을 구하고 조건에 맞지 않는 원소 제거하는게 나을듯
def DFS():
    if len(stack) == M:
        print(*stack)
        return
    prev_value = 0
    for i in range(len(items)):
        if not visited[i] and prev_value != items[i]:
            stack.append(items[i])
            visited[i] = True
            DFS()
            prev_value = stack.pop()
            visited[i] = False

DFS()