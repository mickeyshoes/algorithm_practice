import sys
import heapq

input = sys.stdin.readline

for i in range(int(input())):
    M = int(input())
    numbers = []
    for _ in range(M//10+1):
        numbers.extend(list(map(int, input().rstrip('\n').split())))
    #priority q 
    max_q = []
    min_q = []
    answer = []

    for i in numbers:
        if len(max_q) == len(min_q):
            heapq.heappush(max_q, -i)
        else:
            heapq.heappush(min_q, i)

        try:
            if -max_q[0] > min_q[0]:
                heapq.heappush(min_q, -heapq.heappop(max_q))
                heapq.heappush(max_q, -heapq.heappop(min_q))

            if (len(max_q) + len(min_q)) % 2 == 1:
                answer.append(-max_q[0])

        except IndexError:
            answer.append(i)
            continue
    
    print(len(answer), end='')
    for i in range(len(answer)):
        if i % 10 == 0:
            print()
        print(answer[i], end=' ')