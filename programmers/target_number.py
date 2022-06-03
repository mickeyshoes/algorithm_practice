from collections import deque

def solution(numbers, target):
    q= deque([])
    q.append(numbers[0])
    q.append(-numbers[0])
    
    for i in numbers[1:]:
        temp  = []
        while q:
            a = q.popleft()
            temp.append(a+i)
            temp.append(a-i)
        for t in temp:
            q.append(t)
            
    return list(q).count(target)