import sys
from collections import deque

N,M = map(int, sys.stdin.readline().rstrip('\n').split())

maze = [list(map(int,sys.stdin.readline().rstrip('\n'))) for _ in range(N)]
axis_x = [1,0,0,-1]
axis_y = [0,1,-1,0]

maze[0][0]=0

def bfs(maze):
    q = deque([(0,0,1)])
    while q:
        x,y,c = q.popleft()

        for i in range(4):
            mx = x + axis_x[i]
            my = y + axis_y[i]

            if mx == N-1 and my == M-1:
                return c +1

            if 0<= mx <N and 0<= my <M:
                if maze[mx][my] == 1:
                    q.append((mx,my,c+1))
                    maze[mx][my] = 0

print(bfs(maze))