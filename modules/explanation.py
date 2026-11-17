
import sympy as sp


def explain_differentiation(expression, variable):
    """
    Generate a step-by-step explanation
    for differentiating a polynomial.
    """

    steps = []

    expanded = sp.expand(expression)

    steps.append(
        f"Original expression: {sp.sstr(expression)}"
    )

    steps.append(
        f"Expanded expression: {sp.sstr(expanded)}"
    )

    steps.append(
        f"Apply the power rule: d({variable}**n)/d{variable} "
        f"= n*{variable}**(n-1)."
    )

    terms = sp.Add.make_args(expanded)

    for term in terms:
        derivative = sp.diff(term, variable)

        steps.append(
            f"Derivative of {sp.sstr(term)} "
            f"= {sp.sstr(derivative)}"
        )

    result = sp.diff(expression, variable)

    steps.append(
        f"Final answer: {sp.sstr(result)}"
    )

    return steps
