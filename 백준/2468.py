import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
ary = []
maximum = 0
answer = 1
for _ in range(N):
    temp = list(map(int, input().split()))
    ary.append(temp)
    for i in temp:
        maximum = max(maximum, i)

def is_range(x:int, y:int)->bool:
    return 0<=x<N and 0<=y<N

def BFS(height:int, coord:tuple):
    q = deque()
    q.append(coord)

    while q:
        x,y = q.popleft()
        for dx,dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            tx,ty = x+dx, y+dy

            if is_range(tx,ty) and not visited[tx][ty] and ary[tx][ty]>height:
                visited[tx][ty] = True
                q.append((tx,ty))
    

for d in range(1, maximum):
    temp = 0
    visited = [[False for _ in range(N)] for __ in range(N)]
    for i in range(N):
        for j in range(N):
            if ary[i][j] > d and not visited[i][j]:
                temp +=1
                visited[i][j] = True
                BFS(d, (i,j))
    answer = max(answer,temp)
    
print(answer)