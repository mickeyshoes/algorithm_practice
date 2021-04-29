def prime_check(num : int) -> bool:
    if num <2 : return False

    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

import sys

print(prime_check('a'))

N = int(sys.stdin.readline().rstrip('\n'))

print(sum(map(prime_check, map(int, sys.stdin.readline().rstrip('\n').split()))))