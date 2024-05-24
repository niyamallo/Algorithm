import sys
from itertools import product
input = sys.stdin.readline

target = input().rstrip()
m = int(input())
ls = []
broken = set(list(map(int, input().split())))

if int(target) == 100:
    print(0)
    exit()

for i in range(10):
    if i not in broken:
        ls.append(str(i))

min_count = abs(int(target) - 100)

for i in range(1, len(target)+2):
    for j in product(ls, repeat = i):
        num = int(''.join(list(j)))
        if num > 1000000:
            break
        min_count = min(min_count, abs(int(target)-num)+i)

print(min_count)