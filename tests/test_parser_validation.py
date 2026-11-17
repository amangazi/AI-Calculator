
import pytest
import sympy as sp

import modules.expression_parser as expression_parser
from modules.expression_parser import parse_expression


@pytest.mark.parametrize(
    "expression",
    [
        "True",
        "'hello'",
        "unknown_variable",
        "x @ 2",
        "~x",
        "x.sin()",
        "unknown_function(x)",
        "sin(x, y)",
        "sin(x=2)",
        "x > 2",
        "1e309"
    ]
)
def test_invalid_expressions(expression):
    with pytest.raises((ValueError, ZeroDivisionError)):
        parse_expression(expression)


def test_non_string_input():
    with pytest.raises(ValueError):
        parse_expression(123)


def test_empty_expression():
    with pytest.raises(ValueError):
        parse_expression("")


def test_expression_too_long():
    with pytest.raises(ValueError):
        parse_expression("x" * 201)


def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        parse_expression("10/0")


def test_unsupported_unary_operator():
    with pytest.raises(ValueError, match="Unsupported unary operator"):
        parse_expression("~x")


def test_invalid_mathematical_syntax():
    with pytest.raises(ValueError, match="Invalid mathematical syntax"):
        parse_expression("x +")


def test_unary_plus():
    result = parse_expression("+5")
    assert result == 5


def test_unary_minus():
    result = parse_expression("-5")
    assert result == -5


def test_expression_exceeds_node_limit():

    def build_balanced_expression(count):
        if count == 1:
            return "x"

        left_count = count // 2
        right_count = count - left_count

        left = build_balanced_expression(left_count)
        right = build_balanced_expression(right_count)

        if left_count > 1:
            left = f"({left})"

        if right_count > 1:
            right = f"({right})"

        return f"{left}+{right}"

    expression = build_balanced_expression(51)

    with pytest.raises(ValueError, match="Expression is too complex"):
        parse_expression(expression)


def test_expression_exceeds_depth_limit():
    expression = "x"

    for _ in range(25):
        expression = f"sin({expression})"

    with pytest.raises(ValueError, match="Expression nesting is too deep"):
        parse_expression(expression)


def test_recursion_error_during_ast_traversal(monkeypatch):

    def simulate_recursion_error(node):
        raise RecursionError

    monkeypatch.setattr(
        expression_parser.ast,
        "iter_child_nodes",
        simulate_recursion_error
    )

    with pytest.raises(
        ValueError,
        match="Expression nesting is too deep"
    ):
        parse_expression("x")


@pytest.mark.parametrize(
    "expression",
    [
        "x**1001",
        "x**-1001"
    ]
)
def test_exponent_exceeds_limit(expression):
    with pytest.raises(
        ValueError,
        match="Exponent magnitude is too large"
    ):
        parse_expression(expression)


@pytest.mark.parametrize(
    "expression",
    [
        "x**1000",
        "x**-1000"
    ]
)
def test_exponent_at_limit_is_accepted(expression):
    x = sp.Symbol("x")

    result = parse_expression(expression)

    expected = x**1000 if expression == "x**1000" else x**-1000

    assert result == expected


def test_non_real_exponent_is_rejected():
    with pytest.raises(
        ValueError,
        match="Exponent must be a real number"
    ):
        parse_expression("x**sqrt(-1)")


def test_large_integer_result_is_rejected():
    expression = (
        "99999999999999999999999999999999999999999999999999**1000"
    )

    with pytest.raises(
        ValueError,
        match="Numerical result is too large"
    ):
        parse_expression(expression)


def test_integer_result_within_bit_limit_is_accepted():
    result = parse_expression("2**100")
    assert result == 2**100


def test_negative_integer_exponent_is_accepted():
    result = parse_expression("2**-10")
    assert result == sp.Rational(1, 1024)
