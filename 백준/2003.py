import sys
input = sys.stdin.readline

N,M = map(int, input().rstrip('\n').split())
arr = list(map(int, input().rstrip('\n').split()))

answer, end = 0,0

for start in range(N):

    while True:
        if end >= N:
            break
        target = sum(arr[start:end+1])
        if target > M:
            break
        if target == M:
            answer +=1

        end+=1

print(answer)