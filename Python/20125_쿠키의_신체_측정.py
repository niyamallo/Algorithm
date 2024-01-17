import sys

n = int(sys.stdin.readline())
groups = [list(sys.stdin.readline().rstrip()) for x in range(n)]

for i in range(n):
    if groups[i].count("*") == 1:
        x = groups[i].index("*")
        y = i + 1
        break

leftArm = 0
for i in range(x):
    if groups[y][i] == "*":
        leftArm += 1

rightArm = 0
for i in range(x+1, n):
    if groups[y][i] == "*":
        rightArm += 1

body = -1
endBodyX = 0
endBodyY = 0
for i in range(y, n):
    if groups[i][x] == "_":
        endBodyX = x
        endBodyY = i - 1
        break
    body += 1

leftLeg = 0
for i in range(endBodyY+1, n):
    if groups[i][endBodyX-1] == "*":
        leftLeg += 1

rightLeg = 0
for i in range(endBodyY+1, n):
    if groups[i][endBodyX+1] == "*":
        rightLeg += 1

print(y+1, x+1)
print(leftArm, rightArm, body, leftLeg, rightLeg)
