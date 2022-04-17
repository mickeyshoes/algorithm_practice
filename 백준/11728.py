import sys
input = sys.stdin.readline

N,M = map(int, input().rstrip('\n').split())
A = list(map(int, input().rstrip('\n').split()))
B = list(map(int, input().rstrip('\n').split()))

answer = []
a_idx, b_idx = 0,0

while a_idx !=N and b_idx !=M:
    target = 0 
    
    if A[a_idx] > B[b_idx]:
        target = B[b_idx]
        b_idx +=1
    elif A[a_idx] < B[b_idx]:
        target = A[a_idx]
        a_idx+=1
    else:
        target = A[a_idx]
        answer.append(target)
        a_idx+=1
        b_idx+=1
    answer.append(target)

answer = answer + A[a_idx:] + B[b_idx:]

print(*answer)
