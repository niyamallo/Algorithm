import sys

input_ = sys.stdin.readline

N, B = input_().split()
num_N = list(N)
num_N.reverse()
B = int(B)

number = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

ans = 0
for i in range(len(num_N)):
    ans += number.index(num_N[i])*B**i

print(ans)