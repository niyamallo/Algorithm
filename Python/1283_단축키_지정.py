import sys
input = sys.stdin.readline

n = int(input())
alps = set()
for _ in range(n):
    option = input().rstrip()
    tmp = option.lower()
    flag1 = False
    flag2 = False
    for i in range(len(tmp)):
        if (i == 0 or tmp[i-1] == " ") and tmp[i] not in alps:
            alps.add(tmp[i])
            print(option[:i] + f'[{option[i]}]'+ option[i+1:])
            flag1 = True
            break
    
    if not flag1:
        for i in range(len(tmp)):
            if tmp[i] != " " and tmp[i] not in alps:
                alps.add(tmp[i])
                print(option[:i] + f'[{option[i]}]'+ option[i+1:])
                flag2 = True
                break
    if not flag1 and not flag2:
        print(option)