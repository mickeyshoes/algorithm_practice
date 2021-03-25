import sys

n,x= map(int, sys.stdin.readline().split())

a = sys.stdin.readline().rstrip('\n')
a = list(map(int, a.split()))

for i in range(n):
    if x > a[i]:
        print(a[i], end=' ')