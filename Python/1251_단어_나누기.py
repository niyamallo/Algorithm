word = input()
words = []

for i in range(1, len(word)-1):
    for j in range(i+1, len(word)):
        head = word[:i][::-1]
        body = word[i:j][::-1]
        tail = word[j:][::-1]
        words.append(head+body+tail)

words.sort()
print(words[0])