import sys
import re

input = sys.stdin.readline

N = int(input().rstrip('\n'))
l,r = input().rstrip('\n').split('*')
filter = re.compile(l+'[a-z]*'+r)

for i in range(N):
    user = input().rstrip('\n')
    result = filter.match(user)
    try:
        if result.group() == user:
            print('DA')
        else:
            print('NE')
    except AttributeError:
        print('NE')