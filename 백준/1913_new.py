import sys
input = sys.stdin.readline

N = int(input().rstrip('\n'))
M = int(input().rstrip('\n'))
ary = [[0 for _ in range(N)] for __ in range(N)]
dxs, dys = [1,0,-1,0], [0,1,0,-1]
x,y,dir = 0,0,0
answer = []
ary[0][0] = N*N

def is_range(x:int, y:int)->bool:
    return 0<=x<N and 0<=y<N

for i in range(N*N-1, 0, -1):
    nx,ny = x+ dxs[dir], y+ dys[dir]

    if not is_range(nx,ny) or ary[nx][ny] != 0:
        dir = (dir+1)%4

    x,y, = x+dxs[dir], y+dys[dir]
    ary[x][y] = i

for i in ary:
    print(*i)
for i in range(N):
    for j in range(N):
        if ary[i][j] == M:
            print(i+1, j+1)
            break