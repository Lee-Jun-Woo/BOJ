students = set(range(1, 31))
students_suc = set()
for _ in range(28):
    students_suc.add(int(input()))
students = tuple(students - students_suc)
print(min(students))
print(max(students))