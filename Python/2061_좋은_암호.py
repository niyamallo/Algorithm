import sys
input = sys.stdin.readline

k, l = map(int, input().split())

for i in range(2, l):
    if(k % i == 0):
        print("BAD", i)
        exit()
        
print("GOOD")