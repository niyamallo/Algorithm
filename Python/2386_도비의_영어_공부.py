import sys
input = sys.stdin.readline

while True:
    string = input().rstrip()
    if string == "#":
        break
    keyword = string[0]
    string = string.lower()
    print(f'{keyword} {string.count(keyword) - 1}')