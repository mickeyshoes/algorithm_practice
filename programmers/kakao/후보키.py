from itertools import combinations

def solution(relation):
    row, column = len(relation[0]), len(relation)
    idx = tuple(range(row))
    cand_key_set = set()
    # combination 을 활용하여 키 조합 생성
    for i in range(1, row+1):
        # 키 조합을 이용해 set을 만들어 유일성에 부합하는지 확인
        for comb in combinations(idx, i):
            unique_set = set()
            for j in range(column):
                unique_set.add(tuple(relation[j][item] for item in comb))
            print(i, comb)
            # print(unique_set)
            if len(unique_set) == column:
                cand_key_set.add(bin(sum([2**item for item in comb])))
    # 생성된 키를 통해 최소성을 확인하기
    '''
    위에서 비트 마스킹 한 결과로 & 연산 돌려서 하나라도 1 뜨는 원소 제거하면 되는데
    생각만큼 코드가 잘 안짜진다..
    '''
    print(sorted(cand_key_set, key=lambda x:len(x)))
    
    return len(cand_key_set)