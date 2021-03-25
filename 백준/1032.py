import sys

n = int(sys.stdin.readline().rstrip('\n'))

input_list = []

for i in range(n):
    input_list.append(sys.stdin.readline().rstrip('\n'))

answer = list(input_list[0])

for j in range(1, len(input_list)):

    for k in range(len(answer)):
        if answer[k] == input_list[j][k]:
            continue
        else:
            answer[k] = '?'

print(''.join(answer))