import sys
input = sys.stdin.readline

N = int(input().rstrip('\n'))
answer = 0
'''
10^i-1 보다 큰지 확인해서 몇개를 가지고 있는지 확인
이전 값을 저장하고 있다가 다음 값을 답에 더해줄때 i 만큼 곱해서 더해주어야함
'''
prev_count = 0
for i in range(1,len(str(N))+1):
    counting = (10**i) - 1
    target = counting - prev_count
    answer += target * i
    print(i, target, answer)
    temp = target


# for i in range(1,9):
#     if N <0:
#         break
#     target = N % (10**i)
#     print(i,target)
#     answer += i * target
#     N -= 10**i

print(answer)