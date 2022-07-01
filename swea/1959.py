T = int(input())

def sliding_window(A:list, B:list)->int:
    answer = -1
    for i in range(len(A)-len(B)+1):
        temp = 0
        for idx, item in enumerate(B):
            temp += item * A[i+idx]
        answer = max(answer, temp)
    return answer

for test_case in range(1, T + 1):
    N,M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    if N>M:
        answer = sliding_window(A,B)
    else:
        answer = sliding_window(B,A)
    print(f'#{test_case} {answer}')