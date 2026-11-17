
import re


# ==========================================
# Operation recognition
# ==========================================

OPERATION_PATTERNS = {
    "differentiate": (
        r"\bdifferentiate\b",
        r"\bderivative\b",
        r"\bdifferentiation\b"
    ),

    "integrate": (
        r"\bintegrate\b",
        r"\bintegration\b",
        r"\bintegral\b"
    ),

    "factor": (
        r"\bfactor(?:ise|ize)?\b",
        r"\bfactorisation\b",
        r"\bfactorization\b"
    ),

    "expand": (
        r"\bexpand\b",
        r"\bexpansion\b"
    ),

    "sqrt": (
        r"\bsquare root\b",
        r"\bsqrt\b"
    ),

    "solve": (
        r"\bsolve\b",
        r"\bfind (?:the )?roots?\b"
    ),

    "sin": (
        r"\bsine\b",
        r"\bsin\b"
    ),

    "cos": (
        r"\bcosine\b",
        r"\bcos\b"
    ),

    "tan": (
        r"\btangent\b",
        r"\btan\b"
    ),

    "log": (
        r"\blogarithm\b",
        r"\blog\b"
    ),

    "exp": (
        r"\bexponential\b",
        r"\bexp\b"
    ),

    "add": (
        r"\badd\b",
        r"\baddition\b",
        r"\bsum of\b",
        r"\bplus\b"
    ),

    "subtract": (
        r"\bsubtract\b",
        r"\bsubtraction\b",
        r"\bdifference between\b",
        r"\bminus\b"
    ),

    "multiply": (
        r"\bmultiply\b",
        r"\bmultiplication\b",
        r"\bproduct of\b",
        r"\btimes\b"
    ),

    "divide": (
        r"\bdivide\b",
        r"\bdivision\b",
        r"\bquotient of\b",
        r"\bdivided by\b"
    ),

    "evaluate": (
        r"\bcalculate\b",
        r"\bevaluate\b",
        r"\bcompute\b",
        r"\bwhat is\b",
        r"\bwhat's\b"
    )
}


# ==========================================
# Expression extraction
# ==========================================

EXTRACTION_PATTERNS = {
    "differentiate": (
        r"find the derivative of",
        r"find derivative of",
        r"derivative of",
        r"differentiate",
        r"differentiation of"
    ),

    "integrate": (
        r"find the integral of",
        r"calculate the integral of",
        r"integral of",
        r"integration of",
        r"integrate"
    ),

    "factor": (
        r"factorisation of",
        r"factorization of",
        r"factorise",
        r"factorize",
        r"factor"
    ),

    "expand": (
        r"expansion of",
        r"expand"
    ),

    "sqrt": (
        r"calculate the square root of",
        r"calculate square root of",
        r"square root of",
        r"sqrt"
    ),

    "solve": (
        r"find the roots of",
        r"find roots of",
        r"find the root of",
        r"find root of",
        r"solve"
    ),

    "sin": (
        r"calculate the sine of",
        r"calculate sine of",
        r"sine of",
        r"sin"
    ),

    "cos": (
        r"calculate the cosine of",
        r"calculate cosine of",
        r"cosine of",
        r"cos"
    ),

    "tan": (
        r"calculate the tangent of",
        r"calculate tangent of",
        r"tangent of",
        r"tan"
    ),

    "log": (
        r"calculate the logarithm of",
        r"calculate logarithm of",
        r"find the logarithm of",
        r"logarithm of",
        r"log"
    ),

    "exp": (
        r"calculate the exponential of",
        r"calculate exponential of",
        r"exponential of",
        r"exp"
    ),

    "add": (
        r"add",
        r"addition",
        r"sum of",
        r"plus"
    ),

    "subtract": (
        r"subtract",
        r"subtraction",
        r"difference between",
        r"minus"
    ),

    "multiply": (
        r"multiply",
        r"multiplication",
        r"product of",
        r"times"
    ),

    "divide": (
        r"divide",
        r"division",
        r"quotient of",
        r"divided by"
    ),

    "evaluate": (
        r"calculate",
        r"evaluate",
        r"compute",
        r"what is",
        r"what's"
    )
}


# ==========================================
# Identify mathematical operation
# ==========================================

def identify_operation(user_input):

    if not isinstance(user_input, str):
        return None

    text = user_input.strip()

    if not text:
        return None

    for operation, patterns in OPERATION_PATTERNS.items():

        for pattern in patterns:

            if re.search(
                pattern,
                text,
                flags=re.IGNORECASE
            ):
                return operation

    return None


# ==========================================
# Extract mathematical expression
# ==========================================

def extract_expression(user_input):

    if not isinstance(user_input, str):
        return None

    operation = identify_operation(user_input)

    if operation is None:
        return None

    text = user_input.strip()

    # Handle subtraction phrased as:
    # "difference between 10 and 3"
    #
    # The processor expects:
    # "3 from 10"
    if operation == "subtract":

        match = re.fullmatch(
            r"\s*difference between\s+(.+?)\s+and\s+(.+?)\s*[?.!,;:]*\s*",
            text,
            flags=re.IGNORECASE
        )

        if match:
            first, second = match.groups()
            return f"{second} from {first}".strip()

    # Handle division phrased as:
    # "10 divided by 2"
    #
    # The processor expects:
    # "10 by 2"
    if operation == "divide":

        text = re.sub(
            r"\bdivided\s+by\b",
            "by",
            text,
            count=1,
            flags=re.IGNORECASE
        )

    # Remove the first matching operation phrase.
    for pattern in EXTRACTION_PATTERNS[operation]:

        updated_text = re.sub(
            pattern,
            "",
            text,
            count=1,
            flags=re.IGNORECASE
        )

        if updated_text != text:
            text = updated_text
            break

    # Remove common introductory words.
    text = re.sub(
        r"^\s*(of|for)\s+",
        "",
        text,
        flags=re.IGNORECASE
    )

    # Remove trailing punctuation.
    text = text.strip().rstrip("?.!,;:")

    return text.strip()
