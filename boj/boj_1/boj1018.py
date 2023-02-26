n, m = map(int, input().split())
board = []
result = 32
 
for _ in range(n):
    board.append(input())
 
for i in range(n-7):
    for j in range(m-7):
        draw = 0
        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a + b) % 2 == 0:
                    if board[a][b] != 'B':
                        draw += 1
                else:
                    if board[a][b] != 'W':
                        draw += 1
        if draw > 32:
            draw = 64-draw
        if draw < result:
            result = draw
 
print(result)