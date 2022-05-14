import sys
from itertools import combinations
input = sys.stdin.readline

N = int(input().rstrip('\n'))
jobs = list(map(int, input().rstrip('\n').split()))

# def calculate_friday(i:int):
#     for comb in combinations(jobs, i):
#         if sum(comb) % 7 == 4:
#             return True
#     return False

# flag = False
# for i in range(1, N+1):
#     if calculate_friday(i):
#         flag = True
#         break

# print('YES') if flag else print('NO')

stack = []
ans = [False]
visited = [False] * (N+1)
def DFS(sum_value:int):

    if sum_value % 7 == 4:
        ans[0] = True
        return

    if len(stack) == N:
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            stack.append(jobs[i])
            sum_value += jobs[i]
            DFS(sum_value)
            sum_value -= jobs[i]
            visited[i] = False
            stack.pop()

DFS(0)
print('YES') if ans[0] else print('NO')