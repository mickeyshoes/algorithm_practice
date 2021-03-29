import sys

while True:

    input_line = int(sys.stdin.readline().rstrip('n'))

    if input_line == 0:
        break

    else:
        input_line = list(str(input_line))

        palindrome = list(reversed(input_line))

        if palindrome == input_line:
            print('yes')
        else:
            print('no')