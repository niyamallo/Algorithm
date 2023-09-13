import sys
import math

ls = [0]*11

for i in list(map(int, sys.stdin.readline().rstrip())):
    ls[i] += 1

ls[6] = math.ceil((ls[6] + ls[9])/2)
ls[9] = 0

print(max(ls))