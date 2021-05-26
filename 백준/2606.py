import sys

node = int(sys.stdin.readline().rstrip('\n'))
edge = int(sys.stdin.readline().rstrip('\n'))

node_dict = {}

for i in range(1,node+1):
    node_dict[i] = []

for _ in range(edge):
    n,e = map(int, sys.stdin.readline().rstrip('\n').split())
    node_dict[n].append(e)
    node_dict[e].append(n)

print(node_dict)
visited = [False] * len(node_dict)

def bfs(node_dict : dict, start : int, visited: list):
    print(f'start : {start}')
    visited[start-1] = True
    for i in node_dict[start]:
        if not visited[i-1]:
            bfs(node_dict, i, visited)

bfs(node_dict, 1, visited)
print(sum(visited)-1)