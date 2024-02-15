import sys
input = sys.stdin.readline

n, m = map(int, input().split())
password = dict()

for _ in range(n):
    adr, pw = input().split()
    password[adr] = pw

for _ in range(m):
    adr = input().rstrip()
    print(password[adr])