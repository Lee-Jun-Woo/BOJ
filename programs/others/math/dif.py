# 미분

def f(x):
    return x**2 + 2*x + 3

for i in range(1, 6):
    print(f(i), end=' ')
    print(round((f(i+0.000000001)-f(i)) / 0.000000001, 3))