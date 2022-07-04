import numpy as np


def func(f_, matrix):
    size = len(f_)
    print()
    for i in range(size):
        f_[i][0] = np.amax(matrix[i])
        index = np.where(matrix[i] == np.amax(matrix[i]))
        f_[i][1] = index[0][0]
        print(f"f'({i}) = {f_[i][1]}")

def D(table, iter, k):
    lst_ = [0]
    for i in table[iter - 1]:
        if i[0] == k:
            lst_.append(i[1])
    return max(lst_)


def method(table, invest):
    iter = len(table)
    inv = invest
    matrix = np.array([[0] * (invest + 1) for i in range(invest + 1)], dtype=float)
    f_ = np.array(
        [[[0, 0] for i in range(invest + 1)] for j in range(iter + 1)], dtype=float
    )
    path = []
    while iter > 0:
        print(f"\nstep {iter}")
        for x in range(invest + 1):
            for k in range(invest + 1):
                if k <= x:
                    matrix[x][k] = D(table, iter, k) + f_[iter][x - k][0]
                    print(round(matrix[x][k],2), end=" | ")
            print()
        func(f_[iter - 1], matrix)
        iter -= 1
    f_ = np.delete(f_, -1, axis=0)
    for i in range(len(f_)):
        t = f_[i][inv][1]
        path.append((i + 1, t))
        inv -= int(t)
    return path, np.amax(matrix[-1])
