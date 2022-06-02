def solution(progresses, speeds):
    answer = []
    from queue import Queue
    temp = Queue()
    for i in range(len(progresses)):
        d,v = divmod(100 - progresses[i], speeds[i])
        if v >0:
            d+=1
        temp.put(d)
            
    stack = []
    stack.append(temp.get())
    
    for i in range(temp.qsize()):
        a = temp.get()
        if a > stack[0]:
            answer.append(len(stack))
            stack = []
            stack.append(a)
        else:
            stack.append(a)
            
    answer.append(len(stack))
        
    return answer