import sys
input = sys.stdin.readline

d, h, w = map(int, input().split())

ans = (d**2 / (h**2 + w**2))**(1/2)

print(int(ans*h), int(ans*w))