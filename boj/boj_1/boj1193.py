X = int(input())
num, row = 0, 0

while X > num:
    row += 1
    num += row

if row % 2:
    upper = 1
    lower = row
    while num > X:
        upper += 1
        lower -= 1
        num -= 1
else:
    upper = row
    lower = 1
    while num > X:
        upper -= 1
        lower += 1
        num -= 1

print(f'{upper}/{lower}')