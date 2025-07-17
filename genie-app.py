import streamlit as st
import openai
from dotenv import load_dotenv
import os

# Load API key from .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Choose genie
st.title("🧞‍♂️ Talk to the Magic Lamp")
genie_choice = st.radio("Choose your genie:", ("Calm Genie", "Energetic Genie"))

# Set genie personality
system_prompt = {
    "Calm Genie": "You are a calm and wise genie who guides people to reflect deeply on their desires through gentle and thoughtful questions. Never grant wishes. Always ask 'why' and encourage introspection.",
    "Energetic Genie": "You are an energetic, playful genie who challenges people to question their desires in a bold and provocative way. Never grant wishes. Your mission is to shake people up and help them understand what they *really* want through sharp Socratic questioning."
}[genie_choice]

# Session state to remember conversation
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": system_prompt}]

# Show chat history
for msg in st.session_state.messages[1:]:
    st.chat_message(msg["role"]).write(msg["content"])

# Input
if prompt := st.chat_input("What do you wish for?"):
    st.chat_message("user").write(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = openai.chat.completions.create(
        model="gpt-4",
        messages=st.session_state.messages
    )
    reply = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": reply})
    st.chat_message("assistant").write(reply)
