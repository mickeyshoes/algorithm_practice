def solution(skill, skill_trees):
    answer = 0
    for own_skill_tree in skill_trees:
        check = ''
        for item in own_skill_tree:
            if item in skill:
                check += item
        check_count = 0        
        for i in range(len(check)):
            if check[i] == skill[i]:
                check_count +=1
        if check_count == len(check):
            answer +=1
    return answer