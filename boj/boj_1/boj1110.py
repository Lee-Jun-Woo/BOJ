import sys
num = int(sys.stdin.readline().rstrip())
cnt = 0
START_NUM = num
while True:
    cnt += 1
    num = (num%10)*10 + (num//10 + num%10)%10
    if num == START_NUM: break
print(cnt)