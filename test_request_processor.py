from modules.request_processor import process_request


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
    "calculate exponential of 2",
    "factorise x.__class__",
    "differentiate open('file.txt')",
    "expand x +",
    "solve unknown_function(x)",
    "calculate 25 + 17",
    "evaluate 100 / 4",
    "compute 8 * 9",
    "what is 50 - 12",
    "calculate 10/0",
    "calculate x/0",
    "calculate 1/(x-x)"
]


for user_input in test_inputs:

    result = process_request(user_input)

    print("User Request:", user_input)
    print("Calculator Result:", result)
    print("-" * 60)