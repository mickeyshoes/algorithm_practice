import sys

input = sys.stdin.readline
N = int(input().rstrip('\n'))

def solution():
    a,b,ta,tb = map(int, input().rstrip('\n').split())
    x,y = 0,0
    count = 0
    while x+y != a+b:
        count +=1        
        if x == a:
            x = 1
        else:
            x +=1
        if y == b:
            y = 1
        else:
            y +=1
        
        if x == ta and y == tb:
            print(count)
            return
    print(-1)

for _ in range(N):
    solution()