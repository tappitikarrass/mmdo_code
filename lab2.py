import numpy as np
from scipy.optimize import linprog

A = np.array([[-1, 1], [-1, 3], [1, 1]])
b = np.array([5, 19, 11])

# так як цільова функція має додаткову константу 1
# потрібно перетворити її: відняти 0,5 від кожного коефіцієнта
# та відняти 1 від результату X(x_mix)
c = np.array([0.5, -2.5])

ans = linprog(c, A_ub=A, b_ub=b, method="simplex")
print("X(x_min) =", ans.fun-1,
        "\nx_min =", ans.x,
        "\nstatus =", ans.message)
