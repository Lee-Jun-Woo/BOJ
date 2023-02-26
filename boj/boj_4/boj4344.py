for _ in range(int(input())):
    array = [int(num) for num in input().split()][1:]
    mean = sum(array) / len(array)
    percent = len(list(filter(lambda x: x > mean, array))) / len(array) * 100
    print('%0.3f%%' % percent)