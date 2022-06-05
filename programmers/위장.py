def solution(clothes):
    from collections import Counter
    from functools import reduce
    a = Counter([category for item, category in clothes])
    answer = reduce(lambda x,y : x*(y+1), a.values() ,1) - 1
    return answer