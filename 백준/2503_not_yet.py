import sys
from itertools import combinations
input = sys.stdin.readline
N = int(input())
visited = [False] * 10
case = [
    [[1,0,0], [0,1,0], [0,0,1]],
    [[1,1,0], [1,0,1], [0,1,1]],
]

for _ in range(N):
    number, strike, ball = input().split()
    strike, ball = int(strike), int(ball)
    activate = []
    for i in range(3):
        if strike>0:
            activate.append(1)
            strike -=1
        else:
            activate.append(0)

    for c in combinations(activate, 3):
        print(c)
    


# stack = []
# result = set()
# def permutations():

#     if len(stack) == 3:
#         result.add(''.join([str(i) for i in stack]))
#         return

#     for i in range(1,10):
#         if not visited[i]:
#             visited[i] = True
#             stack.append(i)
#             permutations()
#             stack.pop()
#             visited[i] = False

# permutations()

price_value = [False] * 3
test = set()
def make_specific_values():

    if sum(price_value) == 3:
        test.add(''.join([str(i) for i in stack]))
        return

    for i in range(len(price_value)):
        if not price_value[i]:
            for j in range(1,10):
                print(i, j, stack)
                if not visited[j]:
                    price_value[i] = True
                    visited[j] = True
                    stack[i] = j
                    make_specific_values()
                    visited[j] = False
                    price_value[i] = False

stack = [2,1,0]
visited[1] = True
visited[2] = True
price_value[1] = True
price_value[0] = True
make_specific_values()
print(test)
print(len(test))


