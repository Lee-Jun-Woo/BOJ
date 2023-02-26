word = input()
result = 0
for chr in word:
    ascii_code = ord(chr)
    if ascii_code <= 82: result += ((ascii_code - 56) // 3)
    elif ascii_code == 83: result += 8
    elif 84 <= ascii_code <= 86: result += 9
    else: result += 10
print(result)