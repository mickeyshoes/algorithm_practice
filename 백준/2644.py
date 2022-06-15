import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
t_a, t_b = map(int, input().split())
d= defaultdict(list)
for _ in range(int(input())):
    p,c = map(int, input().split())
    d[p].append(c)
    d[c].append(p)

visited = [False] * (N+1)
answer = -1
def DFS(people:int, depth:int):
    global answer

    if people == t_b:
        answer = depth
        return

    for i in d[people]:
        if not visited[i]:
            visited[i]=True
            DFS(i,depth+1)

DFS(t_a,0)
print(answer)