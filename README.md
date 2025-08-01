Shiza Pa-Piza!!

# 🕍 Rabbi AI

**Rabbi AI** is a mystical chatbot powered by Python and Streamlit. It simulates conversations with various rabbinic personas, offering spiritual, philosophical, and sometimes humorous insights in response to user questions.

---

## 💡 Features

- Choose from multiple rabbinic personas:
  - Mystical Rabbi
  - Surfer Dude Rabbi
  - Talmud Scholar
  - Brooklyn Bubbie
- Stateful chat history
- Styled UI with fixed input bar
- API integration with LLAMA v4
- Autoscroll support

---

## 🛠 Stack

- Python 3.11+
- [Streamlit](https://streamlit.io/)
- Conda (for environment management)
- Docker (optional for containerized deployment)
- Llama API (external chat completion)

---

## 🚀 Getting Started

### 1. Clone the Repo

```zsh
git clone https://github.com/yourusername/rabbi-ai.git
cd rabbi-ai
```

### 2. Setup the Environment

```zsh
conda create -n rabinacle python=3.11
conda activate rabinacle
pip install -r requirements.txt or conda.Yaml
```

### 3. Add API Key

```py
LLAMA_API_KEY=your_llama_api_key_here
```

### 4. Run with Streamlit

```zsh
streamlit run app.py
```

### Docker Usage (Optional Build)

```zsh
docker build -t rabbi-ai .
docker run -p 8501:8501 --env-file .env rabbi-ai
```
