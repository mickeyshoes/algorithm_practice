import sys
from functools import reduce

N = int(sys.stdin.readline().rstrip('\n'))

input_list = sorted(list(map(int, sys.stdin.readline().rstrip('\n').split())))
count = 0
for i in range(1,len(input_list)+1):
    count += reduce(lambda x,y :x+y, input_list[:i])
print(count)

count = 0
for i in range(len(input_list)):
    count += input_list[i] * (N-i)
print(count)