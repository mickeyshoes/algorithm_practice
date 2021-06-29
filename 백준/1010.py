import sys
input = sys.stdin.readline

N = int(input().rstrip('\n'))

for _ in range(N):
    a,b = map(int, input().rstrip('\n').split())
    answer = [1,1,1]

    for i in range(1,b+1):
        answer[0] *= i
    for i in range(1,a+1):
        answer[1] *= i
    for i in range(1,b-a+1):
        answer[2] *= i

    print(answer[0]//(answer[1]*answer[2]))