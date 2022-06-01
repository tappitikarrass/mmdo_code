#!/bin/env python3
import numpy as np
import math

class LinearModel:
    def __init__(self,
                 A = np.empty([0,0]),
                 b = np.empty([0,0]),
                 c = np.empty([0,0]),
                 minmax = "MAX"):
        self.A = A
        self.b = b
        self.c = c
        self.x = [float(0)] * len(c)
        self.minmax = minmax
        self.printIter = True
        self.optimalValue = None
        self.transform = False
        
    def addA(self, A):
        self.A = A
        
    def addB(self, b):
        self.b = b
        
    def addC(self, c):
        self.c = c
        self.transform = False
    
    def setObj(self, minmax):
        if(minmax == "MIN" or minmax == "MAX"):
            self.minmax = minmax
        else:
            print("Invalid objective.")
        self.transform = False
            
    def setPrintIter(self, printIter):
        self.printIter = printIter
            
    def printSoln(self):
        print("Coef: ")
        print(self.x)
        print("Result: ")
        print(self.optimalValue)
        
    def printTableau(self, tableau):
        
        print("ind \t\t", end = "")
        for j in range(0, len(c)):
            print("x_" + str(j), end = "\t")
        for j in range(0, (len(tableau[0]) - len(c) - 2)):
            print("s_" + str(j), end = "\t")
        
        print()
        for j in range(0, len(tableau)):
            for i in range(0, len(tableau[0])):
                if(not np.isnan(tableau[j, i])):
                    if(i == 0):
                        print(int(tableau[j, i]), end = "\t")
                    else:
                        print(round(tableau[j, i], 2), end = "\t")
                else:
                    print(end = "\t")
            print()
            
    def getTableau(self):
        if(self.minmax == "MIN" and self.transform == False):
            self.c[0:len(c)] = -1 * self.c[0:len(c)]
            self.transform = True
        
        t1 = np.array([None, 0])
        numVar = len(self.c)
        numSlack = len(self.A)
        
        t1 = np.hstack(([None], [0], self.c, [0] * numSlack))
        
        basis = np.array([0] * numSlack)
        
        for i in range(0, len(basis)):
            basis[i] = numVar + i
        
        A = self.A
        
        if(not ((numSlack + numVar) == len(self.A[0]))):
            B = np.identity(numSlack)
            A = np.hstack((self.A, B))
            
        t2 = np.hstack((np.transpose([basis]), np.transpose([self.b]), A))
        
        tableau = np.vstack((t1, t2))
        
        tableau = np.array(tableau, dtype ='float')
        
        return tableau
            
    def optimize(self):
        
        if(self.minmax == "MIN" and self.transform == False):
            for i in range(len(self.c)):
                self.c[i] = -1 * self.c[i]
                transform = True
        
        tableau = self.getTableau()
         
        if(self.printIter == True):
            print("Starting Tableau:")
            self.printTableau(tableau)
        
        optimal = False
        iter = 1

        while(True):
            
            if(self.printIter == True):
                print("----------------------------------")
                print("Iteration :", iter)
                self.printTableau(tableau)
                
            if(self.minmax == "MAX"):
                for profit in tableau[0, 2:]:
                    if profit > 0:
                        optimal = False
                        break
                    optimal = True
            else:
                for cost in tableau[0, 2:]:
                    if cost < 0:
                        optimal = False
                        break
                    optimal = True

            if optimal == True: 
                 break
            
            if (self.minmax == "MAX"):
                n = tableau[0, 2:].tolist().index(np.amax(tableau[0, 2:])) + 2
            else:
                n = tableau[0, 2:].tolist().index(np.amin(tableau[0, 2:])) + 2

            minimum = 99999
            r = -1

            for i in range(1, len(tableau)): 
                if(tableau[i, n] > 0):
                    val = tableau[i, 1]/tableau[i, n]
                    if val<minimum: 
                        minimum = val 
                        r = i
                            
            pivot = tableau[r, n] 
            
            print("Pivot Column:", n)
            print("Pivot Row:", r)
            print("Pivot Element: ", pivot)

            tableau[r, 1:] = tableau[r, 1:] / pivot 
            
            for i in range(0, len(tableau)): 
                if i != r:
                    mult = tableau[i, n] / tableau[r, n]
                    tableau[i, 1:] = tableau[i, 1:] - mult * tableau[r, 1:] 

            tableau[r, 0] = n - 2
            
            iter += 1
            
        
        if(self.printIter == True):
            print("----------------------------------")
            print("Final Tableau reached in", iter, "iterations")
            self.printTableau(tableau)
        else:
            print("Solved")
            
        self.x = np.array([0] * len(c), dtype = float)
        # save coefficients
        for key in range(1, (len(tableau))):
            if(tableau[key, 0] < len(c)):
                self.x[int(tableau[key, 0])] = tableau[key, 1]
        
        self.optimalValue = -1 * tableau[0,1]

if __name__ == "__main__":
    np.seterr(all='raise')
    # example 1
    model1 = LinearModel(minmax="MAX")
    A = np.array([[2, 11],
                 [1, 1],
                 [4, -5]])
    b = np.array([38, 7, 5])
    c = np.array([1, 1])
    # example 2
    model1 = LinearModel(minmax="MIN")
    A = np.array([[-1, -2],
                  [-3, -1],
                  [-1, 0],
                  [0, -1]])
    b = np.array([-10, -10, 0, 0])
    c = np.array([2, -3])

    model1.addA(A)
    model1.addB(b)
    model1.addC(c)

    try:
        model1.optimize()
    except Exception:
        print("No optimal solution")
        exit(0)
    print("\n")
    model1.printSoln()
