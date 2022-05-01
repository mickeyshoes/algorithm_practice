def is_prime(number:int)->bool:
    result = False
    if number not in [0,1]:
        for i in range(2, int(number**0.5)+1):
            if number % i == 0:
                return result
        result = True
    return result

def make_k_base(n,k):
    base_string = ''
    while n > 0:
        d,m = divmod(n,k)
        base_string = str(m) + base_string
        n = d
    return base_string

def solution(n, k):
    answer = 0
    base_number = make_k_base(n,k)
    for num in base_number.split('0'):
        if len(num) >0 and is_prime(int(num)):
            answer +=1
        
    return answer