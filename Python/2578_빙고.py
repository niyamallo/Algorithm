# 빙고가 3개 이상이 되어야 게임이 끝나는데, 2개에서 한 번에 3개를 초과하는 경우를 생각하지 못해서 헤맸다.

import sys
input = sys.stdin.readline

nums = []
for i in range(5):
    nums += list(map(int, input().split()))

x = [0, 0, 0, 0, 0]
y = [0, 0, 0, 0, 0]
cnt = 0
LtoR = 0
RtoL = 0
bingo = 0

suggested_nums = []
for i in range(5):
    suggested_nums += list(map(int, input().split()))

for suggested_num in suggested_nums:
    a = nums.index(suggested_num)//5
    b = nums.index(suggested_num)%5
    x[a] += 1
    y[b] += 1
    cnt += 1
    if a == b:
        LtoR += 1
    if a+b == 4:
        RtoL += 1
    if LtoR >=5 or RtoL >=5 :
        bingo = 1
    if LtoR >=5 and RtoL >=5 :
        bingo = 2
    if bingo + x.count(5) + y.count(5) >= 3:
        print(cnt)
        break