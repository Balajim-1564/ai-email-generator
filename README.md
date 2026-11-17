# AI Email Generator

A Streamlit app that generates email drafts with the OpenAI API.

## Run locally

1. Install the dependencies:

   ```powershell
   python -m pip install -r requirements.txt
   ```

2. Set your OpenAI API key in PowerShell:

   ```powershell
   $env:OPENAI_API_KEY = "your-api-key"
   ```

3. Start the app from this folder:

   ```powershell
   python -m streamlit run app.py
   ```

Alternatively, create `.streamlit/secrets.toml` with:

```toml
OPENAI_API_KEY = "your-api-key"
```

Do not commit this file or share your API key.

## Deploy with Streamlit Community Cloud

1. Push this project to a GitHub repository.
2. Sign in to [Streamlit Community Cloud](https://share.streamlit.io/) with GitHub and create a new app.
3. Select this repository, its branch, and `app.py` as the entry point.
4. In the app's **Advanced settings** or **Secrets** settings, add:

   ```toml
   OPENAI_API_KEY = "your-api-key"
   ```

5. Save and deploy the app.

Never put an API key in source code or commit `.streamlit/secrets.toml`.
