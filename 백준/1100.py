import sys
input = sys.stdin.readline

ary = [input().rstrip('\n') for _ in range(8)]
answer = 0

for i in range(8):
    check = [0,2,4,6]
    if i % 2 == 1:
        check = [i+1 for i in check]
    
    for j in check:
        if ary[i][j] == 'F':
            answer +=1

print(answer)