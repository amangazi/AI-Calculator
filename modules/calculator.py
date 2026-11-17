
import numpy as np
import sympy as sp


# ==========================================
# Symbolic expression operations
# ==========================================

def expand_expression(expression):
    return sp.expand(expression)


def factor_expression(expression):
    return sp.factor(expression)


def differentiate_expression(expression, variable):
    return sp.diff(expression, variable)


def integrate_expression(expression, variable):
    return sp.integrate(expression, variable)


# ==========================================
# Basic arithmetic operations
# ==========================================

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0 or getattr(b, "is_zero", None) is True:
        raise ZeroDivisionError("Cannot divide by zero.")

    return a / b


# ==========================================
# Expression evaluation
# ==========================================

def evaluate_expression(expression, variable, value):
    return expression.subs(variable, value)


def evaluate_numerically(expression, variable, values):
    numerical_function = sp.lambdify(
        variable,
        expression,
        modules="numpy"
    )

    result = numerical_function(values)

    if not np.all(np.isfinite(result)):
        raise ValueError(
            "Numerical evaluation produced a non-finite result."
        )

    return result


# ==========================================
# Mathematical functions
# ==========================================

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
