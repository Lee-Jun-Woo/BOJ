coordinates = []
for _ in range(int(input())):
    coordinates.append(tuple(map(int, input().split())))
coordinates.sort(key=lambda xy: xy[1])
coordinates.sort(key=lambda xy: xy[0])
for coor in coordinates:
    print(coor[0], end=' ')
    print(coor[1])