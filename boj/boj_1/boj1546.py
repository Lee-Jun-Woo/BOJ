n = int(input())
arr = [int(num) for num in input().split()]
max_score = max(arr)
arr = [(score/max_score) * 100 for score in arr]
print(sum(arr) / n)