import sys
input = sys.stdin.readline

n = int(input())
min_A, min_B, min_C, max_A, max_B, max_C = 0, 0, 0, 0, 0, 0
for _ in range(n):
    a, b, c = map(int, input().split())
    min_A, min_B, min_C = a + min(min_A, min_B), b + min(min_A, min_B, min_C), c + min(min_B, min_C)
    max_A, max_B, max_C = a + max(max_A, max_B), b + max(max_A, max_B, max_C), c + max(max_B, max_C)
print(max(max_A, max_B, max_C), min(min_A, min_B, min_C))