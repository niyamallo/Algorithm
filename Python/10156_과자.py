import sys
input = sys.stdin.readline

price, quantity, money = map(int, input().split())
needs = price * quantity - money

if needs > 0:
    print(needs)
else:
    print(0)