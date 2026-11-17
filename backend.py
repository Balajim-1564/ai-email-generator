# Import the OpenAI client so this file can send requests to the OpenAI API.
from openai import OpenAI


def generate_email(purpose, tone, recipient, length, api_key):
    """Generate an email using its purpose, tone, and recipient."""

    # Insert the values from the app into instructions for the AI.
    prompt = f"""
    You are an expert email writer.
    Generate email.
    Purpose: {purpose}
    Tone: {tone}
    Recipient: {recipient}
    Length: {length}
    Return:
    Subject: Body:
    """

    # Send the instructions to the selected model and ask it to write the email.
    client = OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role":"system",
                "content":"You generate emails."
            },

            {
                "role":"user",
                "content":prompt
            }
        ]
    )

    # Return the first generated email so the Streamlit app can display it.
    return response.choices[0].message.content
