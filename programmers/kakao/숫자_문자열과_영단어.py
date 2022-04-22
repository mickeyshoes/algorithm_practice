def solution(s):
    answer = []
    numbers = dict(zero='0', one='1', two='2', three='3', four='4', five='5', six='6', seven='7', eight='8', nine='9')

    stack = []
    for word in s:
        if not word.isdigit():
            stack.append(word)
        else:
            answer.append(str(word))

        if len(stack) >= 3 and ''.join(stack) in numbers:
            answer.append(numbers[''.join(stack)])
            stack = []

    return int(''.join(answer))