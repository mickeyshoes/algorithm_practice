import sys

a,b = map(int, sys.stdin.readline().rstrip('\n').split())

prime = [False] *2 + [True] * (b-1)
temp_a = a

while temp_a<=b:
    for i in range(2, int(temp_a**0.5) +1):
        if temp_a % i == 0:
            print(f'temp_a  {temp_a} i : {i}')
            prime[temp_a] =False
            break
    temp_a +=1

for i in range(a,b+1):
    if prime[i]:
        print(i)