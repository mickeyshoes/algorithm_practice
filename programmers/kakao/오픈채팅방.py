def solution(record):
    answer = []
    id_dict = dict()
    
    for r in record:
        r = r.split()
        if len(r) >2:
            id_dict[r[1]] = r[2]
    
    for r in record:
        r = r.split()
        if r[0] == 'Enter':
            answer.append(f'{id_dict[r[1]]}님이 들어왔습니다.')
        elif r[0] == 'Leave':
            answer.append(f'{id_dict[r[1]]}님이 나갔습니다.')
        else:
            continue
    
    return answer