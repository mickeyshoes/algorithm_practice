import sys
import math

fac = math.factorial
N,M = map(int, sys.stdin.readline().rstrip('\n').split())
print(fac(N)//(fac(M) * fac(N-M)))