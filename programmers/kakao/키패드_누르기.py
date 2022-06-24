def manhattan_distance(target, axis):
    
    keypad = {
        1: (-1,3), 2: (0,3), 3: (1,3),
        4: (-1,2), 5: (0,2), 6: (1,2),
        7: (-1,1), 8: (0,1), 9: (1,1),
        10: (-1,0), 0: (0,0), 11: (1,0)
    }
    
    return abs(keypad[target][0] - keypad[axis][0]) + abs(keypad[target][1] - keypad[axis][1])
    
def solution(numbers, hand):
    answer = ''
    for i in numbers:
        if i % 3 == 1:
            answer +='L'
        elif i % 3 == 0 and i != 0:
            answer +='R'
        else:
            left = answer.rfind('L')
            right = answer.rfind('R')
            if left < 0:
                left = manhattan_distance(10,i)
            else:
                left = manhattan_distance(numbers[left], i)
            if right < 0:
                right = manhattan_distance(11,i)
            else:
                right = manhattan_distance(numbers[right], i)
                
            print(f'left : {left} right : {right}')
            
            if left > right:
                answer += 'R'
            elif right > left:
                answer +='L'
            else:
                answer += hand[0].upper()
    return answer