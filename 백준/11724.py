import sys

N,M = map(int, sys.stdin.readline().rstrip('\n').split())

node_dict = dict()

for i in range(1,N+1):
    node_dict[i] = []

for _ in range(M):
    n,e = map(int, sys.stdin.readline().rstrip('\n').split())
    node_dict[n].append(e)
    node_dict[e].append(n)

visited = [False] * N

def dfs(visited:list, node_dict:dict, start:int):
    stack = [start]
    visited[start-1] = True
    count = 0

    while len(stack) > 0:
        n = stack.pop()
        for i in node_dict[n]:
            if not visited[i-1]:
                stack.append(i)
                visited[i-1] = True
                count+=1
    
    return count

answer = []
for i in range(1,N+1):
    temp = dfs(visited,node_dict,i)
    if temp > 0:
        answer.append(1+temp)

print(N - sum(answer) + len(answer))