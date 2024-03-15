import sys
input = sys.stdin.readline

n = int(input())
ALP_SET = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
ALPS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for _ in range(n):
    alps = input().rstrip()
    checkAlps = [0]*26
    for alp in alps:
        if alp in ALP_SET:
            checkAlps[ALPS.index(alp)] += 1
    total = 0
    for i in range(len(checkAlps)):
        if checkAlps[i] == 0:
            total += 65 + i
    print(total)