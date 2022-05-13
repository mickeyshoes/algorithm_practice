from itertools import permutations
import re
def solution(expression):
    answer = 0
    # 연산 문자 추출 및 중복 제거
    operations = list(set(re.findall('\D+', expression)))
    # 가장 우선 순위가 낮은 문자열을 제거 하면서 계산하는거 어떰?
    for ops in permutations(operations, len(operations)):
        print(ops)
        for i in range(len(operations)-1,0,-1):
            print(ops[i])
            expression = ''.join(expression.split(ops[i]))
            print(expression)
    return answer