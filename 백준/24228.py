import sys
input = sys.stdin.readline

a,b = map(int, input().rstrip('\n').split())

print(a-1+(2*b))