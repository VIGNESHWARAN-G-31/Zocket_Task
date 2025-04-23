
# 🚀 AI Agent for Web Content Summarization

Welcome to the **AI Agent for Web Content Summarization** project!  
This intelligent agent can **autonomously analyze and summarize** the content of any web page provided via a URL. With the explosion of information online, this tool helps streamline content consumption by generating concise, meaningful summaries from full-length articles. 🔍🤖

---

## 🧠 Overview

AI agents are transforming how we interact with the web. This project showcases how modern AI can be combined with web scraping and Natural Language Processing (NLP) to automate web content summarization.

Built using Python, **BeautifulSoup**, **Hugging Face Transformers**, and **BART** (Bidirectional and Auto-Regressive Transformers), this agent reads articles and presents a quick summary — perfect for research, productivity, and news tracking.

---

## ✨ Features

- 🔗 Accepts any **valid URL** as input
- 🌐 Fetches and parses web content using **BeautifulSoup** and **Requests**
- 📄 Extracts relevant text (titles, headings, paragraphs) from web pages
- 🤖 Summarizes content using **Hugging Face Transformer models** like **BART**
- 🗣️ **Voice Narration** feature powered by **gTTS (Google Text-to-Speech)**
- 📄 **PDF Export** functionality for saving summaries as downloadable PDFs
- 📊 **Graphical Summary** that visualizes the most common words in the content
- 🧩 Modular and customizable for other NLP tasks

---

## 🧰 Tech Stack

- **Python 3.8+**
- **BeautifulSoup4** – HTML parsing
- **Requests** – For HTTP requests
- **Transformers** – Pretrained summarization models (BART, T5)
- **Torch** – Model backend for transformers
- **gTTS** – For text-to-speech conversion
- **FPDF** – For generating PDFs from summaries
- **Matplotlib** – For creating graphical representations of word frequencies
- **Spacy, NLTK** – For advanced NLP tasks like keyword extraction

---

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/ai-web-summarizer.git
   cd ai-web-summarizer
2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt

## 🚀 Usage 
 1.**Run the application using Streamlit:**
  ```bash
    streamlit run app.py
---

## 🚀 Example Interaction

1. Enter a URL: `https://example.com/news-article`  
2. Wait for the content to be fetched and summarized  
3. Use features:  
   - View summary  
   - Listen to text-to-speech narration  
   - Download summary as PDF  
   - View graphical summary of most common words
---

## 🛠️ How It Works

### 🧾 Step-by-Step Pipeline:
1. 🔗 User inputs a URL  
2. 🌐 The system fetches HTML content using requests  
3. 🧹 Cleans and parses content using BeautifulSoup  
4. 📄 Extracts meaningful text: headers, paragraphs, and meta content  
5. 🤖 Summarizes the text using the BART model from transformers  
6. 🗣️ Converts text to speech using gTTS  
7. 📄 Exports summary as a PDF using FPDF  
8. 📊 Generates visualizations using Matplotlib and WordCloud  
---
## 🌍 Applications

- 📰 News aggregation and summarization  
- 📚 Educational tools for reading comprehension and research  
- 🧠 Cognitive assistants for summarizing dense technical content  
- 🔎 Search engine companions that summarize linked content  
- 📖 Reading tools for busy professionals  
 
---
 
### **SAMPLE OUTPUT**:
![Screenshot 2025-04-23 185135](https://github.com/user-attachments/assets/102a717f-0f72-4ee1-8bb1-29b0511dc984)
![Screenshot 2025-04-23 185115](https://github.com/user-attachments/assets/0b33985b-2c35-4222-9936-71521981e3cc)





