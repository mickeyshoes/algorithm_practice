a = int(input('x input : '))
b = int(input('y input : '))

def calculate(a,b):
    if a >0 and b >0 :
        return 1
    elif a >0 and b <0 :
        return 4
    elif a <0 and b >0 :
        return 2
    elif a <0 and b <0:
        return 3
    else:
        print(f'{a}, {b}')
        return 0

calculate(a,b)
