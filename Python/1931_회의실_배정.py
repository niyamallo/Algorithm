import sys
input = sys.stdin.readline

n = int(input())
ls = []
for _ in range(n):
    a, b = map(int, input().split())
    ls.append((a, b))
ls.sort(key=lambda x:(x[1], x[0]))

end = 0
cnt = 0

for new_start, new_end in ls:
    if end <= new_start:
        end = new_end
        cnt += 1

print(cnt)