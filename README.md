
# AI Calculator

A Python-based mathematical assistant that accepts natural-language requests, processes mathematical expressions, and performs symbolic and numerical calculations through an interactive Streamlit interface.

The project uses a rule-based natural-language processing engine and a restricted Python AST parser. It does not currently integrate an external large language model (LLM).

## Features

### Mathematical Operations

- Basic arithmetic: addition, subtraction, multiplication, and division.
- Symbolic differentiation.
- Symbolic integration.
- Algebraic expression expansion.
- Algebraic factorisation.
- Equation solving.
- Trigonometric functions: sine, cosine, and tangent.
- Logarithms.
- Square roots.
- Exponential functions.

### Application Features

- Natural-language mathematical request processing.
- Mathematical expression validation.
- Step-by-step differentiation explanations.
- Step-by-step integration explanations.
- Calculation history.
- Option to clear calculation history.
- Error handling for invalid expressions and mathematical operations.

### Input Validation and Security

- Restricted AST-based expression parsing.
- Explicitly permitted mathematical symbols, constants, and functions.
- AST complexity and expression-length limits.
- Exponent magnitude and numerical result-size limits.
- No arbitrary Python code execution through `eval()`.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core application logic |
| SymPy | Symbolic mathematics |
| NumPy | Numerical computation |
| Streamlit | Web-based user interface |
| pytest | Automated testing |
| pytest-cov | Test coverage analysis |

## Project Structure

```text
AI-calculator/
│
├── app.py
├── requirements.txt
├── requirements-dev.txt
├── README.md
├── .gitignore
├── pytest.ini
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
    ├── test_equation_solver.py
    ├── test_nlp_engine.py
    ├── test_parser_validation.py
    ├── test_processor.py
    └── test_result_formatting.py
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/amangazi/AI-Calculator.git
cd AI-Calculator
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

**Windows Command Prompt:**

```cmd
.venv\Scripts\activate
```

### 4. Install dependencies

Install the application dependencies:

```bash
python -m pip install -r requirements.txt
```

For development and testing, install the additional dependencies:

```bash
python -m pip install -r requirements-dev.txt
```

## Running the Application

Start the Streamlit application:

```bash
python -m streamlit run app.py
```

Streamlit will provide a local URL through which the application can be accessed in your browser.

## Running Tests

Run the complete automated test suite:

```bash
python -m pytest -q
```

Generate a test coverage report:

```bash
python -m pytest --cov=modules --cov-report=term-missing
```

## Application Architecture

The application follows a modular architecture in which each component has a specific responsibility.

1. **Streamlit Interface (`app.py`):** Accepts user requests, displays calculation results and explanations, and maintains calculation history.
2. **NLP Engine (`nlp_engine.py`):** Uses predefined patterns and rules to identify mathematical operations and extract expressions from natural-language requests.
3. **Expression Parser (`expression_parser.py`):** Parses mathematical expressions using Python's AST and validates permitted operations, symbols, numerical values, and expression complexity.
4. **Request Processor (`request_processor.py`):** Coordinates operation identification, expression parsing, variable selection, calculation, and response generation.
5. **Calculator Engine (`calculator.py`):** Performs symbolic and numerical mathematical operations using SymPy and NumPy.
6. **Equation Solver (`equation_solver.py`):** Solves supported mathematical equations using SymPy.
7. **Explanation Generator (`explanation.py`):** Produces term-by-term explanations for differentiation and integration.
8. **Output Formatter (`output_formatter.py`):** Converts mathematical results into readable output for presentation.

## Processing Workflow

A typical request follows this sequence:

```text
User Input
    |
    v
Streamlit Interface
    |
    v
NLP Engine
    |
    v
Expression Parser
    |
    v
Request Processor
    |
    v
Calculator / Equation Solver
    |
    v
Explanation Generator
    |
    v
Output Formatter
    |
    v
Result Display
```

## Current Scope and Limitations

- Natural-language processing is rule-based rather than powered by an LLM.
- Mathematical expression parsing is restricted to explicitly supported syntax and functions.
- The application does not currently provide mathematical graph plotting or unit conversion.
- The available operations and supported input patterns are limited to the implemented functionality.

## License

No license has currently been specified.
