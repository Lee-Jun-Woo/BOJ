l, p = map(int, input().split())
news = list(map(int, input().split()))
for i in news:
    print(i - (l*p))