import sys
input = sys.stdin.readline

N,S = map(int, input().rstrip('\n').split())
ary = list(map(int, input().rstrip('\n').split()))
ans = 100001
left, right = 0,0
temp_sum = ary[left]

while True:
    if left == N:
        break

    if temp_sum >=S:
        ans = min(ans, right-left+1)
    else:
        if right < N-1:
            right+=1
            temp_sum += ary[right]
            continue

    temp_sum -= ary[left]
    left+=1

print(ans) if ans != 100001 else print(0)