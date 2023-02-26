a = input()
res = ''
for char in a:
    if 65 <= ord(char) <= 90:
        res += char.lower()
    else:
        res += char.upper()
print(res)