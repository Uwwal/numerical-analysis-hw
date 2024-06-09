import numpy as np


def Hilbert(n):
    H = np.empty((n, n))

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            H[i - 1, j - 1] = 1 / (i + j - 1)
    return H


def Cholesky(m):
    n = m.shape[0]
    L = np.zeros_like(m)

    for i in range(n):
        for j in range(i + 1):
            if i == j:
                s = sum(L[i][k] ** 2 for k in range(j))
                L[i][j] = np.sqrt(m[i][i] - s)
            else:
                s = sum(L[i][k] * L[j][k] for k in range(j))
                L[i][j] = (m[i][j] - s) / L[j][j]

    return L


def solve(n, noise=False):
    H = Hilbert(n)
    x = np.ones(n).reshape(n, 1)
    if noise:
        x += np.random.normal(0, 1e-7, (n, 1))
    b = np.matmul(H, x)
    cond = np.linalg.cond(H, p=np.inf)
    L = Cholesky(H)

    L_inv = np.linalg.inv(L)
    x_hat = np.matmul(np.matmul(L_inv.T, L_inv), b)
    r = b - np.matmul(H, x_hat)
    delta = x_hat - x

    print(f"cond = {cond}")
    print(f"n:{n}, noise:{noise}")
    print(f"{np.linalg.norm(r, ord=np.inf):.20f}")
    print(f"{np.linalg.norm(delta, ord=np.inf):.20f}")

    print("***************************************")


solve(10)
solve(10, True)
solve(8)
solve(12)
solve(14)
