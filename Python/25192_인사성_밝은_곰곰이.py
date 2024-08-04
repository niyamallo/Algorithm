import sys; input = sys.stdin.readline

n = int(input())
names = set()
count = 0

for _ in range(n):
    command = input().rstrip()
    if command == "ENTER":
        names.clear()
        continue
    if command in names:
        continue
    names.add(command)
    count += 1

print(count)