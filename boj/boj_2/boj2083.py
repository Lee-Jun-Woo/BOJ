while True:
    name, age, weight = input().split()
    if name == '#': break
    print(name, end=' ')
    if int(age) > 17 or int(weight) >= 80:
        print('Senior')
    else:
        print('Junior')