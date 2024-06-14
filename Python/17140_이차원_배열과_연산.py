import sys
input = sys.stdin.readline

def sorting(matrix, RC):

    sorted_matrix = []
    max_count = 0
    
    for i in range(len(matrix)):
        
        B = []
        dic = dict()
        
        for j in range(len(matrix[i])):
            if matrix[i][j]!=0:
                if matrix[i][j] not in dic:
                    dic[matrix[i][j]] = 1
                else:
                    dic[matrix[i][j]] += 1
        
        for key,value in dic.items():
            B.append([key,value])
        
        B.sort(key=lambda x: [x[1],x[0]])
        C = sum(B,[])
        max_count = max(max_count,len(C))
        sorted_matrix.append(C)
    
    for i in sorted_matrix:
        i+=[0]*(max_count-len(i))
        if len(i)>100:
            break
    
    return sorted_matrix if RC=="R" else list(zip(*sorted_matrix))

r,c,k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(3)]

result = 0

while True:

    count = 0

    if result >=101:
        print(-1)
        break

    if r-1<len(A) and c-1<len(A[0]):
        if A[r-1][c-1] == k:
            print(result)
            break

    if len(A)>=len(A[0]):
        A = sorting(A,"R")

    else :
        A = sorting(list(zip(*A)),"C")
        
    result += 1