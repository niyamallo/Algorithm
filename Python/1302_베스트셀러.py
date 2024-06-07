import sys
input = sys.stdin.readline

n = int(input())
books = dict()
for _ in range(n):
    book = input().rstrip()
    if book in books:
        books[book] += 1
    else:
        books[book] = 1

best = [key for key, value in books.items() if max(books.values()) == value]
best.sort()

print(best[0])