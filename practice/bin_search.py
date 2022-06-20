import sys
input = sys.stdin.readline

N,M = map(int, input().split())
sorted_ary = list(map(int, input().split()))

def bin_search(target):
    left, right = 0, len(sorted_ary)-1

    while left <=right:
        mid = (left+right)//2

        if sorted_ary[mid] == target:
            return mid+1
        elif sorted_ary[mid] > target:
            right = mid -1
        else:
            left = mid +1

    return -1


for _ in range(M):
    a = int(input())
    print(bin_search(a))