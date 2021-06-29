import sys

N = int(sys.stdin.readline().rstrip('\n'))

input_list = []

for _ in range(N):
    k,v = map(int, sys.stdin.readline().rstrip('\n').split())
    input_list.append([k,v])

input_list = sorted(input_list, key= lambda item:(item[1], item[0]))
print(input_list)
answer = [input_list[0]]

for i in range(1, len(input_list)):
    if answer[-1][1] <= input_list[i][0]:
        answer.append(input_list[i])
        continue

print(len(answer))