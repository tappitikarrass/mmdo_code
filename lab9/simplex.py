from scipy.optimize import linprog

def simplex_solve(A, B, C):
    return linprog(C, A_ub=A, b_ub=B)