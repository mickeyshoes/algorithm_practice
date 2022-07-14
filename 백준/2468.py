import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
ary = [list(map(int, input().split())) for _ in range(N)]
visited = [[False for _ in range(N)] for __ in range(N)]
q = deque()