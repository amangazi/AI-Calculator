import sympy as sp


def solve_equation(expression, variable):
    solutions = sp.solve(expression, variable)
    return solutions