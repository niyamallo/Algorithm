import sys
input = sys.stdin.readline

s = list(input().rstrip())
l = list(input().rstrip())

while len(s) < len(l):
    if l[-1] == "A":
        l.pop()
    elif l[-1] == "B":
        l.pop()
        l.reverse()

if s == l:
    print(1)
else:
    print(0)