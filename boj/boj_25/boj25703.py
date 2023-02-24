n = int(input())
print('int a;\nint *ptr = &a;')
if n >= 2: print('int **ptr2 = &ptr;')
if n >= 3:
    for i in range(3, n+1):
        print('int ', end='')
        print('*' * i, end='')
        print(f'ptr{i} = &ptr{i-1};')