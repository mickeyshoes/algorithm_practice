import sys
input = sys.stdin.readline

N = int(input().rstrip('\n'))
infos = [tuple(map(int, input().rstrip('\n').split())) for _ in range(N)]

print(infos)
print(sorted(infos, reverse=True, key=lambda x:(x[0],x[1])))