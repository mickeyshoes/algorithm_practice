import sys

first, last = map(int, sys.stdin.readline().rstrip('\n').split())

answer_list = []

for i in range(1,1000):
    for k in range(i):
        answer_list.append(i)

result = 0

for item in range(first-1,last):
    result += answer_list[item]

print(result)