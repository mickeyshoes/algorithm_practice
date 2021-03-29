import sys

X = int(sys.stdin.readline().rstrip('\n'))

def my_func(X):
    count =0
    while True:

        if X == 1:
            break

        elif X == 2:
            count +=1
            break

        else:
            new_x, remain = divmod(X,3)
            X = new_x
            count = count + remain + 1
    return count

def bottom_top(X):
    cache = []
    for i in range(0,X+1):
        cache.append(0)

    for i in range(2,X+1):
        if i % 6 == 0:
            cache[i] = min(cache[i//3], cache[i//2], cache[i-1]) +1
        elif i % 3 == 0:
            cache[i] = min(cache[i//3], cache[i-1])+1
        elif i % 2 == 0:
            cache[i] = min(cache[i//2], cache[i-1])+1
        else:
            cache[i] = cache[i-1]+1
    return cache[X]

print(bottom_top(X))

while True:
    if my_func(X) != bottom_top(X):
        print(X)
        break
    else:
        X +=1
