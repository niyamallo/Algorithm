import sys
input = sys.stdin.readline

n = int(input())
ns = input().split()
n_dict = {}
for n in ns:
    if n in n_dict:
        n_dict[n] = n_dict[n] + 1
    else:
        n_dict[n] = 1

m = int(input())
ms = input().split()
for m in ms:
    if m in n_dict:
        print(n_dict[m], end = " ")
    else:
        print(0, end = " ")