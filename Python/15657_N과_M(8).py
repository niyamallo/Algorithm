import sys
input = sys.stdin.readline

def backtracking():
    if len(answer) == m:
        print(" ".join(map(str, answer)))
    else:
        for num in nums:
            if len(answer) == 0 or answer[-1] <= num:
                answer.append(num)
                backtracking()
                answer.pop()

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
answer = []

backtracking()