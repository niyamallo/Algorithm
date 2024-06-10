from itertools import combinations
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
ls = list(combinations(range(1,n+1), m))
answer = 0
answer_set = set()
for i in range(1, 1+m):
    answer_set.add(i)

for nums in ls:
    cnt = 0
    for num in nums:
        if num in answer_set:
            cnt += 1
        if cnt == k:
            answer += 1
            break

print(answer/len(ls))