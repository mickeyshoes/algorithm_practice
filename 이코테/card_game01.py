import sys

card_list = []

row, column  = map(int, sys.stdin.readline().rstrip('\n').split())

for i in range(row):
    card_list.append(list(map(int, sys.stdin.readline().rstrip('\n').split())))
    del card_list[i][column:]

print(card_list)

low = 0

for i in range(row):
    print(f'minimun is {min(card_list[i])}')
    card_list[i].sort()
    print(f'card_list {i} : {card_list[i]}')
    if low - card_list[i][0] < 0:
        low = card_list[i][0]

print(low)