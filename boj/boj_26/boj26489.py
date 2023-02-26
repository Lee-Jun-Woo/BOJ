cnt = 0
while True:
    try:
        ggfjj = input()
        cnt += 1
    except EOFError:
        break
print(cnt)