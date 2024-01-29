import sys
input = sys.stdin.readline

fibonacci = [0]*491
fibonacci[1] = 1
for i in range(2,491):
    fibonacci[i] = fibonacci[i-1] + fibonacci[i-2]

while True:
    hour = int(input())
    if hour == -1:
        break
    print(f'Hour {hour}: {fibonacci[hour]} cow(s) affected')