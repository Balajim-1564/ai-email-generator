# Import Streamlit to build the web interface.
import os

import streamlit as st
from streamlit.errors import StreamlitSecretNotFoundError

# Import the backend function that creates the email.
from backend import generate_email


def get_api_key():
    """Read the OpenAI key from the environment or Streamlit secrets."""
    api_key = os.getenv("OPENAI_API_KEY")
    if api_key:
        return api_key

    try:
        return st.secrets["OPENAI_API_KEY"]
    except (KeyError, StreamlitSecretNotFoundError):
        return None


# Display the app's title.
st.title("AI Email Generator")

# Collect the user's email purpose and preferences.
purpose = st.text_area("Enter purpose")
tone = st.selectbox("Select Tone", ["Formal", "Friendly", "Professional"])
recipient = st.selectbox("Recipient", ["Manager", "Client", "Student"])
length = st.selectbox("Length", ["Short","Medium","Long"])

# Run this block only after the user clicks the button.
if st.button("Generate Email"):
    # Generate and display an email only when a purpose was provided.
    if purpose:
        api_key = get_api_key()
        if not api_key:
            st.error("Set OPENAI_API_KEY in your environment or Streamlit secrets.")
        else:
            with st.spinner("Writing your email..."):
                output = generate_email(
                    purpose,
                    tone,
                    recipient,
                    length,
                    api_key
                )

            st.subheader("Generated Email")
            st.write(output)
    else:
        # Ask the user to enter a purpose before generating an email.
        st.warning("Enter purpose")
