from grad import GradDescent

def main():
    coef= [4, 5, 3, -2, 2, -1, 0, -3, 1, 0]
    gd = GradDescent(coef, 10, 0.0005)

    
    min_x1, min_x2, min_x3, itr = gd.gradient_descent(0, 0, 0)
    func_min = sum(gd.coef[0][i] * min_x1 **
        gd.coef[1][i] * min_x2 **
            gd.coef[2][i] * min_x3 **
            gd.coef[3][i] for i in range(10))

    print(f"X1 = {min_x1};\nX2 = {min_x2};\nX3 = {min_x3};")
    print(f"F(X1, X2, X3) = {coef[0]}*X1^2 + {coef[1]}*X2^2 + {coef[2]}*X3^2 +" +
              f" {coef[3]}*X1*X2 + {coef[4]}*X1*X3 + {coef[5]}*X2*X3 +" +
              f" {coef[6]}*X1 + {coef[7]}*X2 + {coef[8]}*X3 + {coef[9]}")
    print("F(X1; X2; X3)", func_min)
    print("Iterations =", itr)

if __name__ == '__main__':
    main()
