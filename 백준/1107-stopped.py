import sys

present_channel = 100

target_channel = int(sys.stdin.readline().rstrip('\n'))
broken = int(sys.stdin.readline().rstrip('\n'))
broken_channel = list(map(int, sys.stdin.readline().rstrip('\n').split()))[:broken]
save_button = [i for i in range(9) if i not in broken_channel]

if len(save_button) == 0 :
    print(target_channel - present_channel + 1)
else:
    count = 0
    near_number = str() 

    for number in str(target_channel):
        temp = list(map(lambda y: abs(int(number) - y), save_button))
        temp_index = temp.index(min(temp))
        near_number += str(save_button[temp_index])
        count+=1

    print(f'near_number : {near_number} count : {count}')