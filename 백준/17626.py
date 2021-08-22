import sys

N = int(sys.stdin.readline().rstrip('\n'))
answer = []
i = 1
while N >=0:
    temp = i*i
    if temp < N:
        i +=1
        continue
    elif temp == N:
        answer.append(i)
        break
    else:
        temp = i-1
        answer.append(temp)
        N = N - temp**2
        i = 0
        
print(answer)