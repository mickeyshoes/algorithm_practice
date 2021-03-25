import sys, copy

return_to_a = sys.stdin.readline().rstrip('\n')

if int(return_to_a) - 10 < 0:
    return_to_a = '0' + return_to_a

return_to_a = list(return_to_a)
answer = return_to_a
cycle = 0
check = []

while True:

    check.append(return_to_a[1])
    test = str(int(return_to_a[0]) + int(return_to_a[1]))
    if int(test) - 10 <0:
        test = '0' + test
    check.append(test[1])
    cycle +=1

    if answer == check:
        break

    else:
        return_to_a = copy.deepcopy(check)
        check.clear()

print(cycle)