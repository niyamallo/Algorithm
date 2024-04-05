import sys
input = sys.stdin.readline

def backtracking():
    if len(answer) == m:
        print(" ".join(map(str, answer)))
    else:
        for num in nums:
            if num not in answer:
                answer.append(num)
                backtracking()
                answer.pop()

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
answer = []

backtracking()