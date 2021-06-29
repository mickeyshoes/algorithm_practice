import sys
from collections import Counter
input = sys.stdin.readline

N = int(input().rstrip('\n'))
W = input().rstrip('\n')
print(Counter(W.replace('pPAp','1'))['1'])
print(W.count('pPAp'))