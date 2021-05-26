import sys

saw = set()
heard = set()
s,h = map(int, sys.stdin.readline().rstrip('\n').split())

for i in range(s):
    saw.add(sys.stdin.readline().rstrip('\n'))
for i in range(h):
    heard.add(sys.stdin.readline().rstrip('\n'))

a = sorted(saw.intersection(heard))
print(len(a))
for i in a:
    print(i)