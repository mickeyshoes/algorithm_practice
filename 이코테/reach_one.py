import sys

n ,k = map(int, sys.stdin.readline().rstrip('\n').split())

count = 0 

while True:

    if n == 1:
        break

    elif n%k == 0:
        n = n//k
    else:
        n = n -1

    count +=1

print(count)