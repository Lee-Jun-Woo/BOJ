# 초항별 콜라츠 수열의 길이

from collatz import collatz
import matplotlib.pyplot as plt

len_arr = [0]
for i in range(1, int(input())+1):
    len_arr.append(len(collatz(i)))

plt.plot(len_arr, 'ro')
plt.show()