import sys

N = int(sys.stdin.readline().rstrip('\n'))

number_list = list(map(int, sys.stdin.readline().rstrip('\n').split()))[:N]

for i in number_list:
    for j in range(2,i+1):
        if i % j == 0 and i != j:
            print(f'i : {i} j : {j} i % j : {i%j}')
            number_list.pop(number_list.index(i))
            break

print(f'answer : {number_list}\t{len(number_list)}')