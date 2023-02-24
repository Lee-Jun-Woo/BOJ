piece_found = [int(piece) for piece in input().split()]
piece_correct = [1, 1, 2, 2, 2, 8]
for i in range(6):
    print(piece_correct[i] - piece_found[i], end=' ')