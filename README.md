# AI Calculator

A natural-language mathematical assistant built with Python, SymPy, and Streamlit. The application interprets mathematical requests written in plain English, performs calculations, and presents results through a simple interactive web interface.

## Features

- Natural-language mathematical request processing.
- Arithmetic operations: addition, subtraction, multiplication, and division.
- Symbolic differentiation and integration.
- Algebraic expression expansion and factorisation.
- Equation solving.
- Scientific operations: sine, cosine, tangent, logarithm, square root, and exponential.
- Step-by-step explanations for differentiation.
- Calculation history with a clear-history option.
- Restricted AST-based expression parsing for safer input handling.
- Error handling for invalid mathematical expressions and division by zero.

## Technology Stack

- **Python** — Core application logic.
- **SymPy** — Symbolic mathematics.
- **NumPy** — Numerical computation support.
- **Streamlit** — Web-based user interface.
- **pytest** — Automated testing.
- **pytest-cov** — Test coverage analysis.

## Project Structure

```text
AI-calculator/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── modules/
│   ├── calculator.py
│   ├── equation_solver.py
│   ├── explanation.py
│   ├── expression_parser.py
│   ├── nlp_engine.py
│   ├── output_formatter.py
│   └── request_processor.py
│
└── tests/
    ├── test_calculator.py
    ├── test_nlp_engine.py
    ├── test_parser_validation.py
    ├── test_processor.py
    └── test_result_formatting.py
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone <repository-url>
cd AI-calculator
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

**Git Bash:**

```bash
source .venv/Scripts/activate
```

### 4. Install dependencies

```bash
python -m pip install -r requirements.txt
```

## Running the Application

Start the Streamlit application:

```bash
python -m streamlit run app.py
```

The application will open in your browser.

## Running Tests

Execute the complete test suite:

```bash
python -m pytest
```

To generate a coverage report:

```bash
python -m pytest --cov=modules --cov-report=term-missing
```

## Architecture

The application follows a modular architecture:

1. **Frontend:** Streamlit handles user input and displays results.
2. **NLP Engine:** Identifies the requested mathematical operation and extracts the expression.
3. **Expression Parser:** Validates and parses mathematical expressions using a restricted AST-based approach.
4. **Request Processor:** Coordinates parsing, operation selection, and calculation.
5. **Calculator Engine:** Performs symbolic and numerical mathematical operations.
6. **Explanation Generator:** Produces step-by-step differentiation explanations.
7. **Output Formatter:** Formats mathematical results for presentation.

## Security Considerations

User-provided mathematical expressions are processed using a restricted AST-based parser. Arbitrary Python code execution through `eval()` is not used.

## Project Status

The application currently supports the mathematical operations and interface features listed above. Additional capabilities may be introduced in future development.

## License

License not yet specified.
