import sys; input = sys.stdin.readline

seven25_price, seven25_weight = map(int, input().split())
seven25_avg = seven25_price/seven25_weight
min_avg = seven25_avg

n = int(input())
for _ in range(n):
    tmp_price, tmp_weight = map(int, input().split())
    tmp_avg = tmp_price/tmp_weight
    if tmp_avg < min_avg:
        min_avg = tmp_avg

print(round(min_avg*1000, 2))