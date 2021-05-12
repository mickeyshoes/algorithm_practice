import sys

N = int(sys.stdin.readline().rstrip('\n'))

stack = []
lvm_dict = {
    "command_list" : [],
    "command" : '',
    'cash' : 0,
}

def lvm(stack : list, lvm_dict : dict):
    if lvm_dict['command'] == 'PUSH':
        print(kargs['command'][1])
        stack.append(kargs['command'][1])

    elif lvm_dict['command'] == 'STORE':
        lvm_dict['cash'] = stack.pop()

    elif lvm_dict['command'] == 'LOAD':
        stack.append(lvm_dict['cash'])
    
    elif lvm_dict['command'] == 'PLUS':
        temp = 0
        for i in range(2):
            temp += stack.pop()
        stack.append(temp)

    elif lvm_dict['command'] == 'TIMES':
        temp = 0
        for i in range(2):
            temp *= stack.pop()
        stack.append(temp)

    elif lvm_dict['command'] == 'IFZERO':
        lvm_dict['cash'] = stack.pop()
        if temp == 0:
            lvm_dict['command'] = lvm_dict['command_list'][lvm_dict['command'][1]].split()
            lvm(stack, lvm_dict)

    else:
        return

for i in range(N):
    a = sys.stdin.readline().rstrip('\n')
    lvm_dict['command_list'].append(a)
    lvm_dict['command'] = a.split()
    lvm(stack, lvm_dict)
    print(stack)