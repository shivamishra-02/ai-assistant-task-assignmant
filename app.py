import streamlit as st
from google import genai
import os
from dotenv import load_dotenv

# Load env
load_dotenv()

# Init client
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

# UI
st.set_page_config(page_title="AI Assistant", page_icon="🤖")
st.title("AI Assistant 🤖 Made By Shivam")

user_input = st.text_input("Ask your question:")

if user_input:
    with st.spinner("Thinking..."):

        prompt = f"""
You are a helpful AI assistant.

Answer the question using EXACTLY 3 bullet points.
Each bullet point must be ONE short line (max 10–12 words).
Do NOT write anything extra before or after.
The last bullet point must include a short example.

Question: {user_input}
"""

        response = client.models.generate_content(
            model="models/gemini-2.5-flash",
            contents=prompt
        )

        st.write(response.text)