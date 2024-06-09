import numpy as np
from matplotlib import pyplot as plt
from mpmath import besselj

epsilon = 1e-10


def zeroin(f, a, b):
    a = np.float64(a)
    b = np.float64(b)
    fa = f(a)
    fb = f(b)

    if fa * fb > 0:
        print("signal error")
        return None
    c = a
    fc = fa
    d = b - c
    e = d

    time = 0

    while fb != 0:
        if fa * fb > 0:
            a = c
            fa = fc
            d = b - c
            e = d

        if abs(fa) < abs(fb):
            c = b
            b = a
            a = c

            fc = fb
            fb = fa
            fa = fc

        m = 0.5 * (a - b)
        tol = 2.0 * epsilon * max(abs(b), 1)

        if abs(m) <= tol or fb == 0:
            break

        if abs(e) < tol or abs(fc) <= abs(fb):
            d = m
            e = m
        else:
            s = fb / fc
            if a == c:
                p = 2.0 * m * s
                q = 1.0 - s
            else:
                q = fc / fa
                r = fb / fa
                p = s * (2.0 * m * q * (q - r) - (b - c) * (r - 1.0))
                q = (q - 1.0) * (r - 1.0) * (s - 1.0)

            if p > 0:
                q = -q
            else:
                p = -p

            if 2.0 * p < 3.0 * m * q - abs(tol * q) and p < abs(0.5 * e * q):
                e = d
                d = p / q
            else:
                d = m
                e = m

        c = b
        fc = fb

        time += 1

        if abs(d) > tol:
            b += d
        else:
            b -= np.sign(b - a) * tol

        fb = f(b)

    print(f"time: {time}, root: {b}")
    return b


def J0(x):
    return besselj(0, x)


x_list = np.arange(1, 50, 1e-2)
y_list = [J0(x) for x in x_list]

_, axes = plt.subplots()
plt.plot(x_list, y_list)
plt.axhline(0, linestyle='--', color='black')
for x in range(1, 50, 3):
    plt.axvline(x=x, color='r', linestyle='--')
plt.show()

intervals = [(1 + i * 3, 1 + (i + 1) * 3) for i in range(10)]

_, axes = plt.subplots()
plt.plot(x_list, y_list)
plt.axhline(0, linestyle='--', color='black')

for _, (a, b) in enumerate(intervals):
    zero = zeroin(J0, a, b)
    plt.scatter(zero, 0, s=20, zorder=10)

plt.show()