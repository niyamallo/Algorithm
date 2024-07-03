import sys; input = sys.stdin.readline

n = int(input())
ls = list(map(int, input().split()))
t, p = map(int, input().split())

a = 0
for num in ls:
    if num%t == 0:
        a += num//t
    else:
        a += num//t + 1
print(a)

b = sum(ls)//p
c = n - p*b
print(b, c)