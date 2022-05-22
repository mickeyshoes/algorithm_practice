from collections import defaultdict
from itertools import combinations

def lower_bound(score_list:list, score_len:int, point:int)->int:
    '''
    길이를 한번만 측정하게 해서 시간을 줄였다.
    전체 배열 길이에서 lower bound 해서 얻어낸 end 값을 빼주면 최종 길이다.
    '''
    start, end = 0, score_len
    
    while start <end:
        mid = (start+end)//2
        if score_list[mid] < point:
            start = mid +1
        else:
            end = mid
    
    return score_len - end
        
def solution(info, query):
    answer = []
    info_dict = defaultdict(list)
    '''
    처음에 info 에 담긴 모든 정보를 set 으로 담아서 교집합을 찾는 식으로 진행하였는데 O(len(data))
    a,b, score_list = set(), set(), list()
    그렇게 되면 (len(a) + len(b))*4 + len(score_list(:lower_bound_idx))의 시간이 걸리게 된다.
    미리 info 의 조합을 짜서 dict 에 추가하면, 2^4 * len(data) + O(log n)의 시간에 탐색이 가능해진다.
    '''
    for i in info:
        lan, job, car, food, point = i.split()
        for j in range(5):
            for comb in combinations([lan,job,car,food],j):
                info_dict[''.join(comb)].append(int(point))
    
    for v in info_dict.values():
        v.sort()
        
    for q in query:
        key, temp = '', ''
        for w in q:
            if w != ' ':
                temp +=w
            else:
                if temp != 'and' and temp !='-':
                    key+=temp
                temp =''
        answer.append(lower_bound(info_dict[key], len(info_dict[key]), int(temp)))
        
    return answer