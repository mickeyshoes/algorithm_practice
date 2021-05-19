import sys

key = sys.stdin.readline().rstrip('\n')
encoded_text = sys.stdin.readline().rstrip('\n')
decoded_text = 'MEETMEBYTHEOLDOAKTREENTH'
lines = len(encoded_text) // len(key)
sort_key = sorted(key)

decoded_dict = dict()
print(sort_key)
for i in range(len(key)):
    print(encoded_text[lines*i:lines*(i+1)])
    decoded_dict[i] = sort_key[i] + encoded_text[lines*i:lines*(i+1)]

print(decoded_dict)

values = list(decoded_dict.values())
plain_dict = dict()

for i in range(len(key)):
    for j in range(len(values)):
        if key[i] == values[j][0]:
            plain_dict[i] = values.pop(j)
            break

print(plain_dict)

for i in range(1, lines+1):
    for j in list(plain_dict.values()):
        print(j[i], end='')