import sys

N, M = map(int, sys.stdin.readline().rstrip('\n').split())
d = {}

for i in range(N):
    k,v = sys.stdin.readline().rstrip('\n').split()
    d[k] = v

for i in range(M):
    print(d[sys.stdin.readline().rstrip('\n')])