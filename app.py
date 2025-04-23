import streamlit as st
from test import fetch_web_content, summarize_with_hf, format_summary, extract_keywords
from gtts import gTTS
from fpdf import FPDF
import os
import matplotlib.pyplot as plt
from collections import Counter
import re

# Set page config
st.set_page_config(page_title="Smart Summarizer", layout="wide")

# Session state for summary
if "formatted_summary" not in st.session_state:
    st.session_state.formatted_summary = ""

# Custom CSS
st.markdown("""
    <style>
    body, .stApp {
        background: linear-gradient(to right, #dbeafe, #e0f2fe);
        font-family: 'Segoe UI', sans-serif;
    }
    .main-title {
        font-size: 3em;
        color: #1e293b;
        text-align: center;
        font-weight: 700;
        margin-top: 1rem;
        margin-bottom: 2rem;
    }
    .section-header {
        font-size: 1.5em;
        font-weight: 600;
        color: #0f172a;
        margin-bottom: 10px;
    }
    .content-box {
        background-color: #ffffff;
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        overflow-wrap: break-word;
        height: 100%;
    }
    .divider {
        height: 100%;
        width: 2px;
        background-color: #94a3b8;
        margin: auto;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="main-title">🌐 Web Content Summarizer</div>', unsafe_allow_html=True)

# Feature Buttons
feature_col1, feature_col2, feature_col3, feature_col4, feature_col5 = st.columns(5)
with feature_col1:
    summary_button = st.button("Summary")
with feature_col2:
    keyword_button = st.button("Keyword Extraction")
with feature_col3:
    narration_button = st.button("Voice Narration")
with feature_col4:
    pdf_button = st.button("Download PDF")
with feature_col5:
    graphical_button = st.button("Graphical Summary")

# URL input
url_input = st.text_input("🔗 Enter a URL to summarize:")

if url_input:
    content = fetch_web_content(url_input)

    if summary_button:
        with st.spinner("⏳ Generating Summary..."):
            summary = summarize_with_hf(content)
            formatted = format_summary(summary)
            st.session_state.formatted_summary = formatted
            st.markdown(f'<div class="content-box">{formatted}</div>', unsafe_allow_html=True)

    if keyword_button:
        with st.spinner("🔍 Extracting Keywords..."):
            keywords = extract_keywords(content)
            st.markdown(f"**Extracted Keywords:** {keywords}")

    if narration_button:
        if st.session_state.formatted_summary:
            tts = gTTS(st.session_state.formatted_summary, lang='en')
            tts.save("summary.mp3")
            st.audio("summary.mp3")
        else:
            st.warning("⚠️ Generate the summary first to enable narration.")

    if pdf_button:
        def clean_text_for_pdf(text):
            return re.sub(r'[^\x00-\x7F]+', '', text)  # Remove non-ASCII characters (emojis etc.)

        if st.session_state.formatted_summary:
            cleaned_summary = clean_text_for_pdf(st.session_state.formatted_summary.replace('<br>', '\n'))

            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.multi_cell(0, 10, cleaned_summary)
            pdf.output("summary.pdf")

            with open("summary.pdf", "rb") as f:
                st.download_button("📥 Download PDF", f, file_name="summary.pdf", mime="application/pdf")
        else:
            st.warning("⚠️ Generate the summary first to enable PDF download.")

    if graphical_button:
        word_frequencies = Counter(re.findall(r'\w+', content.lower()))
        most_common_words = word_frequencies.most_common(10)
        words = [word[0] for word in most_common_words]
        frequencies = [word[1] for word in most_common_words]

        fig, ax = plt.subplots()
        ax.barh(words, frequencies, color='skyblue')
        ax.set_xlabel('Frequency')
        ax.set_title('Top 10 Most Common Words')
        st.pyplot(fig)

    left_col, mid_col, right_col = st.columns([1.2, 0.05, 1.2])

    with left_col:
        st.markdown('<div class="section-header">📥 Fetched Content</div>', unsafe_allow_html=True)
        if "Error" not in content:
            st.markdown(f'<div class="content-box">{content}</div>', unsafe_allow_html=True)
        else:
            st.error(content)

    with mid_col:
        st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

    with right_col:
        if "Error" not in content and st.session_state.formatted_summary:
            st.markdown('<div class="section-header">🎨 Formatted Summary</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="content-box">{st.session_state.formatted_summary}</div>', unsafe_allow_html=True)
