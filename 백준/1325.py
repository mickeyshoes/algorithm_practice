import sys
from collections import defaultdict,deque
input = sys.stdin.readline

N,M = map(int, input().rstrip('\n').split())
d = defaultdict(list)

for _ in range(M):
    a,b = map(int, input().rstrip('\n').split())
    d[b].append(a)

def bfs(start:int, d:dict, m:int):
    q = deque([])
    visited = [False] * m
    q.append(start)
    visited[start-1] = True
    count = 0
    while q:
        node = q.popleft()
        count +=1
        for n in d[node]:
            if not visited[n-1]:
                visited[n-1] = True
                q.append(n)
    return count

answer = []
temp = 0
for i in range(1,N+1):
    if d[i]:
        a = bfs(i,d,N)
        if temp <= a:
            if temp < a:
                answer = []
                temp = a
            answer.append(i)
print(*answer)