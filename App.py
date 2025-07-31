import streamlit as st
import streamlit.components.v1 as components
import requests
import os

from dotenv import load_dotenv
load_dotenv()

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
    st.session_state.messages = [{"role": "system", "content": get_system_message(persona)}]
if "submitted" not in st.session_state:
    st.session_state.submitted = False

# Display previous messages
for msg in st.session_state.messages:
    if msg["role"] != "system":
        st.markdown(f"**{msg['role'].capitalize()}:** {msg['content']}")

# Text input
with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("You:", key="user_input")
    submit = st.form_submit_button("Send")

if submit and user_input:
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

    if response.status_code == 200:
        data = response.json()
        reply = data["completion_message"]["content"]["text"]
        st.session_state.messages.append({"role": "assistant", "content": reply})
        st.rerun()
    else:
        st.error(f"API call failed. Status: {response.status_code}")
        st.json(response.json())

# auto-scroll

scroll_anchor = st.empty()
scroll_anchor.markdown("<div id='scroll-anchor'></div>", unsafe_allow_html=True)

st.components.v1.html(
    """
    <script>
        var anchor = window.parent.document.querySelector("iframe[srcdoc*='scroll-anchor']");
        if (anchor) {
            anchor.scrollIntoView({ behavior: 'smooth' });
        }
    </script>
    """,
    height=0,
)