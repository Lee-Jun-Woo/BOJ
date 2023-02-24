import sys

s = sys.stdin.read()
letter_cnt = [0] * 26

for char in s:
    if 97 <= ord(char) <= 122:
        letter_cnt[ord(char)-97] += 1

for i in range(26):
    if letter_cnt[i] == max(letter_cnt):
        print(chr(i+97), end='')