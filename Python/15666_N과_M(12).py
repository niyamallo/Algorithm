import sys
input = sys.stdin.readline

def backtracking():
    if len(answer) == m:
        print(" ".join(map(str, answer)))
    else:
        for i in range(len(nums)):
            if len(answer) == 0 or answer[-1] <= nums[i]:
                answer.append(nums[i])
                backtracking()
                answer.pop()

n, m = map(int, input().split())
nums = list(set(map(int, input().split())))
nums.sort()
answer = []

backtracking()