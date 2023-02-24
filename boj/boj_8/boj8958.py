import sys
for i in range(int(sys.stdin.readline().rstrip())):
    ox = sys.stdin.readline().rstrip()
    straight = 0
    score = 0
    for j in ox:
        if j == 'O': straight += 1
        else: straight = 0
        score += straight
    print(score)