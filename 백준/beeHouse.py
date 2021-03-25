import sys
import math

a = int(sys.stdin.readline().rstrip('\n'))

print( math.ceil((3 + math.sqrt(12*a-3)) / 6 ))