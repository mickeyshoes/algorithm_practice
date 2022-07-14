import sys
input = sys.stdin.readline
W,H = map(int, input().split())

building_map = [list(map(int, input().split())) for _ in range(H)]

def is_range(x:int, y:int)->bool:
    return 0<=x<H and 0<=y<W

def move(x:int, y:int, d:int)->tuple:
    is_even = y%2 == 0
    tx,ty = 0,0
    if d == 0:
        ty = -1
        if is_even:
            tx = -1

    if d == 1:
        ty = -1
        if not is_even:
            tx = 1

    if d == 2:
        tx = 1
    
    if d == 3:
        ty = 1
        if not is_even:
            tx = 1

    if d == 4:
        ty = 1
        if is_even:
            tx = -1
    
    if d == 5:
        tx = -1

    return (tx,ty)

answer = 0
for i in range(H):
    for j in range(W):
        if building_map[i][j] == 1:
            cnt = 0
            for k in range(6):
                tx,ty = move(i,j,k)
                if is_range(tx,ty) and building_map[tx][ty] ==0:
                    cnt +=1
                    #맵의 상하좌우 체크해서 값  더하기해야함
                if not is_range(tx,ty):
                    cnt +=1
            answer += cnt

print(answer)