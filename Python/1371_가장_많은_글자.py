import sys
input = sys.stdin.read

alp = "abcdefghijklmnopqrstuvwxyz"
ls = [0]*26

book = input().replace("\n", "").replace(" ","")
for s in book:
    ls[alp.index(s)] += 1

maxFreq = max(ls)

result = ""
for i in range(26):
    if ls[i] == maxFreq:
        result += alp[i]

print(result)