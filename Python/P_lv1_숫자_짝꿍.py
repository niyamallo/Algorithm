def solution(X, Y):
    answer = ''
    list_X = [0]*10
    list_Y = [0]*10
    for num in X:
        list_X[int(num)] += 1
    for num in Y:
        list_Y[int(num)] += 1
    
    list_result = []
    for i in range(10):
        list_result.append(min(list_X[i], list_Y[i]))
    if sum(list_result) == 0:
        answer = "-1"
    elif sum(list_result) == list_result[0]:
        answer = "0"
    else:
        for i in range(9, -1, -1):
            answer += list_result[i]*f'{i}'
    
    return answer