
from modules.nlp_engine import identify_operation, extract_expression


def test_identify_tangent():

    result = identify_operation("calculate tangent of 45")

    assert result == "tan"


def test_extract_expression_without_operation():

    result = extract_expression("hello there")

    assert result is None
