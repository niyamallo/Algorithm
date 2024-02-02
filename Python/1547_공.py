import sys
input = sys.stdin.readline

M = int(input())
cups = [0, 1, 0, 0]
for _ in range(M):
    x, y = map(int, input().split())
    cups[x], cups[y] = cups[y], cups[x]

print(cups.index(1))