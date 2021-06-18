def solution(N, A):
    from collections import defaultdict
    d = defaultdict(int)
    add_number = 0
    for i in range(len(A)):
        if A[i] == N+1:
            if d.values():
                add_number += max(d.values())
            d.clear()
            continue
        d[A[i]] += 1

    return [d[i]+add_number for i in range(1,N+1)]

result = solution(5, [3,3,6,4,6,5,6])

print(result)