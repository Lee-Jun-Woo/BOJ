# 로지스틱 사상

import matplotlib.pyplot as plt

x = float(input('초깃값 입력: '))
x_delta = x + 0.00000000000001
n = int(input('반복 횟수 입력: '))
x_list = [x]

for _ in range(n):
    x = 4*x*(1-x)
    x_list.append(x)
print('x: ' + str(x))

x_delta_list = [x_delta]

for _ in range(n):
    x_delta = 4*x_delta*(1-x_delta)
    x_delta_list.append(x_delta)

print('x delta: ' + str(x_delta))

plt.plot(x_list, 'r-', x_delta_list, 'b-')
plt.show()