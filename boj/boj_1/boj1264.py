while True:
    string = input().lower()
    if string == '#':
        break
    print(string.count('a') +
    string.count('e') +
    string.count('i') +
    string.count('o') +
    string.count('u'))