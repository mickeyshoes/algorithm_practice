from collections import Counter
def solution(N, stages):
    stage_counts = Counter(stages)
    failure = {i:0 for i in range(1,N+1)}
    users = len(stages)
    
    for i in range(1, N+1):
        now = stage_counts[i]
        stage_failure = 0
                
        if users != 0 and now != 0:
            stage_failure = now/users
            users -= now
        
        failure[i] = stage_failure
        
    return [k for k,v in sorted(failure.items(), key= lambda x: x[1], reverse=True)]