import sys
input = sys.stdin.readline

N = int(input().rstrip('\n'))
ary1 = list(map(int, input().rstrip('\n').split()))
ary1.sort()
M = int(input().rstrip('\n'))
ary2 = list(map(int, input().rstrip('\n').split()))
answer = []

print(f'ary1 : {ary1}')
for i in ary2:
    start =0
    end =N-1
    left_idx, right_idx = 0,0

    while start <= end:
        div = (start+end)//2
        if i > ary1[div]:
            start = div +1
        elif i < ary1[div]:
            end = div -1
        else:   
            #lower bound
            #음수가 있어 값이 같은지로 비교문을 넣어야 한다.
            print(start, end)
            break
            temp = div
            while start <= div:
                mid = (start+div)//2
                if i == ary1[mid]:
                    left_idx = mid
                else:
                    div = mid-1
        
            #upper bound
            #음수가 있어 값이 같은지로 비교문을 넣어야 한다.
            while div <=end:
                mid = (div+end)//2
                if i < ary1[mid]:
                    end = div -1
                else:
                    right_idx = mid
                    
            break
#     print(i, left_idx, right_idx)
#     if right_idx != left_idx:
#         answer.append(right_idx - left_idx+1)
#     else:
#         answer.append(0)
# print(' '.join([str(i) for i in answer]))