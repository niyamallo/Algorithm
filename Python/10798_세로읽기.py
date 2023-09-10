import sys

ls = []

for _ in range(5):
    ls.append(sys.stdin.readline().rstrip())
longest = -1
for i in ls:
    if len(i) > longest:
        longest = len(i)

ans = ""
for j in range(longest):
    for i in ls:
        if len(i) >= j+1:
           ans += i[j]

print(ans)

