import sys

lenth = int(input())

for i in range(lenth):
    a,b = map(int, sys.stdin.readline().split())
    print(f'Case #{i+1}: {a+b}')