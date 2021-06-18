def solution(A):
    from collections import Counter
    if not A:
        return -1
    a = Counter(A).most_common()[0]
    if a[1] <= len(A)//2:
        return -1
    return A.index(a[0])

result = solution([])
print(result)