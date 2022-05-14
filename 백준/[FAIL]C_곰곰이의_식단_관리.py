import sys
import re
input = sys.stdin.readline

N = int(input().rstrip('\n'))
S = input().rstrip('\n')

result = re.findall('C+',S)
print(result)