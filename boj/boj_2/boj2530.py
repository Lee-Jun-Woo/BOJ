h, m, s = map(int, input().split())
start = 3600*h + 60*m + s
end = (start + int(input())) % 86400
print(end // 3600, end=' ')
end %= 3600
print(end // 60, end=' ')
end %= 60
print(end)