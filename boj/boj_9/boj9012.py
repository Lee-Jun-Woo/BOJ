def isBalanced(s):
    n = 0
    for i in range(len(s)):
        n += (1 if s[i]=='(' else -1)
        if n < 0:
            return "NO"
    return "YES" if n==0 else "NO"

for _ in range(int(input())):
    print(isBalanced(input()))