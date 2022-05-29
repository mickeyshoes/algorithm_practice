import sys
from itertools import permutations
input = sys.stdin.readline

N = input().rstrip('\n')
temp = -1
for p in permutations(N,len(N)):
    target = ''.join(p)

    if int(target) % 30 ==0:
        temp = max(temp, int(target))

print(temp)