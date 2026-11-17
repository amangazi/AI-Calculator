
import ast
import math
import sympy as sp


# ==========================================
# Supported mathematical elements
# ==========================================

ALLOWED_SYMBOLS = {
    "x": sp.Symbol("x"),
    "y": sp.Symbol("y"),
    "z": sp.Symbol("z")
}


ALLOWED_CONSTANTS = {
    "pi": sp.pi,
    "E": sp.E
}


ALLOWED_FUNCTIONS = {
    "sin": sp.sin,
    "cos": sp.cos,
    "tan": sp.tan,
    "log": sp.log,
    "sqrt": sp.sqrt,
    "exp": sp.exp
}


# ==========================================
# Security and complexity limits
# ==========================================

MAX_AST_NODES = 100
MAX_AST_DEPTH = 20

MAX_EXPONENT = 1000
MAX_NUMERIC_BITS = 100000
MAX_EXPRESSION_LENGTH = 200


# ==========================================
# Numerical result validation
# ==========================================

def validate_numeric_result(result):
    """Validate numerical results before returning them."""

    if result.is_Integer:
        result_bits = abs(int(result)).bit_length()

        if result_bits > MAX_NUMERIC_BITS:
            raise ValueError("Numerical result is too large.")

    if result.is_Float and not math.isfinite(float(result)):
        raise ValueError("Invalid numerical result.")

    return result


# ==========================================
# AST complexity validation
# ==========================================

def validate_ast_complexity(syntax_tree):
    """Limit the number and depth of AST nodes."""

    node_count = 0

    def traverse(node, depth):

        nonlocal node_count

        node_count += 1

        if node_count > MAX_AST_NODES:
            raise ValueError("Expression is too complex.")

        if depth > MAX_AST_DEPTH:
            raise ValueError("Expression nesting is too deep.")

        for child in ast.iter_child_nodes(node):
            traverse(child, depth + 1)

    try:
        traverse(syntax_tree, 1)

    except RecursionError:
        raise ValueError("Expression nesting is too deep.") from None


# ==========================================
# AST expression evaluation
# ==========================================

def evaluate_node(node):

    # Handle numerical constants.
    if isinstance(node, ast.Constant):

        if isinstance(node.value, bool):
            raise ValueError("Boolean values are not allowed.")

        if isinstance(node.value, (int, float)):

            if (
                isinstance(node.value, float)
                and not math.isfinite(node.value)
            ):
                raise ValueError("Invalid numerical value.")

            return validate_numeric_result(sp.sympify(node.value))

        raise ValueError("Unsupported constant.")

    # Handle variables and mathematical constants.
    elif isinstance(node, ast.Name):

        if node.id in ALLOWED_SYMBOLS:
            return ALLOWED_SYMBOLS[node.id]

        if node.id in ALLOWED_CONSTANTS:
            return ALLOWED_CONSTANTS[node.id]

        raise ValueError(f"Unsupported name: {node.id}")

    # Handle arithmetic operators.
    elif isinstance(node, ast.BinOp):

        left = evaluate_node(node.left)
        right = evaluate_node(node.right)

        if isinstance(node.op, ast.Add):
            return validate_numeric_result(left + right)

        elif isinstance(node.op, ast.Sub):
            return validate_numeric_result(left - right)

        elif isinstance(node.op, ast.Mult):
            return validate_numeric_result(left * right)

        elif isinstance(node.op, ast.Div):

            if right.is_zero is True:
                raise ZeroDivisionError(
                    "Division by zero is not allowed."
                )

            return validate_numeric_result(left / right)

        elif isinstance(node.op, ast.Pow):

            if right.is_number:

                if right.is_real is not True:
                    raise ValueError(
                        "Exponent must be a real number."
                    )

                if (
                    right > MAX_EXPONENT
                    or right < -MAX_EXPONENT
                ):
                    raise ValueError(
                        "Exponent magnitude is too large."
                    )

            # Reject zero raised to a negative power.
            if (
                left.is_zero is True
                and right.is_negative is True
            ):
                raise ZeroDivisionError(
                    "Division by zero is not allowed."
                )

            # Check integer exponentiation size before calculating it.
            if (
                left.is_Integer
                and right.is_Integer
                and right >= 0
            ):

                base_value = int(left)
                exponent_value = int(right)

                if base_value not in (-1, 0, 1):

                    estimated_bits = (
                        abs(base_value).bit_length()
                        * exponent_value
                    )

                    if estimated_bits > MAX_NUMERIC_BITS:
                        raise ValueError(
                            "Numerical result is too large."
                        )

            return validate_numeric_result(left ** right)

        raise ValueError("Unsupported arithmetic operator.")

    # Handle positive and negative values.
    elif isinstance(node, ast.UnaryOp):

        operand = evaluate_node(node.operand)

        if isinstance(node.op, ast.UAdd):
            return operand

        elif isinstance(node.op, ast.USub):
            return validate_numeric_result(-operand)

        raise ValueError("Unsupported unary operator.")

    # Handle mathematical function calls.
    elif isinstance(node, ast.Call):

        if not isinstance(node.func, ast.Name):
            raise ValueError("Unsupported function call.")

        function_name = node.func.id

        if function_name not in ALLOWED_FUNCTIONS:
            raise ValueError(
                f"Unsupported function: {function_name}"
            )

        if len(node.args) != 1 or node.keywords:
            raise ValueError(
                "Functions must have exactly one argument."
            )

        argument = evaluate_node(node.args[0])

        result = ALLOWED_FUNCTIONS[function_name](argument)

        return validate_numeric_result(result)

    else:
        raise ValueError("Unsupported mathematical expression.")


# ==========================================
# Public expression parser
# ==========================================

def parse_expression(user_input):
    """Safely parse a mathematical expression using Python AST."""

    if not isinstance(user_input, str):
        raise ValueError("Input must be a string.")

    user_input = user_input.strip()

    if not user_input:
        raise ValueError("Expression cannot be empty.")

    if len(user_input) > MAX_EXPRESSION_LENGTH:
        raise ValueError("Expression is too long.")

    try:

        syntax_tree = ast.parse(
            user_input,
            mode="eval"
        )

        # Validate complexity before evaluating.
        validate_ast_complexity(syntax_tree)

        expression = evaluate_node(syntax_tree.body)

        return expression

    except SyntaxError:
        raise ValueError("Invalid mathematical syntax.") from None

    except RecursionError:
        raise ValueError("Expression nesting is too deep.") from None
