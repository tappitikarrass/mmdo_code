from math import fabs

def fib(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def get_min_fib(c):
    n = 0
    while (fib(n) < c):
        n += 1
    return n

def f(x):
    return pow(x, 5) - 5 * pow(x, 3) + 10 * pow(x, 2) - 5 * x

def main():
    a, b, eps = -3, -2, 0.1
    vars = (b - a) / eps

    n = get_min_fib(vars)

    x1 = a + (fib(n - 2)/fib(n)) * (b - a)
    x2 = a + (fib(n - 1)/fib(n)) * (b - a)
    k = 0

    while True:
        if f(x1) <= f(x2):
            b = x2
            x2 = x1
            x1 = a + (fib(n - 3)/fib(n - 1)) * (b - a)
        else:
            a = x1
            x1 = x2
            x2 = a + (fib(n - 2)/fib(n - 1)) * (b - a)
        k += 1

        if fabs(b - a) < eps:
            break

    xmin = (a + b) / 2
    print("xmin \t=", xmin)
    print("f(xmin) =", f(xmin))

if __name__ == "__main__":
    main()
