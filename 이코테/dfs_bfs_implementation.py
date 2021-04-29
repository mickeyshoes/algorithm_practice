def dfs(graph : list, visit : int, log : list) -> None:
    log[visit] = True
    for node in graph[visit]:
        if not visited[node]:
            print(node, end=' ')
            dfs(graph, node, log)

from collections import deque

def bfs(graph : list, start : int, log: list) ->None:
    queue = deque([start])
    log[start] = True
    
    while queue:
        node = queue.popleft()
        print(node, end=' ')

        for i in graph[node]:
            if not log[i]:
                queue.append(i)
                log[i] = True

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False] * 9
dfs(graph, 1, visited)
print()
visited = [False] * 9
bfs(graph, 1, visited)