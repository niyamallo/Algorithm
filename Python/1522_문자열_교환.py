import sys
input = sys.stdin.readline

string = list(input().rstrip())
sw = string.count("a")
lenString = len(string)
string = string + string[0:lenString-1]

cnt = sw
for i in range(lenString):
    tmp = string[i:i+sw].count("b")
    if tmp < cnt:
        cnt = tmp

print(cnt)