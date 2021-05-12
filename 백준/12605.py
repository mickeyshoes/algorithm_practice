import sys

N = int(sys.stdin.readline().rstrip('\n'))
answer = []
for _ in range(N):
    answer.append(sys.stdin.readline().rstrip('\n'))

order = 1
for i in answer:
    i = i.split()[::-1]
    print(f'Case #{order}:', end=' ')
    order+=1
    for j in i:
        print(j, end=" ")
    print()