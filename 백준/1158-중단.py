import sys
from queue import Queue

N, K = map(int, sys.stdin.readline().rstrip('\n').split())

queue = Queue()
human_list = []

for i in range(1,N+1):
    human_list.append(i)

print(human_list)

while len(human_list) == 0:
    