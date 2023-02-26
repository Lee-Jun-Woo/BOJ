n = (int(input()) // 100) * 100
f = int(input())

while True:
    if n % f:
        n += 1
    else:
        print("%02d" % (n%100))
        break