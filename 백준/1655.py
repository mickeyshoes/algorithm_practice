import sys
import heapq

N = int(sys.stdin.readline().rstrip('\n'))

#max_q
max_q = []
min_q = []

for i in range(N):
    a = int(sys.stdin.readline().rstrip('\n'))

    if len(max_q) == len(min_q):
        heapq.heappush(max_q,-a)
    else:
        heapq.heappush(min_q,a)
    
    try:
        if -max_q[0] > min_q[0]:
            heapq.heappush(min_q, -heapq.heappop(max_q)) #+
            heapq.heappush(max_q, -heapq.heappop(min_q)) #-
        print(-max_q[0]) 
    
    except IndexError:
        print(a)
        continue