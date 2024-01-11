def solution(cards):
    answer = 0
    boxes = len(cards)
    box = [0]*boxes
    group = []
    
    for i in range(boxes):
        cnt = 0
        if box[i] == 0:
            box[i] = 1
            cnt += 1
            num = cards[i] - 1
            while box[num] == 0:
                box[num] = 1
                cnt += 1
                num = cards[num] - 1
            group.append(cnt)
    group.sort(reverse=True)
    if len(group) == 1:
        answer = 0
    else:
        answer = group[0] * group[1]
    return answer