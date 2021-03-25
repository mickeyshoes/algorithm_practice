import sys

N = int(sys.stdin.readline().rstrip('\n'))

data_queue = []

def dequeue():
    result = data_queue.pop(0)
    return result

def enqueue(data):
    data_queue.append(data)

for i in range(N):
    order = sys.stdin.readline().rstrip('\n').split()
    if order[0] == 'push':
        enqueue(order[1])

    elif order[0] == 'pop':
        if len(data_queue) == 0:
            print(-1)
        else:
            print(dequeue())

    elif order[0] == 'front':
        if len(data_queue) == 0:
            print(-1)
        else:
            print(data_queue[0])

    elif order[0] == 'back':
        if len(data_queue) == 0:
            print(-1)
        else:
            print(data_queue[len(data_queue)-1])

    elif order[0] == 'size':
        print(len(data_queue))

    elif order[0] == 'empty':
        if len(data_queue) == 0:
            print(1)
        else:
            print(0)