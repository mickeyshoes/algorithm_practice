import sys

input = sys.stdin.readline

N = int(input().rstrip('\n'))
distance = list(map(int, input().rstrip('\n').split()))
costs = list(map(int, input().rstrip('\n').split()))

min_cost = costs[0]
mul_distance = 0
answer= 0

for i in range(len(distance)):
    if costs[i] < min_cost:
        answer += (mul_distance * min_cost)
        min_cost = costs[i]
        mul_distance = 0
    
    mul_distance += distance[i]

print(answer + min_cost * mul_distance)