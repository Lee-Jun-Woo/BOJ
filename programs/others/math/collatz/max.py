# 초항별 콜라츠 수열의 최댓값

from collatz import collatz
import matplotlib.pyplot as plt

max_arr = [0]
for i in range(1, int(input())+1):
    max_arr.append(max(collatz(i)))

plt.plot(max_arr, 'ro')
plt.show()