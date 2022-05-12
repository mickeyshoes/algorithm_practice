def solution(answers):
    answer = []
    correct = [0,0,0]
    pick = ['12345', '21232425', '3311224455']
    for i in range(len(answers)):
        target = str(answers[i])
        if pick[0][i%5] == target:
            correct[0] +=1
        if pick[1][i%8] == target:
            correct[1] +=1
        if pick[2][i%10] == target:
            correct[2] +=1

    target = max(correct)
    if correct.count(target)>1:
        answer = [i+1 for i in range(len(correct)) if correct[i] == target]
    else:
        answer.append(correct.index(target)+1)
    return answer