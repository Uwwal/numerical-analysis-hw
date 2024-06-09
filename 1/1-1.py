import numpy as np
import matplotlib.pyplot as plt


def calculate_actual_err(h):
    return np.abs(np.cos(1) - (np.sin(1 + h) - np.sin(1)) / h)


h_list = np.power(10, np.arange(-17, 0, 0.1))
actual_list = calculate_actual_err(h_list)

e = 1e-16

e1_list = h_list / 2
e2_list = (2.0 * e) / h_list
e3_list = e1_list + e2_list

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.plot(h_list[::], actual_list[::], color='red', label='实际总误差')
plt.plot(h_list[::], e1_list[::], color='green', label='截断误差')
plt.plot(h_list[::], e2_list[::], color='blue', label='舍入误差')
plt.plot(h_list[::], e3_list[::], color='brown', label='总误差限')
plt.xlabel("步长")
plt.legend()
plt.ylabel("误差")
plt.xscale('log')
plt.yscale('log')
plt.savefig('1-1.png')

plt.show()
