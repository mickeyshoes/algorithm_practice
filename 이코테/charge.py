money = int(input("money : "))

money_list = [500, 100, 50 ,10]

total = 0

for i in money_list:
    count, money = divmod(money,i)
    total +=count

print(total)