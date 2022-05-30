import sys
input = sys.stdin.readline

N = input().rstrip('\n')

temp = 0
check_0 = False
answer = []
for i in str(N):
    temp += int(i)
    answer.append(i)
    if i == '0':
        check_0 = True

if temp % 3 == 0 and check_0:
    print(''.join(sorted(answer, reverse=True)))
else:
    print(-1)