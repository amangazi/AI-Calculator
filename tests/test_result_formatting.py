
import sympy as sp

from modules.output_formatter import format_result


def test_format_python_integer():
    result = format_result(42)
    assert result == "Result: 42"


def test_format_python_float():
    result = format_result(3.14)
    assert result == "Result: 3.14"


def test_format_string():
    result = format_result("Calculation complete")
    assert result == "Result: Calculation complete"


def test_format_sympy_integer():
    result = format_result(sp.Integer(42))
    assert result == "Result: 42"


def test_format_exact_sympy_number():
    result = format_result(sp.sqrt(2))

    assert result == (
        "Exact result: sqrt(2)\n"
        "Numerical approximation: 1.41421356237310"
    )


def test_format_sympy_expression():
    x = sp.Symbol("x")

    result = format_result(x**2 + 2*x + 1)

    assert result == "Result: x**2 + 2*x + 1"


def test_format_equation_solutions():
    result = format_result([-3, 3])

    assert result == "Results: [-3, 3]"
