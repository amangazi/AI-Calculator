
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

def explain_integration(expression, variable):
    """
    Generate a step-by-step explanation
    for integrating an expression term by term.
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
        f"Integrate each term with respect to {variable}."
    )

    terms = sp.Add.make_args(expanded)

    for term in terms:
        integral = sp.integrate(term, variable)

        steps.append(
            f"Integral of {sp.sstr(term)} "
            f"= {sp.sstr(integral)}"
        )

    result = sp.integrate(expression, variable)

    steps.append(
        f"Antiderivative: {sp.sstr(result)}"
    )

    steps.append(
        "Add the constant of integration C for an indefinite integral."
    )

    return steps
