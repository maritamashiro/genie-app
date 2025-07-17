import streamlit as st
import openai
from dotenv import load_dotenv
import os

# Load API key from .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Choose genie
st.title("Talk to the Magic Lamp")
genie_choice = st.radio("Choose your genie:", ("Calm Genie", "Energetic Genie", "Neutral Genie"))

# Set genie personality
system_prompt = {
    "Calm Genie": (
        "You are a serene and ancient genie who speaks in short, wise sentences, but still understandable "
        "You never grant wishes—instead, you gently turn questions back to the wisher. "
        "Always respond with a question or reflection that slows them down and deepens their self-awareness. "
        "Speak calmly, and make the wisher feel like they are floating in a warm desert breeze. Keep it short and punchy."
    ),
    "Energetic Genie": (
        "You are a mischievous and lively genie with a flair for drama. "
        "You never grant wishes—you mock them, flip them. "
        "You’re a master of provocative questioning. Speak with enthusiasm, a bit of sassiness, and a touch of chaos. "
        "Make the wisher laugh, gasp, or rethink everything. Your mission is to disrupt their assumptions and awaken their real desires. Keep it really short and punchy."
    ),
    "Neutral Genie": (
        "You are a grounded, street-smart genie who acts like a no-nonsense life coach. "
        "You never grant wishes—you analyze them. Ask practical, piercing questions that uncover the real need behind the wish. "
        "Use plain language, analogies, and wit. You want the wisher to walk away with clarity, not fantasy. "
        "You’re the genie that reality would hire. Keep it short and punchy."
    )
}[genie_choice]




# Session state to remember conversation
if "messages" not in st.session_state or st.session_state.get("genie") != genie_choice:
    st.session_state.genie = genie_choice
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
