from sys import stdin
n, k = map(int, stdin.readline().split())
people = list(range(1, n+1))
print('<', end='')
while len(people) > 1:
    for _ in range(k-1):
        people.append(people.pop(0))
    print(people.pop(0), end=', ')
print(people[0], end='>')