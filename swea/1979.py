T = int(input())
for test_case in range(1, T + 1):
    N,K = map(int, input().split())
    puzzle_map = [input().split() for _ in range(N)]
    answer = 0
    #row
    for i in puzzle_map:
        row = ''.join(i).replace('0', ' ').split()
        for j in row:
            if len(j) == K:
                answer+=1
    #col
    for i in zip(*puzzle_map):
        col = ''.join(i).replace('0', ' ').split()
        for j in col:
            if len(j) == K:
                answer +=1
    print(f'#{test_case} {answer}')