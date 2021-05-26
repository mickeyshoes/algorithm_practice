#https://jyami.tistory.com/15
import sys

T =int(sys.stdin.readline().rstrip('\n'))

dp = {
    0 : 0,
    1 : 1,
    2 : 2,
    3 : 4
}

for _ in range(T):
    number = int(sys.stdin.readline().rstrip())
    for i in range(4, number+1,1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    print(dp[number])