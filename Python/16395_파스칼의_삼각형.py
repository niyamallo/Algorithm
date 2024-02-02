import sys
input = sys.stdin.readline

n, k = map(int, input().split())

pascal = [0, 1, 0]

for _ in range(n-1):
    new_pascal = [0]
    for i in range(len(pascal)-1):
        new_pascal.append(pascal[i]+pascal[i+1])
    new_pascal.append(0)
    pascal = new_pascal

print(pascal[k])
