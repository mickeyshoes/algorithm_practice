import sys
input = sys.stdin.readline

N,M = map(int, input().rstrip('\n').split())
ary = list(map(int, input().rstrip('\n').split()))
for i in range(1, N):
    ary[i] = ary[i] + ary[i-1]
answer = []
for _ in range(M):
    i,j = map(int, input().rstrip('\n').split())
    temp = 0
    if i -2 <= 0:
        i = 0
        temp += ary[i]
    else:
        i -=2
    answer.append(ary[j-1]-ary[i]+temp)

for i in answer:
    print(i) 