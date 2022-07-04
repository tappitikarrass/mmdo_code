from sympy import symbols

x1, x2, alpha = symbols('x1, x2, alpha')

def golden(a, b, eps, f):
    C = 1.6180339887498949

    l = b - a
    x1 = b - l / C
    x2 = a + l / C

    while abs(b - a) > eps:
        if f.subs(alpha, x1) < f.subs(alpha, x2):
            b = x2
        else:
            a = x1
        l = b - a
        x1 = b - l / C
        x2 = a + l / C
    
    return (b + a) / 2