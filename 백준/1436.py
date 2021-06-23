import sys

N = int(sys.stdin.readline().rstrip('\n'))
c = 0
i = 666
while True:
    if '666' in str(i):
        c +=1
        if N == c:
            print(i)
            break
    i+=1