n = int(input())
result = 0
for _ in range(n):
    letters = []
    word = input()
    i = 0
    for chr in word:
        if chr in letters:
            if chr == word[i-1]: pass
            else: break
        else:
            letters.append(chr)
        i += 1
    if i == len(word): result += 1
print(result)