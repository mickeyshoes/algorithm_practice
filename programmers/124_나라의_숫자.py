def solution(n):
    answer = ''
    
    while True:
        a,b = divmod(n,3)
        
        if n <= 3:
            answer += '124'[b-1]
            break
        else:
            answer += '412'[b]
            if b == 0:
                n = a - 1
            else:
                n = a
            
    return answer[::-1]