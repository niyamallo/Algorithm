import sys
input = sys.stdin.readline

string1, string2 = input().split()
strList1 = list(string1)
strLen1 = len(strList1)
strList2 = list(string2)
strLen2 = len(strList2)

cnt = 50

for j in range(strLen2 - strLen1 + 1):
    tmp = 0
    for i in range(strLen1):
        if strList1[i] != strList2[j+i]:
            tmp += 1
    if tmp < cnt:
        cnt = tmp

print(cnt)