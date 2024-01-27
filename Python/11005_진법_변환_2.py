import sys
input = sys.stdin.readline

N, B = map(int, input().split())
arr = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ans = ""

while N > 0:
    ans += arr[N%B]
    N = N//B

print(ans[::-1])