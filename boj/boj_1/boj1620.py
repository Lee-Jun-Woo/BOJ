n, m = map(int, input().split())
pok2num = dict()
num2pok = dict()
for i in range(1, n+1):
    pokemon = input()
    pok2num[pokemon] = i
    num2pok[i] = pokemon
for _ in range(m):
    question = input()
    if question.isdigit():
        print(num2pok[int(question)])
    else:
        print(pok2num[question])