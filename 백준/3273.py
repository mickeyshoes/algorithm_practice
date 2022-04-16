import sys
input = sys.stdin.readline

N = int(input().rstrip('\n'))
items = list(map(int, input().rstrip('\n').split()))
items.sort()
X = int(input().rstrip('\n'))
start = 0
end = N - 1
cnt = 0

while start < end:
    value = items[start] + items[end]
    if value > X:
        end -=1
    else:
        if value == X:
            cnt+=1
        start +=1

print(cnt)