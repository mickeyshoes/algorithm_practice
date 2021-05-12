from collections import deque
import sys

N, K = map(int, sys.stdin.readline().rstrip('\n').split())

joseputh = deque()

for i in range(1,N+1):
    joseputh.append(i)

print('<', end='')
for i in range(len(joseputh)):
    if len(joseputh) == 1:
        print(joseputh.popleft(), end='>')
    else:
        joseputh.rotate(-K+1)
        print(joseputh.popleft(), end=', ')