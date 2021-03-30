import sys
from itertools import combinations

N,M = map(int, sys.stdin.readline().rstrip('\n').split())

input_number = list(map(int, sys.stdin.readline().rstrip('\n').split()))

combination_list = [sum(i) for i in combinations(input_number,3) if sum(i) <= M]

print(max(combination_list))