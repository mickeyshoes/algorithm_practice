import sys
import re

input = sys.stdin.readline
N = int(input().rstrip('\n'))
p = re.compile('(100+1+|01)+')

for _ in range(N):
    string = input().rstrip('\n')
    if p.fullmatch(string):
        print('YES')
    else:
        print('NO')