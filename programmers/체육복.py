def solution(n, lost, reserve):
    lost = set(lost)
    reserve = set(reserve)
    cashing = lost & reserve
    answer = n - len(lost) + len(cashing)
    lost = lost - cashing
    reserve = reserve - cashing

    for i in lost:
        for j in (i-1, i+1):
            if j in reserve:
                reserve.remove(j)
                answer+=1
                break
            else:
                continue
    return answer