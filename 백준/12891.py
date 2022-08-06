import sys
input = sys.stdin.readline

S, P = map(int, input().rstrip('\n').split())
dna_string = input().rstrip('\n')
A,C,G,T = map(int, input().rstrip('\n').split())
cnt_dict = dict(A=0,C=0,G=0,T=0)
answer = 0

def is_substring(a:int, c:int, g:int, t:int)->bool:
    return a>=A and c>=C and g>=G and t>=T

for i in range(P):
    cnt_dict[dna_string[i]]+=1
if is_substring(*cnt_dict.values()):
    answer +=1

for i in range(1, S-P+1):
    cnt_dict[dna_string[i+P-1]]+=1
    cnt_dict[dna_string[i-1]]-=1
    if is_substring(*cnt_dict.values()):
        answer +=1

print(answer)