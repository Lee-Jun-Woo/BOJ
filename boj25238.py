a, b = map(int, input().split())
user_defend = a * ((100-b)/100)
print(0 if user_defend >= 100 else 1)