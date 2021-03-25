import sys

N = int(sys.stdin.readline().rstrip('\n'))

word_list = []

for i in range(N):
    word_list.append(sys.stdin.readline().rstrip('\n'))

answer = 0

for item in word_list:
    for k in range(len(item)):
        if k+2 >= len(item):
            break
        if item[k] != item[k+1] and item[k] in item[k+2:]:
            answer +=1
            break

print(N-answer)