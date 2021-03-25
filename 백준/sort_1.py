import sys

n = int(sys.stdin.readline().rstrip('\n'))

input_number_list = []

for i in range(n):
    input_number_list.append(int(sys.stdin.readline().rstrip('\n')))

input_number_list.sort()
    
print(input_number_list)