word = input().upper()
char_count = [0] * 26
for i in range(26):
    char_count[i] = word.count(chr(i+65))
if char_count.count(max(char_count)) == 1:
    print(chr(char_count.index(max(char_count))+65))
else: print('?')