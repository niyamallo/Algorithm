import sys
input = sys.stdin.readline

n = int(input())
fibonacci = [1]*46
for i in range(2,46):
    fibonacci[i] = fibonacci[i-1] + fibonacci[i-2]

for _ in range(n):
    print(fibonacci[int(input())])