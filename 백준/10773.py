import sys

N = int(sys.stdin.readline().rstrip('\n'))

list_a = []

for _ in range(N):
    i = int(sys.stdin.readline().rstrip('\n'))
    if i == 0:
        try:
            list_a.pop()
        except:
            continue
    else:
        list_a.append(i)

print(sum(list_a))