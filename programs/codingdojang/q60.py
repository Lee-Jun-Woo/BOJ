N, K = [int(num) for num in input("initial data:\n").split()]
a = list(range(1, N+1))
for _ in range(N-1):
    for _ in range(K-1): a.append(a.pop(0))
    del a[0]
print(f"answer:\n{a[0]}")