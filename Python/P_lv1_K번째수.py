def solution(array, commands):
    answer = []
    for i, j, k in commands:
        ls = array[i-1:j]
        ls.sort()
        ans = ls[k-1]
        answer.append(ans)
    return answer