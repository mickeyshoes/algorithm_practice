import sys
from queue import Queue

N = int(sys.stdin.readline().rstrip('\n'))

map = []
visited = [[False]* N for _ in range(N)]

dx = [1,0,0,-1]
dy = [0,1,-1,0]

def bfs(x : int, y : int):
    q = Queue()
    q.put((x,y))
    visited[x][y] = True
    count = 0

    while q.qsize() > 0:
        a,b = q.get()
        # print(f'visited {a},{b}')
        count +=1
        for i in range(len(dx)):
            check_x = a + dx[i]
            check_y = b + dy[i]

            if check_x < 0 or check_x >= N or check_y <0 or check_y >= N:
                # print(f'filtered {i}: {check_x},{check_y}')
                continue

            elif map[check_x][check_y] == '1' and not visited[check_x][check_y]:
                q.put((check_x,check_y))
                visited[check_x][check_y] = True
                # print(f'insert queue {i} : {check_x},{check_y}')

    return count

for _ in range(N):
    line = list(sys.stdin.readline().rstrip('\n'))
    map.append(line)

answer = []

for i in range(N):
    for j in range(N):
        if map[i][j] == '1' and not visited[i][j]:
            # print('------------------------------------------')
            answer.append(bfs(i,j))

answer.sort()
for i in answer:
    print(i)