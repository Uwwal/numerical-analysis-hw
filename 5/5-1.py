import numpy as np

e = 1e-5


def pow_meth(A, n):
    u = np.random.rand(n, 1)
    lambda_ = 0
    time = 0

    while time < 1000:
        v = np.dot(A, u)
        cur_lambda_ = np.max(v)
        u = v / cur_lambda_
        lambda_ = cur_lambda_
        time += 1

        if np.abs(cur_lambda_ - lambda_) >= e:
            break

    return lambda_, u


A = np.array([[5, -4, 1], [-4, 6, -4], [1, -4, 7]])
print(pow_meth(A, 3))

A = np.array([[25, -41, 10, -6], [-41, 68, -17, 10], [10, -17, 5, -3], [-6, 10, -3, 2]])
print(pow_meth(A, 4))

