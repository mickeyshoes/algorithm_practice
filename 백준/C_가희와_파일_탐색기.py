import sys
input = sys.stdin.readline

U, F = map(int, input().split())
user = dict()
file = dict()

def is_attached_group(file_info:list, u:str, executable:str)->bool:
    mod_number, group_info = file_info[0], file_info[1:]
    idx = -1
    aut_list = ['X','W','R']
    # 속한 그룹 확인(본인, 그룹, 그 외)
    if group_info[0] == u:
        idx = 0
    elif group_info[1] in user[u]:
        idx =1
    
    c_idx = 0
    for i in range(len(aut_list)):
        if aut_list[i] == executable:
            c_idx += 2 **i

    # 그 그룹에 맞는 숫자 확인해서 요청한 권한을 수용할 수 있는지 확인
    check = bin(c_idx& int(mod_number[idx]))

    if int(check,2) > 0:
        return True
    return False

for _ in range(U):
    u_info = input().split()
    temp = []
    if len(u_info) >1:
        temp.append(u_info[0])
    user[u_info[0]] = temp + u_info[-1].split(',')

for _ in range(F):
    f_info = input().split()
    file[f_info[0]] = f_info[1:]

for i in range(int(input())):
    u,f,c = input().split()
    if is_attached_group(file[f], u, c):
        print(1)
    else:
        print(0)