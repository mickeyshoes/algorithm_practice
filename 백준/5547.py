import sys
input = sys.stdin.readline
W,H = map(int, input().split())

building_map = [list(map(int, input().split())) for _ in range(H)]

def move(x:int, y:int, d:int)->bool:
    return False