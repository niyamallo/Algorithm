import sys; input = sys.stdin.readline

strings = set()
answer = 0
n, m = map(int, input().split())
for _ in range(n):
    strings.add(input().rstrip())
for _ in range(m):
    newString = input().rstrip()
    if newString in strings:
        answer += 1

print(answer)