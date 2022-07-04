import sys
from collections import defaultdict
input= sys.stdin.readline
N = int(input().rstrip('\n'))

# 1. define table
dp = defaultdict(list)
answer = []
# 2. init table
def is_decending(num:str)->bool:
    prev_value = 10
    for i in range(len(num)):
        target = int(num[i])
        if target >= prev_value:
            return False
        prev_value = target
    return True

for i in range(100):
    target = str(i)
    if is_decending(target):
        dp[len(target)].append(target)
        answer.append(i)

# 3. fill table
for i in range(3,10):
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