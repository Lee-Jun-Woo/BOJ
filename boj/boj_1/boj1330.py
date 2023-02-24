a, b = [int(num) for num in input().split()]
if not (a-b): print('==')
else: print('>' if a>b else '<')