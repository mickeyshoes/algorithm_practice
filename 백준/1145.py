import sys

number_list = list(map(int, sys.stdin.readline().rstrip('\n').split()))

init = min(number_list)

while True:

    count = 0
    for i in number_list:
        if init % i == 0:
            count +=1

    if count >= 3:
        break
    else:
        init +=1

print(init)