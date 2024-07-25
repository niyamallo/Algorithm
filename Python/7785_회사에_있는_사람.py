import sys; input = sys.stdin.readline

workingPeo = set()

n = int(input())
for i in range(n):
    name, statue = input().split()
    if statue == "enter":
        workingPeo.add(name)
    elif statue == "leave":
        workingPeo.remove(name)

answer = sorted(list(workingPeo), reverse=True)

for i in range(len(answer)):
    print(answer[i])