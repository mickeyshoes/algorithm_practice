import sys
input =sys.stdin.readline
N = int(input().rstrip('\n'))
M = int(input().rstrip('\n'))

snail = [[0]*N for _ in range(N)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]
input_value = N*N
x,y,control = 0,0,0

answer = []
while input_value != 0:
    snail[x][y] = input_value
    if snail[x][y] == M:
        answer.append(x+1)
        answer.append(y+1)

    nx = x + dx[control]
    ny = y + dy[control]

    # 범위를 벗어나거나 값이 이미 들어가 있는 경우 방향을 바꾸어줘야 한다
    if nx >= N or ny >= N or nx <0 or ny <0 or snail[nx][ny] !=0:
        control = (control + 1) % 4
        nx = x + dx[control]
        ny = y + dy[control]

    input_value -=1
    x = nx
    y = ny

for i in snail:
    print(*i)
print(*answer)