n = int(input())
cards = map(int, input().split())
m = int(input())
targets = map(int, input().split())

cards_dict = dict()
for i in cards:
    if cards_dict.get(i):
        cards_dict[i] += 1
    else:
        cards_dict[i] = 1

for j in targets:
    if cards_dict.get(j):
        print(cards_dict[j], end=' ')
    else:
        print(0, end=' ')