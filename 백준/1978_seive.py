import sys

N = int(sys.stdin.readline().rstrip('\n'))

number_list = list(map(int, sys.stdin.readline().rstrip('\n').split()))[:N]

max_number = max(number_list)

prime_list =  [False] *2 +[True] * (max_number-1)

cycle_range = int(max_number ** 0.5)

for i in range(2, cycle_range+1):
    if prime_list[i]:
        for j in range(i+i, max_number+1, i):
            prime_list[j] = False
            print(f'prime_list[{j}] : {prime_list[j]}')

max_number = 0

for i in number_list:
    print(f'i : {i} prime_list : {prime_list}')
    if prime_list[i]:
        max_number +=1

print(max_number)
