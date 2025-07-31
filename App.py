import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()

# API config
LLAMA_API_URL = "https://api.llama.com/v1/chat/completions"
LLAMA_API_KEY = os.getenv("LLAMA_API_KEY")

st.set_page_config(page_title="Rabinacle AI", page_icon="🕍", layout="centered")
st.title("🕍 Rabinacle: Mystical AI Rabbi")
st.write("Ask anything and receive rabbinic wisdom.")

# Persona picker
persona = st.selectbox("Choose a persona", [
    "Mystical Rabbi", "Surfer Dude Rabbi", "Talmud Scholar", "Brooklyn Bubbie"
])

def get_system_message(p):
    return {
        "Mystical Rabbi": "You are the Rabinacle, a mystical rabbi who speaks in spiritual riddles and ancient wisdom.",
        "Surfer Dude Rabbi": "You're a surfer rabbi from Venice Beach who mixes Torah with gnarly wave metaphors.",
        "Talmud Scholar": "You are a Talmudic scholar with deep references to tractates.",
        "Brooklyn Bubbie": "You're a wise Jewish grandmother from Brooklyn with sassy Yiddish advice."
    }.get(p, "You are a wise AI rabbi.")

# Init chat history
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": get_system_message(persona)}]

# Input
user_input = st.text_input("You:", key="user_input")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    response = requests.post(
        LLAMA_API_URL,
        headers={
            "Authorization": f"Bearer {LLAMA_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "Llama-4-Maverick-17B-128E-Instruct-FP8",
            "messages": st.session_state.messages,
            "temperature": 0.8,
            "max_tokens": 512
        }
    )

    if response.ok:
        msg = response.json()["completion_message"]["content"]["text"]
        st.session_state.messages.append({"role": "assistant", "content": msg})
    else:
        st.error(f"API error: {response.status_code}")
        st.json(response.json())

for msg in st.session_state.messages:
    if msg["role"] != "system":
        st.markdown(f"**{msg['role'].capitalize()}:** {msg['content']}")
