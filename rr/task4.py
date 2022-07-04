from pulp import *

A = [[1, 1, 1], [3, 2, 3]]
b = [7, 10]
c = [24, 20, 35]

# A = [[1, 1, 1], [3, 2, 3]]
# b = [7, 6]
# c = [24, 20, 35]

# A = [[1, 1, 1], [3, 2, 4]]
# b = [5, 15]
# c = [25, 20, 35]

problem = LpProblem("problem", LpMaximize)

x1 = LpVariable("x1", lowBound=0, cat=LpInteger)
x2 = LpVariable("x2", lowBound=0, cat=LpInteger)
x3 = LpVariable("x3", lowBound=0, cat=LpInteger)

problem += c[0] * x1 + c[1] * x2 + c[2] * x3, "Objective Function"
problem += A[0][0] * x1 + A[0][1] * x2 + A[0][2] * x3 <= b[0], "1st Constraint"
problem += A[1][0] * x1 + A[1][1] * x2 + A[1][2] * x3 <= b[1], "2nd Constraint"

problem += x1 >=0, "x1positive Constraint"
problem += x2 >=0, "x2positive Constraint"
problem += x3 >=0, "x3positive Constraint"

problem.solve()
print("x1: ", x1.varValue)
print("x2:", x2.varValue)
print("x3:", x2.varValue)
print("Z: ", value(problem.objective))

# problem += 24 * x1 + 20 * x2 + 35 * x3, "Objective Function"
# problem += x1 + x2 + x3 <= 7, "a Constraint"
# problem += 3 * x1 + 2 * x2 + 3 * x3 <= 10, "b Constraint"