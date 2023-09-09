import sys

a = list(sys.stdin.readline().rstrip())
a.sort(reverse=True)
print("".join(a))