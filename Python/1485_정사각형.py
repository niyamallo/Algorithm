import sys
input = sys.stdin.readline

def lengthOfLine(a, b):
    return (a[0]-b[0])**2 + (a[1]-b[1])**2

n = int(input())
for _ in range(n):
    flag = True
    dots = []
    for _ in range(4):
        dots.append(list(map(int, input().split())))
    dots.sort()

    if lengthOfLine(dots[0], dots[3]) != lengthOfLine(dots[1], dots[2]):
        print(0)
        continue

    side = lengthOfLine(dots[2], dots[3])
    for i in range(1,3):
        if lengthOfLine(dots[0], dots[i]) != side:
            print(0)
            flag = False
            break
    if flag:
        print(1)