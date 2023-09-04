n = int(input())

for i in range(1,n*2):
    print(" "*abs(n-i) + "*"*(2*(n-abs(n-i))-1))
