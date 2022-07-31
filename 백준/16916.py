import sys
input = sys.stdin.readline

S = input().rstrip('\n')
sub = input().rstrip('\n')

if len(S.replace(sub,'')) == len(S):
    print(0)
else:
    print(1)