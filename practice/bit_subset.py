
def make_subset(total_set:list, l:int)->None:
    for i in range(1<<l):
        print('{', end='')
        for j in range(l):
            if i & (1<<j):
                print(total_set[j], end=',')
        print('}')

a = ['A','B','C','D']

make_subset(a,len(a))