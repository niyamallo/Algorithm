import sys
input = sys.stdin.readline

r, c = map(int, input().split())
jido = []
for i in range(r+2):
    jido.append([])
    for j in range(c+2):
        jido[i].append(".")

for i in range(r):
    a = list(input().rstrip())
    jido[i+1][1:len(a)+1] = a

r = len(jido)
c = len(jido[0])

vt = [[-1, 0], [1, 0], [0, -1], [0, 1]]
sinks = []
for i in range(r):
    for j in range(c):
        if jido[i][j] == "X":
            cnt = 0
            for k in range(4):
                if -1 < j + vt[k][0] < c and -1 < i + vt[k][1] < r and jido[i+vt[k][1]][j+vt[k][0]] == ".":
                    cnt += 1
            if cnt >= 3:
                sinks.append([i, j])

for sink in sinks:
    jido[sink[0]][sink[1]] = "."

r_min = r
r_max = 0
c_min = c
c_max = 0
for i in range(r):
    for j in range(c):
        if jido[i][j] == "X":
            r_min = min(r_min, i)
            r_max = max(i, r_max)
            c_min = min(c_min, j)
            c_max = max(j, c_max)

for i in range(r_max-r_min+1):
    print(*jido[r_min + i][c_min:c_max+1], sep="")