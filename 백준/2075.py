import sys
import heapq

input = sys.stdin.readline

N = int(input())
q = []
for j in range(N):
    a = input().rstrip('\n')
    for i in list(map(int, a.split()))[:N]:
        if not q:
            heapq.heappush(q,i)
        if i > q[0]:
            if len(q) >=N:
                heapq.heappop(q)
            heapq.heappush(q,i)

print(q[0])