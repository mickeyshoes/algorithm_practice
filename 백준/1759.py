import sys
input = sys.stdin.readline

L,C = map(int, input().rstrip('\n').split())
words = input().rstrip('\n').split()
words.sort()
vowels = ('a','e','i','o','u')
stack = []

def vowelable(alphabet:str)->bool:
    if alphabet in vowels:
        return True
    return False
        
def DFS(idx:int, vowel:int, consonant:int)->None:

    if len(stack) == L:
        if vowel >=1 and consonant>=2:
            print(''.join(stack))
        return

    for i in range(idx, len(words)):
        stack.append(words[i])
        
        if vowelable(words[i]):
            vowel +=1
        else:
            consonant +=1
        
        DFS(i+1, vowel, consonant)

        if vowelable(stack.pop()):
            vowel -=1
        else:
            consonant -=1
        
DFS(0, 0, 0)