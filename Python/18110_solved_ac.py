import sys
input = sys.stdin.readline

def roundUp(num):
    int_num = int(num)
    if num - int_num >= 0.5:
        return int_num + 1
    else:
        return int_num

n = int(input())
if n == 0:
    print(0)
else:
    nums = []
    for _ in range(n):
        nums.append(int(input()))
    nums.sort()

    cut = roundUp(n*0.15)

    total = 0
    for i in range(cut, n-cut):
        total += nums[i]

    average = roundUp(total/(n-2*cut))

    print(average)