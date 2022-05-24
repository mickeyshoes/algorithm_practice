import sys
from collections import deque
input = sys.stdin.readline

N = int(input().rstrip('\n'))
ary = list(map(int, input().rstrip('\n').split()))
A,B = map(int, input().rstrip('\n').split())

visited = [False] * N

def BFS(start:int, end:int):
    q= deque([(0,start)])

    while q:
        depth, node = q.popleft()
        visited[node] = True
        
        for i in range(N):
            if not visited[i] and abs(node-i) % ary[node] == 0:
                q.append((depth+1, i))
                if i == end:
                    return depth+1


answer = BFS(A-1, B-1)
print(answer) if answer else print(-1)