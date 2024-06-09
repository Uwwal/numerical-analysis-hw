import numpy as np
from scipy.optimize import root

def newton(f, f_, x0):
    e = 1e-10
    time = 0
    x = x0
    last = x0

    while abs(f(x)) > e or abs(x - last) > e:
        last = x
        x = last - f(x) / f_(x)
        print(f"xk: {last}, xk+1: {x}, k:{time}")

        time += 1
        if time == 100:
            print("100轮不收敛")
            return

    return x


def newton_(f, f_, x0, lambda0=0.95):
    e = 1e-10
    time = 0
    x = x0
    last = x0

    while abs(f(x)) > e or abs(x - last) > e:
        last = x
        x = last - f(x) / f_(x)
        print(f"xk: {last}, xk+1: {x}, k:{time}")

        t_lambda = lambda0
        i = 0
        while abs(f(x)) > abs(f(last)):
            x = last - t_lambda * f(last) / f_(last)
            i += 1
            print(f"xk: {last:.10f}, fx: {f(x):.10f}, i:{i}, lambda:{t_lambda:.10f}")
            t_lambda /= 2

        time += 1
        if time == 100:
            print("100轮不收敛")
            return

    return x


print("res1, newton: ", newton(lambda x: x ** 3 - 2 * x + 2, lambda x: 3 * x ** 2 - 2, 0))
print("res1, newton_downhill: ", newton_(lambda x: x ** 3 - 2 * x + 2, lambda x: 3 * x ** 2 - 2, 0))
x0 = np.array([-1])
sol = root(lambda x: x ** 3 - 2 * x + 2, x0)
print("res1, scipy: ", sol.x, sol.success)

print("res2, newton: ", newton(lambda x: -x ** 3 + 5 * x, lambda x: -3 * x ** 2 + 5, 1.35))
print("res2, newton_downhill: ", newton_(lambda x: -x ** 3 + 5 * x, lambda x: -3 * x ** 2 + 5, 1.35))
x0 = np.array([2.23])
sol = root(lambda x: x ** 3 - 2 * x + 2, x0)
print("res2, scipy: ", sol.x, sol.success)
