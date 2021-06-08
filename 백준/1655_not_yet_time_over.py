import sys
import heapq
import math

N = int(sys.stdin.readline().rstrip('\n'))

number = []

for i in range(N):
    number.append(int(sys.stdin.readline().rstrip('\n')))
    q = []
    for j in number[:i+1]:
        heapq.heappush(q,j)
    index = math.ceil(len(q)/2)-1
    for k in range(index):
        heapq.heappop(q)
    print(q[0])