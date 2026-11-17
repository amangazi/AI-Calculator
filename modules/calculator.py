import sympy as sp


def expand_expression(expression):
    return sp.expand(expression)


def factor_expression(expression):
    return sp.factor(expression)


def differentiate_expression(expression, variable):
    return sp.diff(expression, variable)


def integrate_expression(expression, variable):
    return sp.integrate(expression, variable)


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")

    return a / b


def evaluate_expression(expression, variable, value):
    return expression.subs(variable, value)


def evaluate_numerically(expression, variable, values):
    numerical_function = sp.lambdify(
        variable,
        expression,
        modules="numpy"
    )

    return numerical_function(values)



def calculate_sin(expression):
    return sp.sin(expression)


def calculate_cos(expression):
    return sp.cos(expression)


def calculate_tan(expression):
    return sp.tan(expression)


def calculate_log(expression):
    return sp.log(expression)


def calculate_sqrt(expression):
    return sp.sqrt(expression)


def calculate_exp(expression):
    return sp.exp(expression)
