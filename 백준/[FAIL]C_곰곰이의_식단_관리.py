import sys
import math
input = sys.stdin.readline

N = int(input().rstrip('\n'))
S = input().rstrip('\n')

num_C = S.count('C')
print(math.ceil(num_C//(N-num_C+1)))