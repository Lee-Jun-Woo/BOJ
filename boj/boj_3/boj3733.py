while True:
    try:
        n, s = map(int, input().split())
    except EOFError:
        break
    print(s//(n+1))