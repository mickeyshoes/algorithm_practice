import sys

N = int(sys.stdin.readline().rstrip('\n'))

num_list_a = list(map(int, sys.stdin.readline().rstrip('\n').split()))

M = int(sys.stdin.readline().rstrip('\n'))

num_list_b = list(map(int, sys.stdin.readline().rstrip('\n').split()))

for i in num_list_b:
    if i in num_list_a:
        print(1)
    else:
        print(0)