import sys
input = sys.stdin.readline

N = int(input().rstrip('\n'))
S = input().rstrip('\n')

num_C = S.count('C')
print(num_C//(N-num_C+1))