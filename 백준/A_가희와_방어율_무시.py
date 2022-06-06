import sys
input = sys.stdin.readline

a,b = map(int, input().split())
answer = a - (a*b/100)
print(0) if answer > 99 else print(1)