import sys
from queue import Queue

node, edge, vertex = map(int, sys.stdin.readline().rstrip('\n').split())

adj_dict = dict()


for i in range(1,node+1):
    adj_dict[i] = []

for i in range(edge):
    n,r = map(int, sys.stdin.readline().rstrip('\n').split())
    adj_dict[n].append(r)
    adj_dict[r].append(n)


visited = [False] * len(adj_dict)

# depth
def dfs(adj_dict: dict, start : int, visited : list):
    visited[start-1] = True
    print(start, end=' ')
    adj_dict[start].sort()
    for i in adj_dict[start]:
        if not visited[i-1]:
            dfs(adj_dict, i, visited)
            
# breadth
def bfs(adj_dict : dict, start : int, visited : list):
    q = Queue()
    q.put(start)
    visited[start-1] = True
    
    while q.qsize() >0:
        v = q.get()
        print(v, end=' ')
        adj_dict[v].sort()
        for i in adj_dict[v]:
            if not visited[i-1]:
                q.put(i)
                visited[i-1] = True

dfs(adj_dict, vertex, visited)
# print(adj_dict)
# print(visited)
visited = [False] * len(adj_dict)
print()
bfs(adj_dict, vertex, visited)
# print(adj_dict)
# print(visited)