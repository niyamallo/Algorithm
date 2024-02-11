import sys
input = sys.stdin.readline
nums = set()

m = int(input())
for _ in range(m):
    num = list(input().split())
    cal = num[0]
    if len(num) == 2:
        num = int(num[1])
    if cal == "add":
        nums.add(num)
    elif cal == "remove":
        if num in nums:
            nums.remove(num)
    elif cal == "check":
        if num in nums:
            print(1)
        else:
            print(0)
    elif cal == "toggle":
        if num in nums:
            nums.remove(num)
        else:
            nums.add(num)
    elif cal == "all":
        nums = set([x for x in range(1,21)])
    else:
        nums = set()