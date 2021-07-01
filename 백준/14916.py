N = int(input())
coin = (5,2)
count = 0
while N>1:
    if N % 5 ==0:
        a,b = divmod(N,5)
        count += a
        N = b
        break
    temp = N - coin[0]
    if temp > 5:
        N = temp
    else:
        N = N - coin[1]
    count +=1
if N ==1:
    count = -1
print(count)