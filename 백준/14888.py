import sys
from functools import reduce
input = sys.stdin.readline

N = int(input().rstrip('\n'))
items = list(map(int, input().rstrip('\n').split()))
ops = list(map(int, input().rstrip('\n').split()))
ops = ['+']*ops[0] + ['-']*ops[1] + ['*']*ops[2] + ['/']*ops[3]
stack =[]
visited = [False] * (N-1)
#max, min
answer = [0,reduce(lambda x,y : x*y, items)*2]
def DFS()->None:

    if len(stack) == (N-1):
        result = operation_result(''.join(stack))
        answer[0] = max(answer[0], result)
        answer[1] = min(answer[1], result)
        return

    for i in range(len(ops)):
        if not visited[i]:
            stack.append(ops[i])
            visited[i] = True
            DFS()
            stack.pop()
            visited[i] = False

def operation_result(ops:str)->int:
    result = calculate_ops(items[0], items[1], ops[0])
    for i in range(1, len(ops)):
        result = calculate_ops(result, items[i+1],ops[i])
    return result

def calculate_ops(num1:int, num2:int, ops:str)->int:
    result = 0
    if ops == '+':
        result = num1 + num2
    elif ops == '-':
        result = num1 - num2
    elif ops == '*':
        result = num1 * num2
    elif ops == '/':
        if num1 < 0:
            result = (-1 * num1) // num2
            result = result * (-1)
        else:
            result = num1 // num2
    else:
        print('error')
        print(num1, num2, ops)
    return result

print(ops)
DFS()
for i in range(len(answer)):
    print(answer[i])