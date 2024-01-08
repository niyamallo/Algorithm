import sys

input_ = sys.stdin.readline

a, b = map(int, input_().split())
m = int(input_())
nums_a = list(map(int,input_().split()))

num_10 = 0

for i in range(m):
    num_10 += a**i*nums_a[m-1-i]

nums_b = []

for i in range(19,-1,-1):
    if b**i <= num_10:
        num_b = int(num_10//b**i)
        nums_b.append(num_b)
        num_10 -= num_b*b**i
    else:
        nums_b.append(0)

for i in range(len(nums_b)):
    if nums_b[i] != 0:
        ans = nums_b[i:]
        break
    else:
        pass

print(*ans)