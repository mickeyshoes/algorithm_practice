from itertools import combinations

def solution(relation):
    answer = []
    row, column = len(relation[0]), len(relation)
    idx = tuple(range(row))
    # combination 을 활용하여 키 조합 생성
    for i in range(1, row+1):
        # 키 조합을 이용해 set을 만들어 유일성에 부합하는지 확인
        for comb in combinations(idx, i):
            unique_set = set()
            for j in range(column):
                unique_set.add(tuple(relation[j][item] for item in comb))
            if len(unique_set) == column:
                # 생성된 키를 통해 최소성을 확인하기
                check = sum([2**item for item in comb])
                appendable = True
                # 찾아낸 키가 이미 후보키의 부분집합인 경우 제거
                for k in answer:
                    if k & check == k:
                        appendable = False
                        break
                if appendable:
                    answer.append(check)
    return len(answer)