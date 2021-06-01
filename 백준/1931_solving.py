import sys
from collections import defaultdict

N = int(sys.stdin.readline().rstrip('\n'))

input_list = []

for _ in range(N):
    k,v = map(int, sys.stdin.readline().rstrip('\n').split())
    input_list.append([k,v,v-k+1])

input_list = sorted(input_list, key= lambda item:item[1])
print(input_list)

# answer = []
# visited = [False] * 31

# for i in input_list:
#     count = 0
#     for j in range(i[0], i[1]+1):
#         if not visited[j-1]:
#             count +=1

#     print(f'i : {i} count : {count}')

#     if count == i[2]:
#         for j in range(i[0], i[1]+1):
#             visited[j-1] = True
#         answer.append(i)

# print(answer)