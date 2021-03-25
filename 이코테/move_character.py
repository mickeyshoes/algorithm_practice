import sys

width, height = map(int, sys.stdin.readline().rstrip('\n').split())

init_state = list(map(int, sys.stdin.readline().rstrip('\n').split()))

map_space = [] # 맵을 담을 공간
map_log = [] # 맵의 어디를 다녀왔는지 기록할 공간

for i in range(height):
    input_map = list(map(int, sys.stdin.readline().rstrip('\n').split()))
    map_space.append(input_map[:width]) # map 이상의 원소를 입력하는 경우 방지

d = [0,1,2,3]

# 방향을 바꾸는 함수
def change_d(d_list, d_num):
    d_num += 1

    if d_num not in d_list:
        d_num = 0
    return d_num

# 현재 있는 장소 로그에 담음
map_log.append(init_state[:2])
# 동서남북 다 둘러 보았을 경우를 확인하기 위한 변수
pre_count = 0

while True:
    # 사방을 둘러봐도 갈 곳이 없으면 break
    if pre_count == 4:
        break

    else:
        # 방향 전환
        init_state[2] = change_d(d, init_state[2])
        move = []

        if init_state[2] == 0: # 북
            move = [-1, 0]
        elif init_state[2] == 1: # 동
            move = [0, 1]
        elif init_state[2] == 2: # 남
            move = [1, 0]
        elif init_state[2] == 3: # 서
            move = [0, -1]

        # 현재 위치에서 선택된 방향으로 미리 가봄
        pre = [x+y for x,y in zip(init_state[:2], move)]
        print(f'state : {init_state[:2]} d : {init_state[2]} pre : {pre} ')

        # 맵의 index 를 벗어난 경우 방향 돌리기부터 재시작
        if pre[0] < 0 or pre[1] <0 or pre[0] >= width or pre[1] >= height:
            pre_count +=1
            continue

        else:
            # 미리 가본 방향이 로그에 없고 이동이 가능한 지역 이라면 추가
            if pre not in map_log and map_space[pre[0]][pre[1]] == 0:
                map_log.append(pre)
                init_state[:2] = pre
                pre_count = 0

            else:
                pre_count += 1

print(f'len : {len(map_log)} log : {map_log}')