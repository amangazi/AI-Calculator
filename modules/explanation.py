
import sympy as sp


def explain_differentiation(expression, variable):
    """
    Generate a term-by-term explanation of differentiation.
    """

    steps = []

    expanded = sp.expand(expression)

    steps.append(
        f"Original expression: {sp.sstr(expression)}"
    )

    if expanded != expression:
        steps.append(
            f"Expanded expression: {sp.sstr(expanded)}"
        )

    steps.append(
        f"Differentiate each term with respect to {variable}."
    )

    terms = sp.Add.make_args(expanded)
    derivatives = []

    for term in terms:
        derivative = sp.diff(term, variable)
        derivatives.append(derivative)

        if term.is_Pow and term.exp.is_number:
            steps.append(
                f"Apply the power rule to {sp.sstr(term)}: "
                f"derivative = {sp.sstr(derivative)}."
            )

        elif term.func == sp.sin:
            steps.append(
                f"Apply the sine differentiation rule to "
                f"{sp.sstr(term)}: derivative = {sp.sstr(derivative)}."
            )

        elif term.func == sp.cos:
            steps.append(
                f"Apply the cosine differentiation rule to "
                f"{sp.sstr(term)}: derivative = {sp.sstr(derivative)}."
            )

        elif term.func == sp.exp:
            steps.append(
                f"Apply the exponential differentiation rule to "
                f"{sp.sstr(term)}: derivative = {sp.sstr(derivative)}."
            )

        elif term.func == sp.log:
            steps.append(
                f"Apply the logarithmic differentiation rule to "
                f"{sp.sstr(term)}: derivative = {sp.sstr(derivative)}."
            )

        else:
            steps.append(
                f"Derivative of {sp.sstr(term)} "
                f"= {sp.sstr(derivative)}."
            )

    result = sp.Add(*derivatives)

    steps.append(
        f"Combine the derivatives of all terms: {sp.sstr(result)}."
    )

    return steps


def explain_integration(expression, variable):
    """
    Generate a term-by-term explanation of integration.
    """

    steps = []

    expanded = sp.expand(expression)

    steps.append(
        f"Original expression: {sp.sstr(expression)}"
    )

    if expanded != expression:
        steps.append(
            f"Expanded expression: {sp.sstr(expanded)}"
        )

    steps.append(
        f"Integrate each term with respect to {variable}."
    )

    terms = sp.Add.make_args(expanded)
    integrals = []

    for term in terms:
        integral = sp.integrate(term, variable)
        integrals.append(integral)

        steps.append(
            f"Integral of {sp.sstr(term)} "
            f"= {sp.sstr(integral)}."
        )

    result = sp.Add(*integrals)

    steps.append(
        f"Combine the integrated terms: {sp.sstr(result)}."
    )

    steps.append(
        "Add the constant of integration C for an indefinite integral."
    )

    return steps
