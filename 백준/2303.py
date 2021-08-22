from itertools import combinations
import sys

N = int(sys.stdin.readline().rstrip('\n'))
answer = []

for i in range(N):
    input_list = list(map(int, sys.stdin.readline().rstrip('\n').split()))
    a = max([sum(i)%10 for i in combinations(input_list, 3)])
    answer.append(a)

a = max(answer)
for i in range(len(answer)-1,-1,-1):
    if answer[i] == a:
        print(i+1)
        break