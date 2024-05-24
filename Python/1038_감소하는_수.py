from itertools import combinations

n = int(input())
answer = []
for i in range(1,11):
    for j in combinations(range(10), i):
        answer.append(int(''.join(map(str, reversed(list(j))))))
answer.sort()
length = len(answer)

if n >= length:
    print(-1)
else:
    print(answer[n])