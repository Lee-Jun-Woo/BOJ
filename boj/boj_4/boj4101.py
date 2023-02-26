while True:
    int1, int2 = map(int, input().split())
    if int1 == int2 == 0: break
    if int1 > int2: print('Yes')
    else: print('No')