import sys

a,b = map(int, sys.stdin.readline().rstrip('\n').split())

x = 1

for i in range(1, b+1):
    if a % i == 0 and b % i ==0:
        x = i

print(x)
print(x * (a//x) * (b//x))