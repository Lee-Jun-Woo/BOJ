a = int(input())
x = 1
for _ in range(1000000):
    x = 0.5*(x+(a/x))
print(x)