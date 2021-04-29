import sys

N, K = map(int, sys.stdin.readline().rstrip('\n').split())

input_list =[i for i in range(1,N+1)]

while True:

    if len(input_list) == 0:
        break

    else:
        