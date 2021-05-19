import sys

N = int(sys.stdin.readline().rstrip('\n'))

def stack(*args):
    if args[0][0] == 'push':
        args[1].append(args[0][1])
    
    if args[0][0] == 'pop':
        try:
            print(args[1].pop())
        except IndexError:
            print(-1)

    if args[0][0] =='size':
        print(len(args[1]))

    if args[0][0] =='empty':
        if len(args[1]) == 0:
            print(1)
        else:
            print(0)

    if args[0][0] == 'top':
        # print(f'cash : {cash} args[1] : {args[1]}')
        if len(args[1]) !=0:
            print(args[1][-1])
        else:
            print(-1)

    return args[1]

init_list = []

for i in range(N):
    command = list(sys.stdin.readline().rstrip('\n').split())
    init_list = stack(command, init_list)
    # print(init_list)
