import sys

input = sys.stdin.readline

a,b,c = map(int, input().rstrip('\n').split())

temp = [1,1,1]
target = [a,b,c]
limit = [15,28,19]
cnt = 1
while temp != target:

    for i in range(3):
        temp[i]+=1
        if temp[i] > limit[i]:
            temp[i] = 1
    cnt+=1

    # if cnt == 11:
    #     break

    print(f'{cnt} : temp : {temp}')

print(cnt)