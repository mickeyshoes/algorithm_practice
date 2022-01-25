import sys
from collections import deque
from time import sleep

input = sys.stdin.readline

N = int(input().rstrip())
bridge = list(map(int, input().rstrip().split()))
a,b = map(int, input().rstrip().split())

q = deque()
length = len(bridge)
q.append((a,0))

# def jump(q):
#     answer_list = []
#     while q:
#         current_state, depth = q.popleft()
#         print(f'init : {depth}, value : {current_state}')
#         if current_state <= length:
#             for i in range(1,length,1):
#                 node = current_state
#                 try:
#                     if current_state > b:
#                         node -= bridge[current_state-1]*i
#                     else:
#                         node += bridge[current_state-1]*i
#                     if node == b:
#                         # 다른 경우도 생각하기 위해서 break 는 안함
#                         print(f'hit! {depth+1} : {current_state}')
#                         answer_list.append(depth+1)
#                     elif 0< node <= length:
#                         q.append((node,depth+1))
#                         print(f'start:{depth+1} append {node}')
#                 except IndexError as e:
#                     continue
#             sleep(5)
#     print(answer_list)
#     return min(answer_list) if answer_list else -1

# print(0 if a == b else jump(q))

visited = [False] * length

def jump(start, end):
    stack = []
    answer = []
    stack.append((start,0))

    while stack:
        parent_node, depth = stack.pop()
        # print(f'{parent_node} : {depth}')
        i = 1

        while bridge[parent_node-1] * i < length:
            node = parent_node
            
            #좌,우를 다 확인하는 케이스를 넣어야 함
            if node > end:
                node -= bridge[parent_node-1] * i
            else:
                node += bridge[parent_node-1] * i


            if node == end:
                answer.append(depth+1)
            elif 0< node <= length and not visited[node-1]:
                visited[node-1] = True
                stack.append((node,depth+1))
            i+=1
        print(stack)

    return min(answer) if answer else -1

print(jump(a,b))
