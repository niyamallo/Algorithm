import sys; input = sys.stdin.readline

n = int(input())
score = 0
pineapple = 0
blueberry = 0
times = [-11]*9

for _ in range(n):
    time, a, b = map(int, input().split())
    if time - times[a] <= 10:
        score += 150
    else:
        score += 100
    times[a] = time
    if a < 5:
        pineapple += score
    else:
        blueberry += score
    score = 0

print(pineapple, blueberry)