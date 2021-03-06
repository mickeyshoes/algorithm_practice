import sys
input = sys.stdin.readline

N = int(input().rstrip('\n'))
ary1 = list(map(int, input().rstrip('\n').split()))
ary1.sort()
M = int(input().rstrip('\n'))
ary2 = list(map(int, input().rstrip('\n').split()))
answer = []

for i in ary2:
    start = 0
    end = N -1

    while start <= end:
        div = (start+end)//2
        if i > ary1[div]:
            start = div+1
        elif i < ary1[div]:
            end = div-1
        else:
            answer.append(1)
            break
    if start > end:
        answer.append(0)

print(' '.join([str(i) for i in answer]))