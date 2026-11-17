
import sympy as sp


def solve_equation(expression, variable):

    if not isinstance(expression, sp.Basic):
        raise TypeError("Expression must be a valid SymPy expression.")

    if not isinstance(variable, sp.Symbol):
        raise TypeError("Variable must be a valid SymPy symbol.")

    if variable not in expression.free_symbols:
        raise ValueError(
            f"The variable '{variable}' does not appear in the equation."
        )

    solutions = sp.solve(expression, variable)

    return solutions
