import requests
from bs4 import BeautifulSoup
from transformers import pipeline
from keybert import KeyBERT


def fetch_web_content(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')

        paragraphs = soup.find_all('p')
        content = ' '.join([p.get_text() for p in paragraphs if p.get_text()])

        if len(content) < 1000:
            headings = soup.find_all(['h1', 'h2', 'h3', 'h4'])
            content += ' '.join([h.get_text() for h in headings if h.get_text()])

        return content[:3500]
    except Exception as e:
        return f"⚠️ Error fetching content: {e}"

# Calling Model From HuggingFace(Bart Model)
def summarize_with_hf(text, model_name="sshleifer/distilbart-cnn-12-6"):
    summarizer = pipeline("summarization", model=model_name)
    summary = summarizer(text, max_length=5, min_length=200, do_sample=False)
    return summary[0]["summary_text"]

#This fucntion for generating Summary
def format_summary(summary):
    split_summary = summary.split(". ")
    intro = split_summary[:2]
    highlights = split_summary[2:6]
    insights = split_summary[6:8] if len(split_summary) > 6 else ["🔍 Not enough content to extract specific insights."]
    conclusion = split_summary[8:] if len(split_summary) > 8 else ["📌 Summary ends here."]

    return f"""
📚 <span style="color: #2e8b57;"><b>Introduction</b></span><br>
{" ".join(intro)}<br><br>

---

⚡ <span style="color: #ff6347;"><b>Highlights</b></span><br>
- {"<br>- ".join(highlights) if highlights else 'No clear highlights found.'}<br><br>

---

💡 <span style="color: #00bfff;"><b>Insights</b></span><br>
{" ".join(insights)}<br><br>

---

✨ <span style="color: #ffd700;"><b>Conclusion</b></span><br>
{" ".join(conclusion)}
"""

# this fucntion for keywords feature
def extract_keywords(text, num_keywords=10):
    kw_model = KeyBERT()
    keywords = kw_model.extract_keywords(text, top_n=num_keywords, stop_words='english')
    return ", ".join([kw[0] for kw in keywords])
