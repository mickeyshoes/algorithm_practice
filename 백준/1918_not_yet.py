import sys

infix = sys.stdin.readline().rstrip('\n')
infix = '(' + infix + ')'
a = 0
stack = []
answer = ''
temp = ''


def preprocessing_bracket(expression : str):

    if len(expression) < 4:
        return expression

    op = [['*','/'], ['+','-']]
    new_expression = ''
        '''
        1. * 랑 / 연산자 먼저 괄호 씌워준다.
        2. + - 연산자 괄호 씌워준다.
        3. 리턴
        '''
    return new_expression

def make_postfix(infix: str):
    postfix = ''
    '''
    infix to postfix
    b * c => bc*
    '''
    return postfix

for i in range(len(infix)):
    if infix[i] == ')':
        for j in range(len(stack)):
            b = stack.pop()
            if b != '(':
                temp += b
            else:
                break
    stack.append(infix[i])
    print(f'{i} temp : {temp} \ta : {a}')

print(answer)