import sys
input = sys.stdin.readline

h,m = map(int, input().split(':'))
time_list = list(map(int, input().split()))
L = int(input())


def change_time(h:int, m:int)->tuple:
    if m >=60:
        m = m - 60
        h +=1
    if h > 12:
        h = h - 12
    return (h,m)

for _ in range(L):
    time, cmd = input().split()
    if int(time.split('.')[0]) >= 60:
        # 커맨드 시간이 60초 이상 넘어갔다면 종료
        break
    if 'MIN'in cmd:
        #분 추가
        m += int(cmd[:2])
        h, m = change_time(h,m)
    elif 'HOUR' in cmd:
        # 시간 추가
        h += int(cmd[:1])
        h,m = change_time(h,m)
    else:
        #현재 구역 봉인
        cur = h // 2
        if cur == 6:
            cur = 0
        time_list[cur] = 0

print(sum(time_list)) if sum(time_list)<100 else print(100)