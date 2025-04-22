import streamlit as st
from ai_agent_summary import ai_agent

st.set_page_config(page_title="AI URL Summarizer", layout="wide")

# 💅 Updated CSS for Full-Page Background
st.markdown("""
<style>
    html, body, [class*="css"]  {
        height: 100%;
        margin: 0;
        font-family: 'Segoe UI', sans-serif;
        background: linear-gradient(to right, #8EC5FC, #E0C3FC); /* New full-page background */
    }

    .title {
        font-size: 44px;
        color: #fff;
        text-align: center;
        padding: 20px;
        border-radius: 12px;
        background: linear-gradient(to right, #ff512f, #dd2476);
        box-shadow: 2px 4px 15px rgba(0,0,0,0.3);
    }

    .description {
        font-size: 18px;
        color: #222;
        padding: 5px 0 25px 0;
        text-align: center;
    }

    .stTextInput > div > div > input {
        background-color: #fff;
        border: 2px solid #ff6a00;
        border-radius: 8px;
        padding: 10px;
        box-shadow: 1px 1px 6px rgba(0, 0, 0, 0.1);
    }

    .summary {
        background-color: #ffffff;
        color: #333;
        border-left: 6px solid #ff6a00;
        border-radius: 10px;
        padding: 20px;
        margin-top: 20px;
        font-size: 16px;
        line-height: 1.6;
        box-shadow: 2px 4px 10px rgba(0,0,0,0.15);
    }
</style>
""", unsafe_allow_html=True)

# 🎯 Title and Instructions
st.markdown('<div class="title">🔎 AI URL Summarizer</div>', unsafe_allow_html=True)
st.markdown('<p class="description">Paste any article URL and get a beautifully formatted summary!</p>', unsafe_allow_html=True)

# 🌐 Input Box
url = st.text_input("📥 Enter a URL", placeholder="https://example.com/article")

# 🧠 Generate Summary
if url:
    with st.spinner("✨ Summarizing the content..."):
        summary = ai_agent(url)
        st.markdown('<div class="summary">', unsafe_allow_html=True)
        st.markdown("### 📄 Summary")
        st.markdown(summary, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
