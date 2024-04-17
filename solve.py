import numpy as np
from scipy import integrate


def e(i, h):
    return lambda x: (x / h - i + 1) if h * (i - 1) <= x < h * i else (-x / h + i + 1) if h * i <= x < h * (i + 1) else 0


def e_prim(i, h):
    return lambda x: 1 / h if h * (i - 1) <= x < h * i else -1 / h if h * i <= x < h * (i + 1) else 0


def B(i, j, h, s, z):
    f = lambda x: e_prim(i, h)(x) * e_prim(j, h)(x)
    if z <= 1:
        return 2 * integrate.quad(f, s, z)[0] - 2 * e(i, h)(0) * e(j, h)(0)

    elif s >= 1:
        return 6 * integrate.quad(f, s, z)[0] - 2 * e(i, h)(0) * e(j, h)(0)

    else:
        return 2 * integrate.quad(f, s, 1)[0] + 6 * integrate.quad(f, 1, z)[0] - 2 * e(i, h)(0) * e(j, h)(0)


def L(i, h):
    return -14 * e(i, h)(0)


def create_A(elem_num, h):
    matrix = []
    for i in range(0, elem_num - 1):
        row = []
        for j in range(0, elem_num - 1):
            if i == 0 or j == 0:
                row.append(B(i, j, h, 0, (i + 1) * h))

            else:
                row.append(B(i, j, h, (i - 1) * h, (i + 1) * h))
        matrix.append(row)
    return matrix


def create_X(elem_num, h):
    matrix = []
    for i in range(0, elem_num - 1):
        matrix.append(L(i, h))
    return matrix

def solve(n):
    h = 2 / (n - 1)

    A = np.array(create_A(n, h))
    X = np.array(create_X(n, h))

    W = np.linalg.solve(A, X)

    x = np.linspace(0, 2, num=n)

    for i in range(len(W)):
        W[i] += 3

    y = np.concatenate((W, [3]))

    return x, y
