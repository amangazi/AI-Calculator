
import streamlit as st

from modules.request_processor import process_request


# --------------------------------
# Page configuration
# --------------------------------

st.set_page_config(
    page_title="AI Calculator",
    page_icon="🧮",
    layout="centered"
)


# --------------------------------
# Application heading
# --------------------------------

st.title("🧮 AI Calculator")

st.caption(
    "A natural-language mathematical assistant "
    "powered by Python and SymPy."
)


# --------------------------------
# Session state
# --------------------------------

if "history" not in st.session_state:
    st.session_state.history = []


# --------------------------------
# Input form
# --------------------------------

with st.form("calculator_form"):

    user_input = st.text_area(
        "Enter your mathematical request",
        placeholder="e.g. Differentiate x**2 + 3*x",
        height=100
    )

    submitted = st.form_submit_button(
        "Calculate",
        use_container_width=True
    )


# --------------------------------
# Process request
# --------------------------------

if submitted:

    if not user_input.strip():

        st.warning("Please enter a mathematical request.")

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


# --------------------------------
# Display latest result
# --------------------------------

if st.session_state.history:

    latest = st.session_state.history[0]
    response = latest["response"]

    st.divider()

    if response["success"]:

        st.subheader("Result")

        st.success("Calculation completed successfully!")

        st.code(
            response["result"],
            language="text"
        )

        # Display mathematical explanations separately.
        if response["explanation"]:

            st.subheader("Step-by-step explanation")

            for index, step in enumerate(
                response["explanation"],
                start=1
            ):

                st.markdown(f"**Step {index}**")

                st.write(step)

    else:

        st.error(response["error"])


# --------------------------------
# Calculation history
# --------------------------------

if st.session_state.history:

    st.divider()

    st.subheader("Calculation History")

    if st.button("Clear History"):

        st.session_state.history.clear()
        st.rerun()

    for item in st.session_state.history:

        with st.expander(item["input"]):

            history_response = item["response"]

            if history_response["success"]:

                st.code(
                    history_response["result"],
                    language="text"
                )

                for index, step in enumerate(
                    history_response["explanation"],
                    start=1
                ):

                    st.write(f"{index}. {step}")

            else:

                st.error(history_response["error"])