import sys

init_state = sys.stdin.readline().rstrip('\n')
# 한 글자씩 잘라서 리스트에 삽입
init_state = list(init_state)

limit = 8
count = 0

if ord(init_state[0]) > 105:
    print(count)

else:
    init_state[0] = ord(init_state[0]) - 96

init_state = list(map(int, init_state))

move_up = [ [-2,-1], [-2, 1]]
move_down = [ [2, -1], [2, 1]]
move_left = [ [-1, -2], [1, -2]]
move_right = [ [1, 2], [-1, 2] ]

move = []
move.extend(move_up)
move.extend(move_down)
move.extend(move_left)
move.extend(move_right)

for i in move:
    result = [x+y for x,y in zip(init_state,i)]
    print(result)
    if result[0]>limit or result[1]>limit or result[0]<1 or result[1]<1:
        pass
    else:
        count +=1

print(count)