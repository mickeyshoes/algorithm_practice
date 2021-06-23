import sys

input = sys.stdin.readline

N, target = map(int, input().rstrip('\n').split())

coin = [int(input().rstrip('\n')) for _ in range(N)]

count = 0 
for i in coin[::-1]:
    a,b = divmod(target,i)
    if a != 0:
        count+=a
        target = b

print(count)