import numpy as np

e = 1e-5


def is_upper(A):
    n = A.shape[0]
    for i in range(n):
        for j in range(i):
            if np.abs(A[i, j]) > e:
                return False
    return True


def get_eigen_values(A0):
    A = np.copy(A0)
    while not is_upper(A):
        q, r = np.linalg.qr(A)
        A = np.matmul(r, q)
        print(A * 2)
        print(r)
    return np.diagonal(A)


def get_eigen_values_offset(A0, n):
    A = np.copy(A0)
    while not is_upper(A):
        diagonal_value = A[n - 1][n - 1]
        q, r = np.linalg.qr(A - diagonal_value * np.identity(n))
        A = np.matmul(r, q) + diagonal_value * np.identity(n)
        print(A)

    return np.diagonal(A)


A = np.array([[0.5, 0.5, 0.5, 0.5],
              [0.5, 0.5, -0.5, -0.5],
              [0.5, -0.5, 0.5, -0.5],
              [0.5, -0.5, -0.5, 0.5]])

# print(get_eigen_values(A))
print(get_eigen_values_offset(A, 4))
