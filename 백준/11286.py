import sys
import heapq

N = int(sys.stdin.readline().rstrip('\n'))

heap = []

for _ in range(N):

    number = int(sys.stdin.readline().rstrip('\n'))

    if number == 0:
        try:
            k,v = heapq.heappop(heap)
            print(v)
        except IndexError:
            print(0)
    else:
        sign = 1
        if number <0:
            sign *=-1
        
        heapq.heappush(heap, (sign*number, number))