def solution(board, moves):
    answer = 0
    stack = []
    for col in moves:
        col -=1
        for row in range(len(board)):
            if board[row][col] != 0:
                if stack and stack[-1] == board[row][col]:
                    stack.pop()
                    answer +=1
                else:
                    stack.append(board[row][col])
                board[row][col] = 0
                break
    print(stack)
    return answer