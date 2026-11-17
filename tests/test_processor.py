
import sympy as sp

from modules.request_processor import (
    process_request,
    parse_request_expression,
    identify_variable
)


# ==========================================
# Original request-processing tests
# ==========================================

def test_differentiation():
    result = process_request("differentiate x**3 + 2*x")

    assert result["success"] is True
    assert result["operation"] == "differentiate"
    assert result["result"] == "Result: 3*x**2 + 2"
    assert len(result["explanation"]) > 0


def test_factorisation():
    result = process_request("factorise x**2 + 5*x + 6")

    assert result["success"] is True
    assert result["operation"] == "factor"
    assert result["result"] == "Result: (x + 2)*(x + 3)"


def test_expansion():
    result = process_request("expand (x + 2)*(x + 3)")

    assert result["success"] is True
    assert result["operation"] == "expand"
    assert result["result"] == "Result: x**2 + 5*x + 6"


def test_division_by_zero():
    result = process_request("calculate 10/0")

    assert result["success"] is False
    assert result["error"] == "Division by zero is not allowed."


def test_integration():
    result = process_request("find the integral of sin(x)")

    assert result["success"] is True
    assert result["operation"] == "integrate"
    assert result["result"] == "Result: -cos(x)"


def test_equation_solving():
    result = process_request("find roots of x**2 - 9")

    assert result["success"] is True
    assert result["operation"] == "solve"
    assert result["result"] == "Results: [-3, 3]"


def test_square_root():
    result = process_request("calculate square root of 144")

    assert result["success"] is True
    assert result["operation"] == "sqrt"
    assert result["result"] == "Result: 12"


def test_arithmetic():
    result = process_request("calculate 25 + 17")

    assert result["success"] is True
    assert result["operation"] == "evaluate"
    assert result["result"] == "Result: 42"


def test_invalid_expression():
    result = process_request("expand x +")

    assert result["success"] is False
    assert result["error"] == "Invalid mathematical expression."


def test_unsupported_function():
    result = process_request("solve unknown_function(x)")

    assert result["success"] is False
    assert result["error"] == "Invalid mathematical expression."


def test_unrecognized_request():
    result = process_request("hello there")

    assert result["success"] is False
    assert result["operation"] is None
    assert result["error"] == (
        "Sorry, I could not identify the mathematical operation."
    )


def test_tangent():
    result = process_request("calculate tangent of pi/4")

    assert result["success"] is True
    assert result["operation"] == "tan"
    assert result["result"] == "Result: 1"


def test_unsupported_operation(monkeypatch):
    import modules.request_processor as processor

    monkeypatch.setattr(
        processor,
        "identify_operation",
        lambda user_input: "unsupported"
    )

    result = processor.process_request("calculate 2 + 2")

    assert result["success"] is False
    assert result["operation"] == "unsupported"
    assert result["error"] == "Unsupported mathematical operation."


def test_operation_exception(monkeypatch):
    import modules.request_processor as processor

    def simulate_calculation_failure(expression):
        raise NotImplementedError("Simulated calculation failure")

    monkeypatch.setattr(
        processor,
        "calculate_tan",
        simulate_calculation_failure
    )

    result = processor.process_request("calculate tangent of pi/4")

    assert result["success"] is False
    assert result["operation"] == "tan"
    assert result["error"] == (
        "Unable to complete the mathematical operation."
    )


# ==========================================
# Equation parsing tests
# ==========================================

def test_parse_valid_equation():
    result = parse_request_expression("x**2 = 4", "solve")

    expected = sp.Symbol("x")**2 - 4

    assert sp.expand(result - expected) == 0


def test_parse_equation_with_multiple_equals():
    try:
        parse_request_expression("x = 2 = 3", "solve")
        assert False, "Expected ValueError"
    except ValueError:
        pass


def test_parse_equation_with_empty_left_side():
    try:
        parse_request_expression("= 4", "solve")
        assert False, "Expected ValueError"
    except ValueError:
        pass


def test_parse_equation_with_empty_right_side():
    try:
        parse_request_expression("x**2 =", "solve")
        assert False, "Expected ValueError"
    except ValueError:
        pass


def test_parse_regular_expression():
    result = parse_request_expression("x**2 + 2*x", "expand")

    expected = sp.Symbol("x")**2 + 2*sp.Symbol("x")

    assert result == expected


# ==========================================
# Variable identification tests
# ==========================================

def test_identify_variable_without_symbols():
    result = identify_variable(sp.Integer(25))

    assert result == sp.Symbol("x")


def test_identify_single_variable():
    result = identify_variable(sp.Symbol("y")**2)

    assert result == sp.Symbol("y")


def test_identify_x_when_multiple_variables_exist():
    result = identify_variable(
        sp.Symbol("x") + sp.Symbol("y")
    )

    assert result == sp.Symbol("x")


def test_identify_variable_with_multiple_non_x_symbols():
    result = identify_variable(
        sp.Symbol("y") + sp.Symbol("z")
    )

    assert result is None


def test_differentiation_with_ambiguous_variable():
    result = process_request("differentiate y + z")

    assert result["success"] is False
    assert result["error"] == (
        "Please specify which variable to use."
    )


# ==========================================
# Explanation error handling
# ==========================================

def test_explanation_exception(monkeypatch):
    import modules.request_processor as processor

    def simulate_explanation_failure(expression, variable):
        raise NotImplementedError("Simulated explanation failure")

    monkeypatch.setattr(
        processor,
        "explain_differentiation",
        simulate_explanation_failure
    )

    result = processor.process_request("differentiate x**2")

    assert result["success"] is False
    assert result["error"] == (
        "Unable to complete the mathematical operation."
    )




# ==========================================
# Natural-language arithmetic tests
# ==========================================

def test_addition():
    result = process_request("add 2 and 3")

    assert result["success"] is True
    assert result["operation"] == "add"
    assert result["result"] == "Result: 5"


def test_subtraction():
    result = process_request("subtract 3 from 10")

    assert result["success"] is True
    assert result["operation"] == "subtract"
    assert result["result"] == "Result: 7"


def test_multiplication():
    result = process_request("multiply 4 and 5")

    assert result["success"] is True
    assert result["operation"] == "multiply"
    assert result["result"] == "Result: 20"


def test_division():
    result = process_request("divide 20 by 4")

    assert result["success"] is True
    assert result["operation"] == "divide"
    assert result["result"] == "Result: 5"