for _ in range(int(input())):
    d, f, p = map(float, input().split())
    print('$' + '%.2f' % round(d*f*p, 2))