import sys
import math

a ,b ,v = map(int, sys.stdin.readline().rstrip('\n').split())

print( math.ceil((v-1)/(a-b)))
