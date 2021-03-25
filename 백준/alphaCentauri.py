import sys

T = int(sys.stdin.readline().rstrip('\n'))

for i in range(T):
    start, target = map(int,sys.stdin.readline().rstrip('\n').split())

    move_length = 0

    for i in range(1,target-start):
        if target - start ==1:
            print(move_length+1)
            break
        elif target <= start+i:
            print(move_length+2)
            break
        else:
            start+=i
            move_length+=1