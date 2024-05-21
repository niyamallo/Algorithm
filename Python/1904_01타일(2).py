n = int(input())
if n == 1:
    print(1)
else:
    a = 1
    b = 2
    for _ in range(n-2):
        a, b = b, (a+b)%15746
    print(b)