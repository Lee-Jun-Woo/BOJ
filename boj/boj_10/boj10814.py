people = []
for _ in range(int(input())):
    people.append(tuple(input().split()))
people.sort(key=lambda person: int(person[0]))
for p in people:
    print(p[0] + ' ' + p[1])