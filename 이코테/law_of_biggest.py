import sys

n, m, k = map(int, sys.stdin.readline().rstrip('\n').split())

num_list = list(map(int, sys.stdin.readline().rstrip('\n').split()))

num_list = num_list[:n]

def catch_big_number(num_list):
    big = num_list[0]

    for i in range(len(num_list)):
        if i + 1 == len(num_list):
            pass
        else: 
            if big < num_list[i+1]:
                big = num_list[i+1]

    num_list.remove(big)
    return big

num1 = catch_big_number(num_list)
num2 = catch_big_number(num_list)

if m <= k:
    print(num1 * m)

else:
    count = 0
    result = 0

    for i in range(m):
        if count == k:
            count = 0
            result +=num2
            i +=1
        else:
            result += num1
            count +=1

    print(result)

new_array = []

#반복되는 수열 생성
for i in range(k):
    new_array.append(num1)
new_array.append(num2)

solution = 0

array_repeat_count, remain = divmod(m, k+1)

solution = sum(new_array) * array_repeat_count + num1 * remain

print(solution)


