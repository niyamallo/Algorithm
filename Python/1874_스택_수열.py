import sys

n, *quest = map(int, sys.stdin.buffer.read().splitlines())
nums =  [x for x in range(1, n+1)]
check = [0]*n
ans = [0]
result = []

nums_idx = 0
quest_idx = 0
possibility = True

while quest_idx < n:
    if quest[quest_idx] > ans[-1]:
        ans.append(nums[nums_idx])
        nums_idx += 1
        result.append("+")
    elif quest[quest_idx] == ans[-1]:
        ans.pop()
        quest_idx += 1
        result.append("-")
    elif quest[quest_idx] < ans[-1]:
        possibility = False
        print("NO")
        break

if possibility:
    print(*result, sep="\n")