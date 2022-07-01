T = int(input())

def get_fly_count(x:int, y:int, filter_size:int, fly_map:list)->int:
    result = 0
    for i in range(filter_size):
        for j in range(filter_size):
            result += fly_map[x+i][y+j]
    return result

for test_case in range(1, T + 1):
    N,M = map(int, input().split())
    fly_map = [list(map(int, input().split())) for _ in range(N)]
    answer = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            answer = max(answer, get_fly_count(i, j, M, fly_map))
    print(f'#{test_case} {answer}')