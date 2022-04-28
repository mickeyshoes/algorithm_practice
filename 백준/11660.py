import sys
input = sys.stdin.readline

N,M = map(int, input().rstrip('\n').split())
ary = [list(map(int, input().rstrip('\n').split())) for _ in range(N)]
coord_set = [list(map(int, input().rstrip('\n').split())) for _ in range(M)]

def array_prefix(ary:list):
    for i in range(1, len(ary)):
        ary[i] = ary[i] + ary[i-1]
    return ary

ary = [array_prefix(i) for i in ary]

for coord in coord_set:
    x1,y1,x2,y2 = [i-1 for i in coord]
    answer = 0
    for x in range(x1,x2+1):
        answer += ary[x][y2]
        if y1 != 0:
            answer -= ary[x][y1-1]
    print(answer)