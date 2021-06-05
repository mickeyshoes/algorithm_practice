import sys
import heapq

sys_in = sys.stdin.readline()
N = int(sys_in.rstrip('\n'))
heap = []

for _ in range(N):
    number = int(sys.stdin.readline().rstrip('\n'))

    if number == 0:
        try:
            print(heapq.heappop(heap))
        except IndexError:
            print(0)
    else:
        heapq.heappush(heap, number)