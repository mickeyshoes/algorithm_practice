from collections import defaultdict
from collections import deque
for test_case in range(1, 11):
    answer = [0, 0]
    N, start = map(int, input().split())
    emergency_tel_book = list(map(int, input().split()))
    phone_book = defaultdict(set)
    visited = [False for _ in range(101)]
    q = deque()
    q.append((start, 0))
    visited[start] = True
    for i in range(0,N,2):
        phone_book[emergency_tel_book[i]].add(emergency_tel_book[i+1])

    while q:
        target, depth = q.popleft()

        for i in phone_book[target]:
            if not visited[i]:
                visited[i] = True
                q.append((i, depth+1))

        if depth>answer[1]:
            answer = [target, depth]
        elif depth == answer[1]:
            answer[0] = max(answer[0], target)
    
    print(f'#{test_case} {answer[0]}')