import sys
input = sys.stdin.readline

n = int(input())
doing = input().rstrip()
second = 0
lever = True
cnt = 0

if doing.count("W") < 2:
    print(cnt)
    exit()
for do in doing:
    if do == "P":
        lever = not lever
        if second == 1:
            print(6)
            break
    else:
        if second == 0:
            second += 1
            if lever:
                cnt = 5
            else:
                cnt = 1
        elif second == 1:
            second += 1
            print(cnt)
            break