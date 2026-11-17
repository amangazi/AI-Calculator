
import sympy as sp


def format_result(result):

    # Handle SymPy mathematical objects.
    if isinstance(result, sp.Basic):

        exact_result = sp.sstr(result)

        if result.is_number and not result.is_Integer:

            numerical_result = sp.sstr(result.evalf())

            return (
                f"Exact result: {exact_result}\n"
                f"Numerical approximation: {numerical_result}"
            )

        return f"Result: {exact_result}"

    # Handle equation solutions.
    elif isinstance(result, list):

        return f"Results: {result}"

    # Handle ordinary Python values and error messages.
    else:

        return f"Result: {result}"
