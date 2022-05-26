def solution(scoville, K):
    import heapq
    count = 0
    heap = []
    is_possible = False
    for i in scoville:
        heapq.heappush(heap, i)
        
    while heap:
        try:
            a = heapq.heappop(heap)
            if a >= K:
                is_possible = True
                break
            else:
                b = heapq.heappop(heap)
                heapq.heappush(heap, a+2*b)
                count +=1
        except IndexError:
            break

    if is_possible:
        return count
    
    return int(-1)