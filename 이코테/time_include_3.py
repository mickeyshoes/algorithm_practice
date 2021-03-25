import sys

hour = int(sys.stdin.readline().rstrip('\n'))

start = [0, 0, 0]
target = [hour, 59, 59]
count = 0

while True:

    if sum(start) == sum(target):
        break

    else:
        start[2]+=1

        if start[2] == 60:
            start[2] = 0
            start[1] +=1

        if start[1] == 60:
            start[1] = 0
            start[0] +=1

        if '3' in str(start):
            count +=1

print(f'count : {count} start : {start} target : {target}')
