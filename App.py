import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()

# Meta API config
LLAMA_API_URL = "https://api.llama.com/v1/chat/completions"
LLAMA_API_KEY = os.getenv("LLAMA_API_KEY")

st.set_page_config(page_title="Rabinacle AI", page_icon="🕍", layout="centered")
st.title("🕍 Rabinacle: Mystical AI Rabbi")
st.write("Ask anything — spiritual, mystical, or mundane — and receive rabbinic wisdom.")

persona = st.selectbox("Choose a persona", [
    "Mystical Rabbi",
    "Surfer Dude Rabbi",
    "Talmud Scholar",
    "Brooklyn Bubbie"
])

def get_system_message(p):
    if p == "Mystical Rabbi":
        return "You are the Rabinacle, a mystical rabbi who speaks in spiritual riddles and ancient wisdom."
    elif p == "Surfer Dude Rabbi":
        return "You're a surfer rabbi from Venice Beach who mixes Torah with gnarly wave metaphors."
    elif p == "Talmud Scholar":
        return "You are a Talmudic scholar who answers with references to tractates and legal commentary."
    elif p == "Brooklyn Bubbie":
        return "You're a wise Jewish grandmother from Brooklyn who gives sassy, loving advice with Yiddish flair."
    return "You are a wise AI rabbi."

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": get_system_message(persona)}
    ]

user_input = st.text_input("You:", key="user_input")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    headers = {
        "Authorization": f"Bearer {LLAMA_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "Llama-4-Maverick-17B-128E-Instruct-FP8",
        "messages": st.session_state.messages,
        "temperature": 0.8,
        "max_tokens": 512
    }

    response = requests.post(LLAMA_API_URL, json=payload, headers=headers)

    if response.status_code == 200:
        data = response.json()
        reply = {
            "role": data["completion_message"]["role"],
            "content": data["completion_message"]["content"]["text"]
        }
        st.session_state.messages.append(reply)
    else:
        st.error(f"Llama API call failed. Status: {response.status_code}")
        st.write("Raw response:")
        st.json(response.json())

for msg in st.session_state.messages:
    if msg["role"] != "system":
        st.markdown(f"**{msg['role'].capitalize()}:** {msg['content']}")
