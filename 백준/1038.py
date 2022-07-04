import sys
from collections import defaultdict
input= sys.stdin.readline
N = int(input().rstrip('\n'))

# 1. define table
dp = defaultdict(list)
answer = []

# 2. init table
for i in range(10):
    target = str(i)
    dp[1].append(target)
    answer.append(target)

# 3. fill table
for i in range(2,10):
    temp = []
    for j in range(i-1,10):
        for item in dp[i-1]:
            if str(j) > item[0]:
                temp.append(str(j)+item)
            else:
                break
    dp[i] = temp
    answer.extend(temp)
answer.append(9876543210)

if N >= len(answer):
    print(-1)
else:
    print(answer[N])