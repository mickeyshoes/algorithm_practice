import sys

N = int(sys.stdin.readline().rstrip('\n'))

word_list = []

for i in range(N):
    word_list.append(sys.stdin.readline().rstrip('\n'))

word_list = list(set(word_list))

word_list.sort()
word_list.sort(key=len)

for i in word_list:
    print(i)