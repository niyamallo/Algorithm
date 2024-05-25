import sys
input = sys.stdin.readline

def back_tracking(idx, depth):
    if depth == l:
        vo, co = 0, 0
        for alp in answer:
            if alp in ['a', 'e', 'i', 'o', 'u']:
                vo += 1
            else:
                co += 1
        if vo >= 1 and co >=2:
            print(''.join(answer))
            return
    
    else:
        for i in range(idx, c):
            answer.append(alps[i])
            back_tracking(i+1, depth+1)
            answer.pop()

l, c = map(int, input().split())
alps = sorted(list(input().split()))
answer = []

back_tracking(0,0)