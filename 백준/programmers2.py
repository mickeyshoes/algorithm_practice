def bracket_check(s,start,end):
    count = 0
    while True:
        if s[0] in start:
            start_bracket = start.index(s[0])
            try:
                print('%s %s' % (start[start_bracket], end[start_bracket]))
                end_bracket = s.index(end[start_bracket])
                count+=1
                # 괄호 안의 길이가 0이면
                if len(s[start_bracket+1:end_bracket]) == 0:
                    # 괄호 뒤의 길이가 0인지 확인
                    if len(s[end_bracket+1:]) == 0:
                        break
                    # 아니면 그 뒤를 잘라서 대입
                    else:
                        count+=bracket_check(s[end_bracket+1:], start, end)
                        break
                # 아닌 경우 그 사이를 문자열에 대입
                else:                    
                    count += bracket_check(s[start_bracket+1:end_bracket], start, end)
                    count+=bracket_check(s[end_bracket+1:], start, end)
                    break
            except Exception as e:
                print(e)
                break
        else:
            break
            
    return count

def solution(s):
    answer = 0   
    for _ in range(len(s)):
        s = s[1:len(s)] + s[0]
        if bracket_check(s, ['(', '[', '{'], [')', ']', '}']) == len(s)//2:
            answer +=1
        
    return answer