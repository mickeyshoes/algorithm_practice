import sys

T = int(sys.stdin.readline().rstrip('\n'))
for _ in range(T):
    N = int(sys.stdin.readline().rstrip('\n'))
    answer = [(1,0),(0,1)]
    for i in range(2,N+1):
        answer.append(
            (answer[i-1][0] + answer[i-2][0], answer[i-1][1] + answer[i-2][1]) 
        )
    print(f'{answer[N][0]} {answer[N][1]}')