import sys

decode_text = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "=",
                "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+",
                "w","e", "r", "t", "y", "u", "i", "o", "p", "[", "]", "\\",
                "s", "d", "f", "g", "h", "j", "k", "l", ";", "'", ":", '"',
                "x", "c", "v", "b", "n", "m", ",", ".", "/", "<", ">", "?"]

original_text = ["`", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-",
                "~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_",
                "q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "[", "]",
                "a", "s", "d", "f", "g", "h", "j", "k", "l", ";", "l", ":",
                "z", "x", "c", "v", "b", "n", "m", ",", ".", "m", "<", ">"]


while True:

    input_text = sys.stdin.readline().rstrip('\n').lower()

    if len(input_text) != 0:

        answer = str()
        for i in input_text:
            if i in decode_text:
                answer += original_text[decode_text.index(i)]
            else:
                answer +=i

        print(answer.upper())

    else:
        break