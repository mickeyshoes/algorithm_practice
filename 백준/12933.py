import sys
input = sys.stdin.readline

S = input().rstrip('\n')

stack = []
###quack을 찾아야 한다.
for c in S:
    if c == 'q':
        stack.append(c)
    else:
        for i in stack:
            # 스택에서 하나하나 꺼내서 문장을 완성시켜보자
            pass