import sys
N = int(sys.stdin.readline().rstrip('\n'))

answer =[[1,0],[0,1]]

for i in range(N-1):
    answer.append([
        answer[-1][0] + answer[-2][0],
        answer[-1][1] + answer[-2][1]
    ])

print(answer[-1][0], answer[-1][1])

# memory over 2

# first = 'A'
# second = 'B'

# for i in range(N-1):
#     temp = second
#     second += first
#     first = temp

# print(second.count('A'), second.count('B'))

# memory over 1

# dp = ['A','B']

# for i in range(N-1):
#     dp.append(dp[-1]+dp[-2])
#     print(dp[-1])

# print(dp[-1].count('A'), dp[-1].count('B'))
