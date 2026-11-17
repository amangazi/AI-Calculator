import sympy as sp


def format_result(result):

    # Check whether the result is a SymPy mathematical object
    if isinstance(result, sp.Basic):

        exact_result = str(result)

        # Check whether the result is a numerical value
        if result.is_number and not result.is_Integer:

            numerical_result = str(result.evalf())

            return (
                f"Exact result: {exact_result}\n"
                f"Numerical approximation: {numerical_result}"
            )

        return f"Result: {exact_result}"

    # Handle lists, such as equation solutions
    elif isinstance(result, list):

        return f"Results: {result}"

    # Handle ordinary Python values and error messages
    else:

        return f"Result: {result}"