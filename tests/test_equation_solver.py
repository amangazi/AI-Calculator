
import pytest
import sympy as sp

from modules.equation_solver import solve_equation


def test_solve_quadratic_equation():
    x = sp.Symbol("x")

    result = solve_equation(x**2 - 9, x)

    assert result == [-3, 3]


def test_reject_invalid_expression_type():
    x = sp.Symbol("x")

    with pytest.raises(TypeError):
        solve_equation("x**2 - 9", x)


def test_reject_invalid_variable_type():
    x = sp.Symbol("x")

    with pytest.raises(TypeError):
        solve_equation(x**2 - 9, "x")


def test_reject_variable_not_in_expression():
    x = sp.Symbol("x")
    y = sp.Symbol("y")

    with pytest.raises(ValueError):
        solve_equation(y**2 - 9, x)
