import sys
input = sys.stdin.readline

N = int(input())
# table define
dp = [0 for _ in range(N+1)]

#input init value
dp[1] = 1
dp[2] = 2
dp[3] = 3

# fill table