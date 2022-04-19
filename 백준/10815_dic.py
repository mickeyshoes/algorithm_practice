import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input().rstrip('\n'))
ary1 = list(map(int, input().rstrip('\n').split()))
dic = defaultdict(bool)
M = int(input().rstrip('\n'))
ary2 = list(map(int, input().rstrip('\n').split()))
answer = []

for i in ary1:
    dic[i] = True

for i in ary2:
    if dic[i]:
        answer.append(1)
    else:
        answer.append(0)


print(' '.join([str(i) for i in answer]))