import sys
input = sys.stdin.readline

N = int(input().rstrip('\n'))

def is_prime(number:int)->bool:
    for i in range(2, int(number**0.5)+1):
        if number % i == 0:
            return False
    return True

ary = list()

if N >2:
    ary.append(2)
    ary.extend([i for i in range(3,N+1,2) if is_prime(i)])
else:
    ary = [i for i in range(2,N+1) if is_prime(i)]
    
cnt, end, prefix_sum = 0,0,0
lim = len(ary)
for i in range(lim):
    while end != lim:
        if prefix_sum >= N:
            if prefix_sum == N:
                cnt +=1
            break
        prefix_sum += ary[end]
        end+=1
    prefix_sum -= ary[i]

print(cnt+1) if ary[-1] == N else print(cnt)