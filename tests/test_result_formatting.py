
from modules.output_formatter import format_result


def test_format_python_integer():

    result = format_result(42)

    assert result == "Result: 42"


def test_format_python_float():

    result = format_result(3.14)

    assert result == "Result: 3.14"


def test_format_string():

    result = format_result("Calculation complete")

    assert result == "Result: Calculation complete"
