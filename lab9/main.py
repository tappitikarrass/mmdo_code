from time import sleep
from sympy import diff, symbols, Poly
from simplex import simplex_solve
from beta import golden
import numpy as np
import math

x1, x2, alpha = symbols("x1 x2 alpha")


def function():
    return x1**2 + 2 * x2**2 - 3 * x1 - 8 * x2


def gradient():
    return [diff(function(), x1), diff(function(), x2)]


def equation(X0, Y0, b, grad_vec):
    return X0 + b * grad_vec[0], Y0 + b * grad_vec[1]


# Finding the beta from the 7 lab (with the golden section method)
def beta_golden(x, y, eps):
    return golden(0, 1, eps, function().subs(x1, x).subs(x2, y))


def use_simplex(expr, A, B):
    a = Poly(expr)
    dict_ = a.as_expr().as_coefficients_dict()
    list_ = [0] * 2
    for i in dict_.keys():
        if str(i) == str(x1):
            list_[0] = dict_[i]
        elif str(i) == str(x2):
            list_[1] = dict_[i]
    res = simplex_solve(A, B, list_)
    return res.x


def cgm(x0, eps, A, B):
    cnt = 0
    y0 = [math.inf, math.inf]
    while pow((pow(y0[0] - x0[0], 2) + pow(y0[1] - x0[1], 2)), 0.5) > eps:
        cnt += 1
        y0 = x0.copy()
        # 1.) Find ∇X(x)
        grad = [
            gradient()[0].subs([(x1, x0[0]), (x2, x0[1])]),
            gradient()[1].subs([(x1, x0[0]), (x2, x0[1])]),
        ]
        print(f"iteration {cnt} :")
        print(f"∇X(x{cnt - 1}) = {grad}")
        # 2.) Find x - x0
        delta_X_x0 = np.array([x1 - x0[0], x2 - x0[1]])
        # 3.) Find X0(x)
        X_x0 = delta_X_x0[0] * grad[0] + delta_X_x0[1] * grad[1]
        # 4.) Using the simplex method
        x, y = use_simplex(X_x0, A, B)
        # 5.) h(k) = y(k) - x(k)
        h = [x - x0[0], y - x0[1]]
        # 6.) Find the minimum of beta : b = argmin(X(x0 + b*h0))
        X, Y = equation(x0[0], x0[1], alpha, h)
        beta_min = beta_golden(X, Y, eps)
        x0[0] += beta_min * h[0]
        x0[1] += beta_min * h[1]
        print(f"X{cnt - 1} = ({2 * x0[0]}, {2 * x0[1]})")
        print("f(x1, x2) :", 2 * function().subs(x1, x0[0]).subs(x2, x0[1]))
        print("\n")
        sleep(0.3)

def main():
    print("\n << The Conditional Gradient Method >> \n")
    print("∇X(x0) = ", gradient(), "\n")
    eps = 0.001
    # A = [[-2, -1], [2, 3]]
    # B = [-8, 20]
    # X0 = np.array([3.0, 2.0])
    A = [[2, 1], [1, 5]]
    B = [16, 20]
    X0 = np.array([4.0, 3.0])
    cgm(X0, eps, A, B)


if __name__ == "__main__":
    main()
