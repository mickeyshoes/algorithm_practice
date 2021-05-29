import sys
from queue import Queue

T = int(sys.stdin.readline().rstrip('\n'))
for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().rstrip('\n').split())

    cabbage_locate = []
    moved = []
    mx = [1,0,0,-1]
    my = [0,1,-1,0]

    for _ in range(K):
        k,v = map(int, sys.stdin.readline().rstrip('\n').split())
        cabbage_locate.append((k,v))


    def bfs(x:int, y:int):
        if (x,y) in moved:
            return 0
        q = Queue()
        q.put((x,y))
        moved.append((x,y))
        count = 1
        while q.qsize() > 0:
            qx,qy = q.get()
            for i in range(len(mx)):
                tx = qx + mx[i]
                ty = qy + my[i]
                loc = (tx,ty)
                if loc not in moved and loc in cabbage_locate:
                    moved.append(loc)
                    q.put(loc)
                    count +=1
        return count

    answer = 0
    for i in cabbage_locate:
        if bfs(i[0],i[1])>0:
            answer+=1
    print(answer)