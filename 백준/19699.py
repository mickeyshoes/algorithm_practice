import sys
input = sys.stdin.readline

N,M = map(int, input().rstrip('\n').split())
cows = list(map(int, input().rstrip('\n').split()))
stack = []
answer = []

#memoization 하면 계산량을 줄일 수 있다.
def check_prime(target:int)->bool:
    result = False
    div_limit = int(target**0.5)

    if target == 1:
        result = True

    for i in range(2, div_limit+1):
        if target % i ==0:
            return result

    result= True
    return result


def DFS(idx:int)-> None:
    if len(stack) == M:
        sum_stack = sum(stack)
        if check_prime(sum_stack):
            answer.append(sum_stack)
        return

    for i in range(idx, N):
        stack.append(cows[i])
        DFS(i+1)
        stack.pop()

DFS(0)
if answer:
    print(* sorted(set(answer)))
else:
    print(-1)