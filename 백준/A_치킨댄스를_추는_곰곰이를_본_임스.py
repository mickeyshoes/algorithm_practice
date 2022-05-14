import sys
input = sys.stdin.readline

N = int(input().rstrip('\n'))
A,B = map(int, input().rstrip('\n').split())

ans = A//2 + B
print(N) if ans > N else print(ans)