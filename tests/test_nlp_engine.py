
from modules.nlp_engine import identify_operation, extract_expression


def test_identify_tangent():
    result = identify_operation("calculate tangent of 45")
    assert result == "tan"


def test_extract_expression_without_operation():
    result = extract_expression("hello there")
    assert result is None


def test_extract_derivative_from_calculate_request():
    result = extract_expression(
        "Calculate the derivative of x**2"
    )
    assert result == "x**2"


def test_extract_derivative_from_direct_request():
    result = extract_expression(
        "Differentiate x**3 + 2*x"
    )
    assert result == "x**3 + 2*x"


def test_extract_incomplete_derivative_request():
    result = extract_expression("Differentiate")
    assert result == ""


def test_extract_logarithm_from_find_request():
    result = extract_expression("Find logarithm of 100")
    assert result == "100"


def test_extract_derivative_from_please_find_request():
    result = extract_expression(
        "Please find the derivative of x**2"
    )
    assert result == "x**2"


def test_extract_sum_operands():
    result = extract_expression(
        "What is the sum of 10 and 20"
    )
    assert result == "10 and 20"


def test_extract_product_operands():
    result = extract_expression(
        "What is the product of 4 and 5"
    )
    assert result == "4 and 5"
