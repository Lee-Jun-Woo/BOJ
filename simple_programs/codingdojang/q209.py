import random

cat = random.randint(1, 7)
human = 2
i = 1
cnt = 0

while cat != human:
    cat += (1 if round(random.random()) == 0 else -1)
    if cat == 0: cat = 2
    if cat == 8: cat = 6
    human = int(-abs(i - 5.5) + 6.5)
    print(f'{i}일차: 고양이는 {cat}번 방에 있고, 사람은 {human}번 방의 문을 열었다.')
    if cat != human: i += 1
    cnt += 1

if not cnt: print('1일차: 고양이는 2번 방에 있고, 사람은 2번 방의 문을 열었다.')
print(f'{i}일차에 고양이와 사람 모두 {cat}번 방에 있었다.')
print('고양이를 잡았다!')