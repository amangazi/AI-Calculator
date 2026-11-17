
import pytest
import sympy as sp
import numpy as np

from modules.calculator import (
    add,
    subtract,
    multiply,
    divide,
    evaluate_expression,
    evaluate_numerically,
    calculate_sin,
    calculate_cos,
    calculate_tan,
    calculate_log,
    calculate_sqrt,
    calculate_exp
)


def test_addition():
    assert add(10, 5) == 15


def test_subtraction():
    assert subtract(10, 5) == 5


def test_multiplication():
    assert multiply(10, 5) == 50


def test_division():
    assert divide(10, 5) == 2


def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)


def test_expression_substitution():
    x = sp.symbols("x")
    expression = x**2 + 1

    assert evaluate_expression(expression, x, 3) == 10


def test_numerical_evaluation():
    x = sp.symbols("x")
    expression = x**2

    values = np.array([1, 2, 3])

    result = evaluate_numerically(expression, x, values)

    assert np.array_equal(result, np.array([1, 4, 9]))


def test_sine():
    assert calculate_sin(sp.pi / 2) == 1


def test_cosine():
    assert calculate_cos(sp.pi) == -1


def test_tangent():
    assert calculate_tan(0) == 0


def test_logarithm():
    assert calculate_log(sp.E) == 1


def test_square_root():
    assert calculate_sqrt(9) == 3


def test_exponential():
    assert calculate_exp(0) == 1
