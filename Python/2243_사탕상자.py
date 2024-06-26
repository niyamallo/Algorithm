import sys; input = sys.stdin.readline
from math import ceil, log

def get_candy(left, right, node, rank):
    tree[node] -= 1
    if left == right:
        return left
    mid = (left + right) // 2
    if tree[node * 2] >= rank:
        return get_candy(left, mid, node * 2, rank)
    else:
        return get_candy(mid + 1, right, node * 2 + 1, rank - tree[node * 2])

def put_candy(left, right, node, candy, amount):
    tree[node] += amount
    if left == right:
        return
    mid = (left + right) // 2
    if candy <= mid:
        put_candy(left, mid, node * 2, candy, amount)
    else:
        put_candy(mid + 1, right, node * 2 + 1, candy, amount)

n = int(input())
h = ceil(log(10**6, 2)) + 1
tree = [0]*(2**h)

for _ in range(n):
    command = list(map(int, input().split()))
    if command[0] == 1:
        print(get_candy(1, 10**6, 1, command[1]))
    else:
        put_candy(1, 10**6, 1, command[1], command[2])