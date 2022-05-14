import sys
from collections import defaultdict
input = sys.stdin.readline

ans_dic = defaultdict(bool)
ans = 0
N = int(input().rstrip('\n'))

for _ in range(N):
    name = input().rstrip('\n')
    if name == 'ENTER':
        ans += sum(ans_dic.values())
        ans_dic = defaultdict(bool)
        continue
    ans_dic[name] = True

print(ans + sum(ans_dic.values()))