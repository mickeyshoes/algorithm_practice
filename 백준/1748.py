import sys
input = sys.stdin.readline

N = int(input().rstrip('\n'))
answer = 0
prev_count = 0
'''
1. 10**i -1 자리수 일 때 몇개의 값을 가졌는지 확인
2. 이전에 측정한 자리수의 갯수를 빼고 얻은 값에 i 만큼 곱함
'''
for i in range(1,len(str(N))+1):
    counting = (10**i) - 1
    if N < counting:
        counting = N
    target = counting - prev_count
    answer += target * i
    prev_count += target

print(answer)