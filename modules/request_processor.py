
import sympy as sp

from modules.nlp_engine import identify_operation, extract_expression
from modules.expression_parser import parse_expression
from modules.output_formatter import format_result

from modules.explanation import (
    explain_differentiation,
    explain_integration
)

from modules.calculator import (
    add,
    subtract,
    multiply,
    divide,
    expand_expression,
    factor_expression,
    differentiate_expression,
    integrate_expression,
    calculate_sin,
    calculate_cos,
    calculate_tan,
    calculate_log,
    calculate_sqrt,
    calculate_exp
)

from modules.equation_solver import solve_equation


def create_response(
    success,
    operation=None,
    result=None,
    explanation=None,
    error=None
):
    """Create a consistent structured response."""

    return {
        "success": success,
        "operation": operation,
        "result": result,
        "explanation": explanation or [],
        "error": error
    }


def parse_request_expression(expression_text, operation):

    # Handle equations such as x**2 = 4.
    if operation == "solve" and "=" in expression_text:

        if expression_text.count("=") != 1:
            raise ValueError("Invalid equation.")

        left_text, right_text = expression_text.split("=")

        if not left_text.strip() or not right_text.strip():
            raise ValueError("Incomplete equation.")

        left_side = parse_expression(left_text)
        right_side = parse_expression(right_text)

        return left_side - right_side

    return parse_expression(expression_text)


def parse_arithmetic_operands(expression_text, operation):
    """Extract and safely parse two arithmetic operands."""

    separators = {
        "add": " and ",
        "subtract": " from ",
        "multiply": " and ",
        "divide": " by "
    }

    separator = separators[operation]

    if expression_text.count(separator) != 1:
        raise ValueError("Invalid arithmetic expression.")

    first_text, second_text = expression_text.split(separator)

    if not first_text.strip() or not second_text.strip():
        raise ValueError("Incomplete arithmetic expression.")

    first = parse_expression(first_text)
    second = parse_expression(second_text)

    return first, second


def identify_variable(expression):

    symbols = sorted(
        expression.free_symbols,
        key=lambda symbol: symbol.name
    )

    if not symbols:
        return sp.Symbol("x")

    # Prefer x when multiple variables are present.
    if sp.Symbol("x") in symbols:
        return sp.Symbol("x")

    # Use the variable if only one exists.
    if len(symbols) == 1:
        return symbols[0]

    return None


def process_request(user_input):

    if not isinstance(user_input, str) or not user_input.strip():
        return create_response(
            success=False,
            error="Please enter a mathematical request."
        )

    operation = identify_operation(user_input)

    if operation is None:
        return create_response(
            success=False,
            error="Sorry, I could not identify the mathematical operation."
        )

    expression_text = extract_expression(user_input)

    # Check for an empty extracted expression.
    if not expression_text or not expression_text.strip():
        return create_response(
            success=False,
            operation=operation,
            error="Please provide a mathematical expression."
        )

    try:

        # Parse arithmetic operands separately.
        if operation in ("add", "subtract", "multiply", "divide"):

            first, second = parse_arithmetic_operands(
                expression_text,
                operation
            )

            expression = None

        else:

            expression = parse_request_expression(
                expression_text,
                operation
            )

    except ZeroDivisionError:

        return create_response(
            success=False,
            operation=operation,
            error="Division by zero is not allowed."
        )

    except (ValueError, TypeError, SyntaxError):

        return create_response(
            success=False,
            operation=operation,
            error="Invalid mathematical expression."
        )

    # Identify the variable only for symbolic expressions.
    variable = None

    if expression is not None:
        variable = identify_variable(expression)

    if variable is None and operation in (
        "differentiate",
        "integrate",
        "solve"
    ):

        return create_response(
            success=False,
            operation=operation,
            error="Please specify which variable to use."
        )

    try:

        # Perform the requested mathematical operation.

        if operation == "add":
            result = add(first, second)

        elif operation == "subtract":
            # "Subtract 3 from 10" means 10 - 3.
            result = subtract(second, first)

        elif operation == "multiply":
            result = multiply(first, second)

        elif operation == "divide":
            result = divide(first, second)

        elif operation == "evaluate":
            result = expression

        elif operation == "expand":
            result = expand_expression(expression)

        elif operation == "factor":
            result = factor_expression(expression)

        elif operation == "differentiate":
            result = differentiate_expression(
                expression,
                variable
            )

        elif operation == "integrate":
            result = integrate_expression(
                expression,
                variable
            )

        elif operation == "solve":
            result = solve_equation(
                expression,
                variable
            )

        elif operation == "sin":
            result = calculate_sin(expression)

        elif operation == "cos":
            result = calculate_cos(expression)

        elif operation == "tan":
            result = calculate_tan(expression)

        elif operation == "log":
            result = calculate_log(expression)

        elif operation == "sqrt":
            result = calculate_sqrt(expression)

        elif operation == "exp":
            result = calculate_exp(expression)

        else:

            return create_response(
                success=False,
                operation=operation,
                error="Unsupported mathematical operation."
            )

        # Format the mathematical result.
        formatted_result = format_result(result)

        # Add the integration constant for indefinite integrals.
        if operation == "integrate":
            formatted_result += " + C"

        # Generate operation-specific explanations.
        explanation_steps = []

        if operation == "differentiate":
            explanation_steps = explain_differentiation(
                expression,
                variable
            )

        elif operation == "integrate":
            explanation_steps = explain_integration(
                expression,
                variable
            )

        return create_response(
            success=True,
            operation=operation,
            result=formatted_result,
            explanation=explanation_steps
        )

    except ZeroDivisionError:

        return create_response(
            success=False,
            operation=operation,
            error="Division by zero is not allowed."
        )

    except (
        ValueError,
        TypeError,
        NotImplementedError,
        RecursionError
    ):

        return create_response(
            success=False,
            operation=operation,
            error="Unable to complete the mathematical operation."
        )
