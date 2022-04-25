def solution(N, stages):
    answer = []
    failure = {i:[0,0] for i in range(1,N+1)}
    
    for user in stages:
        if user != N+1:
            failure[user][0] +=1
        for clear in range(1, user):
            failure[clear][1] +=1
    print(sorted(failure.items(), key=lambda a,b: b[0]/b[1]))
    return answer