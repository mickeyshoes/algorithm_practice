import sys

sort_dict = {}
to_be_sort = []

for i in range(1,51):
    sort_dict[i] = []

N = int(sys.stdin.readline().rstrip('\n'))

for i in range(N):
    to_be_sort.append(sys.stdin.readline().rstrip('\n'))

to_be_sort.sort()

for l in range(1,len(sort_dict)+1):
    for item in to_be_sort:
        if len(item) == l:
            if item in sort_dict[l]:
                continue
            sort_dict[l].append(item)

for i in sort_dict:
    for k in range(len(sort_dict[i])):
        print(sort_dict[i][k])
