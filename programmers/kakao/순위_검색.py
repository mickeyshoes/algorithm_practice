from collections import defaultdict
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
        score[idx] = int(point)
        
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
                result = result & set(idx for idx in range(len(score)) if score[idx] >= target_score)
            else:
                result = result & info_dict[i]
        answer.append(len(result))
        
    return answer