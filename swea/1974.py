T = int(input())

def is_one_to_nine(ary:list)->bool:
    return len(set(ary)) == 9

def sliding_window(x:int, y:int, kernel_size:int, sudoku:list)->list:
    result = []
    for i in range(kernel_size):
        for j in range(kernel_size):
            result.append(sudoku[x+i][y+j])
    return result

def check_is_available(sudoku:list)->int:
    #row
    for i in sudoku:
        if not is_one_to_nine(i):
            return 0
    #col
    for i in zip(*sudoku):
        if not is_one_to_nine(list(i)):
            return 0
    #matrix
    for i in range(3):
        x_idx = i*3
        for j in range(3):
            y_idx = i*3
            filtered = sliding_window(x_idx,y_idx, 3, sudoku)
            if not is_one_to_nine(filtered):
                return 0
    return 1

for test_case in range(1, T + 1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    print(f'#{test_case} {check_is_available(sudoku)}')