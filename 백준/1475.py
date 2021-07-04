import sys
from collections import Counter
import math
N = sys.stdin.readline().rstrip('\n')
# temp = Counter(N)
# a = math.ceil((temp['9']+temp['6'])/2)
# comp = 0
# for i in temp.most_common():
#     if i[0] in ['6','9']:
#         continue
#     comp = i[1]
#     break

# print(max(a,comp))

answer = [0] * 10
for i in range(10):
    answer[i] = N.count(str(i))

temp = math.ceil((answer[6]+answer[9])/2)
del answer[6]
answer.pop()
answer.append(temp)
print(max(answer))