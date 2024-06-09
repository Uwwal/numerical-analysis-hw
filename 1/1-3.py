import numpy as np


cur = np.float32(0)
N = 0
while True:
    N += 1
    pre = cur
    cur += np.float32(1.0 / N)
    if pre == cur:
        break

res_32 = cur
print(f"单精度不变化: {N}")

cur = np.float64(0)
for n in range(1, N):
    pre_res64 = cur
    delta = np.float32(1.0 / n)
    cur += delta
    if n > 2000000 and (n % 10000 == 0 or N - n <= 10):
        print(f"n: {n}, sum: {cur}")

res_64 = cur

print(res_32)
print(res_64)

err = res_64 - res_32
print(f"误差: {err}, {err/res_64}")

L = 2
R = 1e19
mach = 2 ** 54
euler = 0.577216

for i in range(100):
    mid = 0.5 * (L + R)
    if mid * (np.log(mid) + euler) > mach:
        R = mid
    else:
        L = mid

print(L)
