import sys

N = int(sys.stdin.readline().rstrip('\n'))

to_be_sorted = [int(sys.stdin.readline().rstrip('\n')) for _ in range(N)]


def quick_sort(sorted_list, left, right):

    if left >= right:
        print(f'break! left : {left} right : {right}')
        return

    else:
        pivot_index = len(sorted_list) // 2
        left_index = left
        right_index = right

        while True:

            if left_index >= right_index:
                break

            else:
                for i in range(left_index,len(sorted_list)):
                    if sorted_list[pivot_index] < sorted_list[i]:
                        left = i
                        break
                    else:
                        left_index +=1

                for i in range(right_index,0,-1):
                    if sorted_list[pivot_index] > sorted_list[i]:
                        right = i
                        break
                    else:
                        right_index -=1

                temp = sorted_list[left]
                sorted_list[left] = sorted_list[right]
                sorted_list[right] = temp

        print(f'list is now {sorted_list}')
        quick_sort(sorted_list[:pivot_index],0,pivot_index-1)
        quick_sort(sorted_list[pivot_index:],pivot_index, len(sorted_list)-1)

quick_sort(to_be_sorted, 0 , len(to_be_sorted)-1)
print(to_be_sorted)

    # for i in range(len(to_be_sorted)):
    #     if to_be_sorted[pivot_index] > to_be_sorted[i]:
    #         right = i

    #     if to_be_sorted[pivot_index] < to_be_sorted[i]:
    #         left = i

    