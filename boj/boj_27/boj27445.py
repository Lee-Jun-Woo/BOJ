n, m = map(int, input().split())
col_lst = []
for _ in range(n-1):
    col_lst.append(int(input()))
row_list = list(map(int, input().split()))
col_lst.append(row_list[0])
r = col_lst.index(min(col_lst)) + 1
c = row_list.index(min(row_list)) + 1
print(r, c)