import sys
N, W, H, L = map(int, sys.stdin.readline().rstrip('\n').split())
print(min(((W//L) * (H//L)), N))