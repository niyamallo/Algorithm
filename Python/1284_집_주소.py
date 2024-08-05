while True:
    command = list(input())
    if command[0] == "0":
        break
    count = len(command) + 1
    for num in command:
        if num == "0":
            count += 4
        elif num == "1":
            count += 2
        else:
            count += 3
    print(count)