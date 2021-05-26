import sys

s = sys.stdin.readline().rstrip('\n')
pattern = sys.stdin.readline().rstrip('\n')
count = s.replace(pattern,'1')
answer = 0
for i in count:
    if i == '1':
        answer +=1

print(answer)