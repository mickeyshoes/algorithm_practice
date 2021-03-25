import sys

N = int(sys.stdin.readline().rstrip('\n'))

N = bin(N)

print(str(N).count('1'))