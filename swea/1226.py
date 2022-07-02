from collections import deque

coord = [(1,0),(-1,0),(0,1),(0,-1)]
def is_range(x:int, y:int)->bool:
    return 0<=x<16 and 0<=y<16

for test_case in range(1, 11):
    _ = int(input())
    q = deque()
    visited=[[False for _ in range(16)] for __ in range(16)]
    maze = []
    for i in range(16):
        temp = input()
        maze.append(temp)
        for idx, v in enumerate(temp):
            if v == '2':
                q.append((i,idx))
                visited[i][idx] = True

    answer = 0
    while q:
        x,y = q.popleft()

        for dx,dy in coord:
            tx,ty = x+dx, y+dy
            if is_range(tx,ty) and not visited[tx][ty] and maze[tx][ty] != '1':
                if maze[tx][ty] == '3':
                    answer = 1
                    q = deque()
                    break
                visited[tx][ty] = True
                q.append((tx,ty))

    print(f'#{test_case} {answer}')