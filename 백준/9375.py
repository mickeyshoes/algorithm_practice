import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input().rstrip('\n'))

for _ in range(N):
    M = int(input().rstrip('\n'))
    d = defaultdict(int)
    answer = 1
    for _ in range(M):
        item, category = input().rstrip('\n').split()
        d[category] +=1
    for i in d.values():
        answer *= (i+1)
    print(answer-1)