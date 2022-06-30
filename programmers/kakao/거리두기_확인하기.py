def is_range(x:int, y:int)->bool:
    return 0<=x<5 and 0<=y<5
    
def check_is_safe(waitting_room:list)->int:
    #p와0인 경우의 거리 확인
    coord = [(1,0),(-1,0),(0,1),(0,-1)]
    for x in range(5):
        for y in range(5):
            if waitting_room[x][y] != 'X':
                check = 0
                for dx,dy in coord:
                    tx,ty = x+dx, y+dy
                    if is_range(tx,ty) and waitting_room[tx][ty] =='P':
                        check +=1
                if (waitting_room[x][y] == 'P' and check >0) or (waitting_room[x][y] =='O' and check>1):
                    return 0
    return 1
                
def solution(places):
    answer = []
    for p in places:
        answer.append(check_is_safe(p))
    return answer