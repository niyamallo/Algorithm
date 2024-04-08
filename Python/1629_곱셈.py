import sys
input = sys.stdin.readline

def find_mod(a, b, c):
    if b == 1:
        return a%c
    elif a == 1:
        return 1
    elif b%2 == 0:
        return (find_mod(a, b//2, c)**2)%c
    else:
        return ((find_mod(a, b//2, c)**2)*a)%c
    
a, b, c = map(int, input().split())
ans = find_mod(a, b, c)

print(ans)