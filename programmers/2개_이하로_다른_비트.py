def solution(numbers):
    answer = []
    for number in numbers:
        if number % 2 ==0:
            answer.append(number+1)
        else:
            #while 문을 돌며 +1 한 수와 xor 한 수의 1의 갯수를 세는 것은 시간초과가 난다.
            num_to_bin = '0' + bin(number)[2:]
            idx = num_to_bin.rfind('01')
            num_to_bin = num_to_bin[:idx] + '10' + num_to_bin[idx+2:]
            answer.append(int(num_to_bin, 2))
    return answer