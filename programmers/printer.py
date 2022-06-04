from collections import deque
import heapq
def solution(priorities, location):
    answer = 0
    heap = []
    q= deque([])
    for i in range(len(priorities)):
        heapq.heappush(heap, -priorities[i])
        q.append((i, priorities[i]))
    m = -heapq.heappop(heap)
    while q:
        i, v = q.popleft()
        if v != m:
            q.append((i,v))
        elif i == location and v == m:
            answer+=1
            break
        else:
            m = -heapq.heappop(heap)
            answer +=1
            
    return answer