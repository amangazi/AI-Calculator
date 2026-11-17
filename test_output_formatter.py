import sympy as sp

from modules.output_formatter import format_result


x = sp.symbols('x')

test_results = [
    sp.log(10),
    sp.exp(2),
    sp.sqrt(2),
    2*x,
    [sp.Integer(-3), sp.Integer(3)]
]

for result in test_results:

    print("Original result:", result)
    print(format_result(result))
    print("-" * 50)