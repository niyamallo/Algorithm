import sys; input = sys.stdin.readline

n = int(input())
a_price = 0
b_price = 0
for time in list(map(int, input().split())):
    a_price += ((time//30)+1) * 10
    b_price += ((time//60)+1) * 15

if b_price < a_price:
    print("M", b_price)
elif a_price == b_price:
    print("Y", "M", a_price)
else:
    print("Y", a_price)