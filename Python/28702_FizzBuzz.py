ls = []
for i in range(3):
    ls.append(input())

answer = 0
for i in range(3):
    if ls[i] not in ["Fizz", "Buzz", "FizzBuzz"]:
        answer = int(ls[i]) + 3 - i
        break

if answer%3 == 0 and answer%5 == 0:
    print("FizzBuzz")
elif answer%3 == 0:
    print("Fizz")
elif answer%5 == 0:
    print("Buzz")
else:
    print(answer)