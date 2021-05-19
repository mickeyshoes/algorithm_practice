import sys

N = int(sys.stdin.readline().rstrip('\n'))

insert_list = [sys.stdin.readline().rstrip('\n') for _ in range(N)]

for item in insert_list:
    stack = []
    stack.append(item[0])
    for i in range(1, len(item)):
        try:
            if stack[len(stack) -1] == '(' and item[i] == ')':
                stack.pop()
                # print(f'{i} : {stack}')
                continue
            else:
                stack.append(item[i])
                # print(f'{i} : {stack}')
        except IndexError:
            stack.append(item[i])
            # print(f'{i} : {stack}')
    print(len(stack), end=' ')
    print(stack, end=' ')
    if len(stack) > 0:
        print('NO')
    else:
        print('YES')