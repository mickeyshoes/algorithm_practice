import sys
from queue import Queue

start, end = map(int, sys.stdin.readline().rstrip('\n').split())

q = Queue()
visited = [False] * 100001
q.put((start,0))

while q.qsize() > 0 :
    t, c = q.get()

    if t == end:
        print(c)
        break

    else:
        t = [t-1, t+1, 2*t]
        for i in t:
            if 0<= i <=100000 and not visited[i-1]:
                q.put((i,c+1))
                visited[i-1] = True