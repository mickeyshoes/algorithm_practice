import sys

N = int(sys.stdin.readline().rstrip('\n'))

input_list = list(map(int, sys.stdin.readline().rstrip('\n').split()))

key_list = sorted(set(input_list))

zip_dict = dict()

for i in range(len(key_list)):
    zip_dict[key_list[i]] = i

for i in input_list:
    print(zip_dict[i], end=' ')