import sys
input = sys.stdin.readline

N,M = map(int, input().rstrip('\n').split())
ary = list(map(int, input().rstrip('\n').split()))
for i in range(1, N):
    ary[i] = ary[i] + ary[i-1]
answer = []
for _ in range(M):
    i,j = map(int, input().rstrip('\n').split())
    i-=1
    temp = ary[j-1]
    if i !=0:
        temp -= ary[i-1]
    answer.append(temp)

for i in answer:
    print(i) 