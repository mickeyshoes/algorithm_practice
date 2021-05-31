import sys
from collections import deque

start, end = map(int, sys.stdin.readline().rstrip('\n').split())

q = deque()
visited = [False] * 100001
q.append((start,0))

while q:
    t, c = q.popleft()

    if t == end:
        print(c)
        break

    else:
        t = [t-1, t+1, 2*t]
        for i in t:
            if 0<= i <=100000 and not visited[i-1]:
                q.append((i,c+1))
                visited[i-1] = True