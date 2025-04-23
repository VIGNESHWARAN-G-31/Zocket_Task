import requests
from bs4 import BeautifulSoup
from transformers import pipeline


def fetch_web_content(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')

        
        paragraphs = soup.find_all('p')
        content = ' '.join([p.get_text() for p in paragraphs if p.get_text()])

        
        if len(content) < 1000:
            headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
            content += ' '.join([h.get_text() for h in headings if h.get_text()])

        return content[:3500]
    except Exception as e:
        return f"⚠️ Error fetching content: {e}"


def format_summary(text):

    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    summary = summarizer(text, max_length=600, min_length=300, do_sample=False)[0]['summary_text']

  
    intro = summary.split(". ")[0:2]
    highlights = summary.split(". ")[2:6]
    insights = summary.split(". ")[6:8]
    conclusion = summary.split(". ")[8:]

    
    return f"""
📄 Summary:




{' '.join(intro)}.

⚡ **Main Highlights**
- {highlights[0]}.
- {highlights[1]}.
- {highlights[2]}.
- {highlights[3]}.

💡 **Additional Insights**
{' '.join(insights)}.

✨ **Conclusion**
{' '.join(conclusion)}.
""".strip()


def ai_agent(url):
    content = fetch_web_content(url)
    if "⚠️" in content:
        return content
    return format_summary(content)


if __name__ == "__main__":
    user_url = input("🔗 Enter a URL to summarize: ")
    result = ai_agent(user_url)
    print(result)
