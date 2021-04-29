import sys

N = int(sys.stdin.readline().rstrip('\n'))

input_list = [list(map(int, sys.stdin.readline().rstrip('\n').split())) for _ in range(N)]

input_list = sorted(input_list, key=lambda a: min(a[1]))