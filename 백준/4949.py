import sys
input = sys.stdin.readline

while True:
    temp = input().rstrip('\n')
    if temp == '.':
        break
    stack = []
    for i in temp:
        if i in ['(', '[']:
            stack.append(i)
        elif i in [')', ']']:
            if stack and ((i == ')' and stack[-1] == '(') or (i == ']' and stack[-1]=='[')):
                stack.pop()
            else:
                stack.append(i)

    print('no') if stack else print('yes')