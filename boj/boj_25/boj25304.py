x = int(input())
money = 0
for product in range(int(input())):
    a, b = [int(num) for num in input().split()]
    money += a * b
if x == money:
    print('Yes')
else:
    print('No')