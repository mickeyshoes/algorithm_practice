import sys
import math

a,b,c = map(int, sys.stdin.readline().rstrip('\n').split())

if b >= c:
    print(-1)
else:
    print(math.floor(a/(c-b)) +1)