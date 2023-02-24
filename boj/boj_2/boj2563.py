black = set()
for _ in range(int(input())):
    black_x, black_y = map(int, input().split())
    for a in range(black_x, black_x+10):
        for b in range(black_y, black_y+10):
            black.add((a, b))
print(len(list(black)))