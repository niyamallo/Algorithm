import sys
input = sys.stdin.readline

def rev(num):
    for i in range(len(num)-1,-1,-1):
        if num[i] != "0":
            return int(num[:i+1][::-1])

x, y = input().split()
total = rev(x) + rev(y)

print(rev(str(total)))