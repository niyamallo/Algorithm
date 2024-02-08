import sys
input = sys.stdin.readline

n = int(input())
ns = sorted(map(int, input().split()))
m = int(input())
ms = list(map(int, input().split()))

for m in ms:
    start = 0
    end = len(ns)-1
    mid = (start+end)//2
    while start <= end:
        if m == ns[mid]:
            print(1)
            break
        elif m < ns[mid]:
            end = mid-1
            mid = (start+end)//2
        elif m > ns[mid]:
            start = mid+1
            mid = (start+end)//2
    if start > end:
        print(0)

