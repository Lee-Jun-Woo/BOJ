for _ in range(int(input())):
    lt, wt, le, we = map(int, input().split())
    st = lt * wt
    se = le * we
    if st > se:
        print('TelecomParisTech')
    elif st < se:
        print('Eurecom')
    else:
        print('Tie')