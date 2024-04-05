import sys
input = sys.stdin.readline

def backtracking():
    if len(answer) == m:
        new_ans = [x for x in answer]
        answer_list.append((new_ans))
    else:
        for i in range(len(nums)):
            if not visited[i]:
                visited[i] = True
                answer.append(nums[i])
                backtracking()
                answer.pop()
                visited[i] = False

n, m = map(int, input().split())
nums = list(map(int, input().split()))
answer_list = []
answer = []
visited = [False]*(n)

backtracking()
answer_list.sort()

print(*answer_list[0])
for i in range(1, len(answer_list)):
    if answer_list[i] != answer_list[i-1]:
        print(*answer_list[i])