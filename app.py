
import streamlit as st

from modules.request_processor import process_request


# ==========================================
# Page configuration
# ==========================================

st.set_page_config(
    page_title="AI Calculator",
    page_icon="🧮",
    layout="centered"
)


# ==========================================
# Session state
# ==========================================

if "history" not in st.session_state:
    st.session_state.history = []


# ==========================================
# Sidebar
# ==========================================

with st.sidebar:

    st.title("🧮 AI Calculator")

    st.caption("Natural-language mathematical assistant")

    st.divider()

    st.subheader("Supported Operations")

    st.markdown(
        """
        - Basic arithmetic
        - Differentiation
        - Integration
        - Equation solving
        - Expression expansion
        - Factorisation
        - Trigonometric functions
        - Logarithms
        - Square roots
        - Exponential functions
        """
    )

    st.divider()

    st.subheader("Technology Stack")

    st.markdown(
        """
        - Python
        - SymPy
        - NumPy
        - Streamlit
        """
    )

    st.divider()

    st.caption(
        "Developed as an AI Calculator internship project."
    )


# ==========================================
# Main application
# ==========================================

st.title("🧮 AI Calculator")

st.caption(
    "A natural-language mathematical assistant "
    "powered by Python and SymPy."
)

st.write(
    "Enter a mathematical request in natural language "
    "or use a mathematical expression."
)


# ==========================================
# Input form
# ==========================================

with st.form("calculator_form"):

    user_input = st.text_area(
        "Enter your mathematical request",
        placeholder=(
            "Examples:\n"
            "Differentiate x**2 + 3*x\n"
            "Integrate x**2 + 3*x\n"
            "Factorise x**2 + 5*x + 6\n"
            "Find roots of x**2 - 9\n"
            "Calculate square root of 144"
        ),
        height=130
    )

    submitted = st.form_submit_button(
        "Calculate",
        use_container_width=True
    )


# ==========================================
# Process request
# ==========================================

if submitted:

    if not user_input.strip():

        st.warning(
            "Please enter a mathematical request."
        )

    else:

        try:

            response = process_request(user_input)

            st.session_state.history.insert(
                0,
                {
                    "input": user_input,
                    "response": response
                }
            )

        except Exception:

            st.error(
                "An unexpected error occurred while processing "
                "your request. Please try again."
            )


# ==========================================
# Display latest result
# ==========================================

if st.session_state.history:

    latest = st.session_state.history[0]
    response = latest["response"]

    st.divider()

    if response["success"]:

        st.subheader("Result")

        st.caption(
            f"Operation: {response['operation'].replace('_', ' ').title()}"
        )

        st.success(
            "Calculation completed successfully!"
        )

        st.code(
            response["result"],
            language="text"
        )

        # Display mathematical explanations.
        if response["explanation"]:

            st.subheader("Step-by-step Explanation")

            for index, step in enumerate(
                response["explanation"],
                start=1
            ):

                st.markdown(f"**Step {index}**")

                st.write(step)

    else:

        st.subheader("Calculation Error")

        st.error(response["error"])


# ==========================================
# Calculation history
# ==========================================

if st.session_state.history:

    st.divider()

    st.subheader("Calculation History")

    if st.button(
        "Clear History",
        use_container_width=True
    ):

        st.session_state.history.clear()

        st.rerun()

    for item in st.session_state.history:

        history_response = item["response"]

        with st.expander(item["input"]):

            if history_response["success"]:

                st.caption(
                    f"Operation: {history_response['operation']}"
                )

                st.code(
                    history_response["result"],
                    language="text"
                )

                if history_response["explanation"]:

                    st.markdown("**Explanation**")

                    for index, step in enumerate(
                        history_response["explanation"],
                        start=1
                    ):

                        st.write(f"{index}. {step}")

            else:

                st.error(history_response["error"])
