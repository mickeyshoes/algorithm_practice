import sys

alphabet = sys.stdin.readline().rstrip('\n')

alphabet = alphabet.upper()

alpha_list = list(set(alphabet))

alpha_dict = {}

for i in alpha_list:
    alpha_dict[i] = int(0)

for i in range(len(alphabet)):
    if alphabet[i] in alpha_dict:
        alpha_dict[alphabet[i]] += 1

answer = []

for key, value in alpha_dict.items():
    if value == max(alpha_dict.values()):
        answer.append(key)

if len(answer) >1:
    print('?')

else:
    print(''.join(answer))