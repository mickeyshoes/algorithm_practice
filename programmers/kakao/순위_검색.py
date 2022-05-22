from collections import defaultdict
def lower_bound(score_list:list, point:int)->set:
    start, mid, end = 0, 0, len(score_list)
    
    while start <=end:
        mid = (start+end)//2
        if score_list[mid][0] < point:
            start = mid +1
        else:
            end = mid
    
    target_set = set(score_list[i][1] for i in range(mid,end))
    return target_set
        
def solution(info, query):
    answer = []
    # string info -> dict(set)으로
    info_dict = defaultdict(set)
    score = [0] * len(info)
    for idx, target in enumerate(info):
        lan, job, car, food, point = target.split()
        info_dict[lan].add(idx)
        info_dict[job].add(idx)
        info_dict[car].add(idx)
        info_dict[food].add(idx)
        score[idx] = tuple(int(point), idx)
    score.sort(key=lambda x:x[0])
        
    for q in query:
        stack = []
        all_pass = set([i for i in range(len(info))])
        result = set([i for i in range(len(info))])
        temp = ''
        for w in q:
            if w !=' ':
                temp +=w
            else:
                if temp != "and":
                    stack.append(temp)
                temp = ""
        stack.append(temp)
        
        for i in stack:
            if i == '-':
                result = result & all_pass
            elif i.isdigit():
                target_score = int(i)
                result = result & lower_bound(score, target_score)
            else:
                result = result & info_dict[i]
        answer.append(len(result))
        
    return answer