T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.

def rotate_array(array:list)->list:
    lim = len(array)
    result = [list() for _ in range(lim)]
    #col
    for i in range(lim):
        #row
        for j in range(lim-1,-1,-1):
            result[i].append(array[j][i])
    return result

for test_case in range(1, T + 1):
    N = int(input())
    answer = [list() for _ in range(N)]
    array = [input().split() for _ in range(N)]
    for _ in range(3):
        array = rotate_array(array)
        for i in range(N):
            answer[i].append(''.join(array[i]))
    print(f'#{test_case}')
    for i in answer:
        print(*i)