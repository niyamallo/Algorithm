def solution(record):
    answer = []
    dic = {}
    
    for sentence in record:
        words = sentence.split()
        if words[0] == "Enter" or words[0] == "Change":
            dic[words[1]] = words[2]
    
    for sentence in record:
        words = sentence.split()
        if words[0] == "Enter":
            answer.append("%s님이 들어왔습니다." %dic[words[1]])
        elif words[0] == "Leave":
            answer.append("%s님이 나갔습니다." %dic[words[1]])
    
    return answer