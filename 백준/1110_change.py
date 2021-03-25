import sys

N = int(sys.stdin.readline().rstrip('\n'))

answer = N
count = 0

while True:

    seat_of_ten , seat_of_one = divmod(N,10)

    N = (seat_of_one * 10) + ( (seat_of_ten + seat_of_one) %10)
    count +=1

    if N == answer:
        break

print(f'answer : {answer} count : {count}')