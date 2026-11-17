from modules.expression_parser import parse_expression


test_inputs = [
    "",
    "x +",
    "import os",
    "open('file.txt')",
    "x.__class__",
    "unknown_function(x)",
    "x @ 2",
    "True"
]


for user_input in test_inputs:

    try:
        result = parse_expression(user_input)

        print("Input:", user_input)
        print("Accepted:", result)

    except (ValueError, SyntaxError) as error:

        print("Input:", user_input)
        print("Rejected:", error)

    print("-" * 50)