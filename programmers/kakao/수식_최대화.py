from itertools import permutations
'''
풀이 방법
    1. 숫자와 연산 문자를 추출하여 리스트를 생성한다.
    2. 연산 문자 순열을 생성하여 모든 우선순위인 경우를 계산한다
        - stack 을 활용하여 우선순위의 연산 문자를 계산한다.
        - 그 결과 값을 다음 우선순위의 연산 문자가 계산할 수 있도록 리스트를 초기화 해 준다.

후기
    stack 을 생각하지 못한게 가장 어려운 점이었다.

참고
https://eda-ai-lab.tistory.com/509
https://tech.kakao.com/2020/07/01/2020-internship-test/
'''
def operation_result(num1:int, num2:int, op:str)->int:
    result = 0
    if op == '-':
        result = num1 - num2
    elif op == '+':
        result = num1 + num2
    else:
        result = num1 * num2
    return result
        
def solution(expression):
    answer = 0
    operations = list()
    exp_to_list = list()
    temp = ''
    # 숫자와 연산 문자 추출 및 중복 제거
    for i in expression:
        if i.isdigit():
            temp += i
        else:
            exp_to_list.append(int(temp))
            exp_to_list.append(i)
            operations.append(i)
            temp = ''
    exp_to_list.append(int(temp))
    operations = list(set(operations))
    
    for ops in permutations(operations, len(operations)):
        # 계산을 위해 임시로 참조할 원본 리스트 복사
        temp_list = exp_to_list
        for op in ops:
            # stack 을 사용해서 특정 op가 찾아오면 계산하고 그 stack 을 다음 계산에 이용할 수 있도록
            stack = list()
            i, limit = 0, len(temp_list)
            
            while i != limit:
                if temp_list[i] != op:
                    stack.append(temp_list[i])
                else:
                    stack.append(operation_result(stack.pop(), temp_list[i+1], op))
                    i +=1
                i+=1
            temp_list = stack
        
        answer = max(answer, abs(temp_list[0]))
            
    return answer