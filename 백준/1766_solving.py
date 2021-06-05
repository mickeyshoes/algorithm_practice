import sys
import heapq

M,C = map(int, sys.stdin.readline().rstrip('\n').split())

numbers = {(i for i in range(1,M+1))}
diff = set()
conditions = []
heap = []
for _ in range(C):
    i,j = map(int, sys.stdin.readline().rstrip('\n').split())
    conditions.append((i,j))
    diff.add(i)
    diff.add(j)

conditions = sorted(conditions, key= lambda x: x[0])
print(numbers)
numbers = numbers.difference(diff)
count = 1
print(numbers)
print(conditions)
for i in numbers:
    for j in conditions:
        if j[1] < i <j[0]:
            heapq.heappush(heap, (count,j[0]))
            heapq.heappush(heap, (count+1,j[1]))
            count+=1
            break
        else:
            heapq.heappush(heap, (count,i))
            count+=1
            break

print(heap)
print(count)
# for _ in range(len(heap)):
#     print(heapq.heappop()[1], end=' ')