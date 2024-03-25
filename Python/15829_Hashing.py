import sys
input = sys.stdin.readline

n = int(input())
alps = input().rstrip()
ALPHABET = ["0","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

cnt = 0
total = 0
for alp in alps:
    num = int(ALPHABET.index(alp))
    total += (num * (31**cnt))%1234567891
    cnt += 1

print(total%1234567891)