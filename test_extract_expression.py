from modules.nlp_engine import extract_expression

test_inputs = [
    "differentiate x**3 + 2*x",
    "find the derivative of x**2",
    "factorise x**2 + 5*x + 6",
    "expand (x + 2)*(x + 3)",
    "find the integral of sin(x)",
    "find roots of x**2 - 9",
    "calculate square root of 144",
    "calculate sine of pi/2",
    "calculate cosine of 0",
    "calculate the logarithm of 10",
    "calculate exponential of 2"
]

for user_input in test_inputs:
    expression = extract_expression(user_input)

    print("User Input:", user_input)
    print("Extracted Expression:", expression)
    print("-" * 60)