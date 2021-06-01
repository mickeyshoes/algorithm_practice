import sys
from queue import Queue

M,N = map(int, sys.stdin.readline().rstrip('\n').split())

farm = []
tomato = []
mx = [-1,1,0,0]
my = [0,0,-1,1]

for i in range(N):
    farm.append(list(map(int, sys.stdin.readline().rstrip('\n').split())))
    for j in range(len(farm[i])):
        if farm[i][j] == 1:
            tomato.append((i,j))

def bfs(tomato_list : list):
    q = Queue()
    for tomato in tomato_list:
        q.put(tomato)
    while q.qsize() > 0:
        tx,ty = q.get()

        for i in range(len(mx)):
            nx = tx + mx[i]
            ny = ty + my[i]

            if 0<= nx <N and 0<= ny <M:
                if farm[nx][ny] == 0:
                    q.put((nx,ny))
                    farm[nx][ny] = farm[tx][ty]+1
                    
# 1이 2개 이상 있는 경우 동시에 동작해야 하므로 1이 포함된 자표 리스트를 넣어준다.
bfs(tomato)
count = 0
zero_check = False
for i in range(N):
    for j in range(M):
        if farm[i][j] == 0:
            zero_check = True
            break
        count = max(count, farm[i][j])

if zero_check:
    print(-1)
else:
    print(count-1)