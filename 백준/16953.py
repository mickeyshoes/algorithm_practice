import sys

N,M = map(int, sys.stdin.readline().rstrip('\n').split())

def solution(N,M):
    count = 1
    while M>N:
        if str(M)[-1] == '1':
            M = int(str(M)[:-1])
        elif M % 2 == 0:
            M = M//2
        else:
            print(-1)
            return
        count +=1

    if M != N:
        count = -1
    print(count)

solution(N,M)