#stack 을 사용해서 구현(방문 노드를 계속 검사하는 식으로)

graph = [
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False] * len(graph)
stack = list()

def dfs(visited : list, number : int, graph : list):
    visited[number-1] = True
    stack.append(number)
    for i in graph[number-1]:
        if visited[i-1] == False:
            dfs(visited, i, graph)

dfs(visited, 1, graph)

print(stack)
print(visited)

from queue import Queue

q = Queue()
visited = [False] * len(graph)

def bfs(visited : list, number : int, graph : list):
    q.put(number)
    visited[number-1] = True

    while q.qsize() > 0:
        next = q.get()
        print(next, end='')
        for i in graph[next-1]:
            if not visited[i-1]:
                q.put(i)
                visited[i-1] = True

bfs(visited, 1, graph)

print()
print(visited)