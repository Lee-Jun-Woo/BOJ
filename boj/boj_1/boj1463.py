import sys
n = int(sys.stdin.readline())
result = 0
original = [n]
while 1 not in original:
    new = []
    for num in original:
        new.append(num-1)
        if not num % 2: new.append(num//2)
        if not num % 3: new.append(num//3)
    original = new
    result += 1
print(result)