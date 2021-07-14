import sys

N,M = map(int, sys.stdin.readline().rstrip('\n').split())

chess_board = []
answer = {}

def add_count(line, color, th):
    result = 0
    # 흑,백이 연달아서 나오면 안되므로 뒤집음
    if th % 2 == 1:
        color = color[::-1]
    # 같은지 비교
    for i in range(8):
        if line[i] != color[i]:
            result += 1
    return result

def calculate_count(matrix):
    start_white = 0
    start_black = 0

    for i in range(8):
        start_black += add_count(matrix[i], 'BWBWBWBW', i)
        start_white += add_count(matrix[i],'WBWBWBWB', i)

    return min(start_black, start_white)

for i in range(N):
    chess_board.append(sys.stdin.readline().rstrip('\n'))

for column in range(N):
    if column+8 >N:
        break
    for row in range(M):
        if row+8 >M:
            break
        else:
            split_matrix = [chess_board[i+column][row:row+8] for i in range(8)]
            answer[f'{column},{row}'] = calculate_count(split_matrix)

print(f'{min(answer.values())}')