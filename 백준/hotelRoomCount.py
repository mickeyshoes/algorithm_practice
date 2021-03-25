import sys
import math

T = int(sys.stdin.readline().rstrip("\n"))

for i in range(T):
    h,w,n = map(int, sys.stdin.readline().rstrip('\n').split())

    number, floor= divmod(n,h)
    
    if floor == 0:
        floor = h
    
    print(f'{floor*100+math.ceil(n/h)}')