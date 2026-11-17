
import re


OPERATION_PATTERNS = {
    "differentiate": [
        r"\bdifferentiate\b",
        r"\bderivative\b",
        r"\bdifferentiation\b"
    ],
    "integrate": [
        r"\bintegrate\b",
        r"\bintegral\b",
        r"\bintegration\b"
    ],
    "factor": [
        r"\bfactor\b",
        r"\bfactorise\b",
        r"\bfactorize\b",
        r"\bfactorisation\b",
        r"\bfactorization\b"
    ],
    "expand": [
        r"\bexpand\b",
        r"\bexpansion\b"
    ],
    "sqrt": [
        r"\bsquare root\b",
        r"\bsqrt\b"
    ],
    "solve": [
        r"\bsolve\b",
        r"\bfind roots\b",
        r"\broots\b"
    ],
    "sin": [
        r"\bsine\b",
        r"\bsin\b"
    ],
    "cos": [
        r"\bcosine\b",
        r"\bcos\b"
    ],
    "tan": [
        r"\btangent\b",
        r"\btan\b"
    ],
    "log": [
        r"\blogarithm\b",
        r"\blog\b"
    ],
    "exp": [
        r"\bexponential\b",
        r"\bexp\b"
    ],
    "add": [
        r"\badd\b",
        r"\baddition\b",
        r"\bsum\b",
        r"\bplus\b"
    ],
    "subtract": [
        r"\bsubtract\b",
        r"\bsubtraction\b",
        r"\bdifference\b",
        r"\bminus\b"
    ],
    "multiply": [
        r"\bmultiply\b",
        r"\bmultiplication\b",
        r"\bproduct\b",
        r"\btimes\b"
    ],
    "divide": [
        r"\bdivide\b",
        r"\bdivision\b",
        r"\bquotient\b",
        r"\bdivided\s+by\b"
    ],
    "evaluate": [
        r"\bevaluate\b",
        r"\bcalculate\b",
        r"\bcompute\b",
        r"\bwhat\s+is\b",
        r"\bwhat's\b"
    ]
}


EXTRACTION_PATTERNS = {
    "differentiate": [
        r"\bdifferentiate\b",
        r"\bderivative\s+of\b",
        r"\bdifferentiation\s+of\b"
    ],
    "integrate": [
        r"\bintegrate\b",
        r"\bintegral\s+of\b",
        r"\bintegration\s+of\b"
    ],
    "factor": [
        r"\bfactor(?:ise|ize)?\b",
        r"\bfactorisation\s+of\b",
        r"\bfactorization\s+of\b"
    ],
    "expand": [
        r"\bexpand\b",
        r"\bexpansion\s+of\b"
    ],
    "sqrt": [
        r"\bsquare\s+root\s+of\b",
        r"\bsqrt\b"
    ],
    "solve": [
        r"\bsolve\b",
        r"\bfind\s+roots\s+of\b",
        r"\broots\s+of\b"
    ],
    "sin": [
        r"\bsine\s+of\b",
        r"\bsin\s+of\b",
        r"\bsine\b",
        r"\bsin\b"
    ],
    "cos": [
        r"\bcosine\s+of\b",
        r"\bcos\s+of\b",
        r"\bcosine\b",
        r"\bcos\b"
    ],
    "tan": [
        r"\btangent\s+of\b",
        r"\btan\s+of\b",
        r"\btangent\b",
        r"\btan\b"
    ],
    "log": [
        r"\blogarithm\s+of\b",
        r"\blog\s+of\b",
        r"\blogarithm\b",
        r"\blog\b"
    ],
    "exp": [
        r"\bexponential\s+of\b",
        r"\bexp\s+of\b",
        r"\bexponential\b",
        r"\bexp\b"
    ],
    "add": [
        r"\badd\b",
        r"\baddition\b",
        r"\bsum\s+of\b",
        r"\bplus\b"
    ],
    "subtract": [
        r"\bsubtract\b",
        r"\bsubtraction\b",
        r"\bdifference\s+between\b",
        r"\bminus\b"
    ],
    "multiply": [
        r"\bmultiply\b",
        r"\bmultiplication\b",
        r"\bproduct\s+of\b",
        r"\btimes\b"
    ],
    "divide": [
        r"\bdivide\b",
        r"\bdivision\b",
        r"\bquotient\s+of\b"
    ],
    "evaluate": [
        r"\bevaluate\b",
        r"\bcalculate\b",
        r"\bcompute\b"
    ]
}


def identify_operation(user_input):

    if not isinstance(user_input, str):
        return None

    text = user_input.lower()

    for operation, patterns in OPERATION_PATTERNS.items():

        for pattern in patterns:

            if re.search(pattern, text):
                return operation

    return None


def extract_expression(user_input):

    if not isinstance(user_input, str):
        return None

    text = user_input.strip()

    operation = identify_operation(text)

    if operation is None:
        return None

    # Handle subtraction phrased as:
    # Difference between 10 and 3.
    if operation == "subtract":

        match = re.fullmatch(
            r"(?:please\s+)?difference between\s+(.+?)\s+and\s+(.+?)\s*[?.!,;:]*",
            text,
            flags=re.IGNORECASE
        )

        if match:
            first = match.group(1).strip()
            second = match.group(2).strip()

            return f"{second} from {first}"

    # Preserve the operand separator expected by request_processor.py.
    if operation == "divide":
        text = re.sub(
            r"\bdivided\s+by\b",
            "by",
            text,
            flags=re.IGNORECASE
        )

    # Remove the operation phrase.
    for pattern in EXTRACTION_PATTERNS.get(operation, []):

        text = re.sub(
            pattern,
            "",
            text,
            count=1,
            flags=re.IGNORECASE
        )

        if text != user_input.strip():
            break

    # Remove introductory command words independently.
    text = re.sub(
        r"^\s*please\s+",
        "",
        text,
        flags=re.IGNORECASE
    )

    text = re.sub(
        r"^\s*(?:find|calculate|compute|evaluate)\s+",
        "",
        text,
        flags=re.IGNORECASE
    )

    text = re.sub(
        r"^\s*(?:what\s+is|what's)\s+",
        "",
        text,
        flags=re.IGNORECASE
    )

    text = re.sub(
        r"^\s*(?:the|of|for)\s+",
        "",
        text,
        flags=re.IGNORECASE
    )

    text = text.strip(" \t\n\r?.!,;:")

    return text
