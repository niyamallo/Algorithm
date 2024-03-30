import sys
input = sys.stdin.readline

n = int(input())
ls = list(map(int, input().split()))
arr = list(set(ls))
arr.sort()

dic = {}
for i in range(len(arr)):
    dic[arr[i]] = i

ans = []
for num in ls:
    ans.append(dic[num])

print(*ans)