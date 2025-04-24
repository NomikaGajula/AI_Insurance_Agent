# 🧠 AI Insurance Agent

A pipeline for automatically scraping, classifying, summarizing, and reporting insurance-relevant articles — tailored for insurance agents to stay informed on climate risk, market trends, and more.

---

## 🗂️ Project Structure

```css
ai-insurance-agent/
│
├── src/
│   ├── scraper.py              # Web/news API scraping logic
│   ├── dashboard.py            # Homepage/dashboard logic
│   ├── insights.py             # Generate insights from processed articles
│   ├── article_sorting.py      # Score and sort articles by relevance
│   ├── summarizer.py           # LLM-based summary generation
│   ├── report_generator.py     # Generate final structured report
│
├── requirements.txt
├── README.md
```

## 🚀 How It Works Project

Scraping: Uses scraper.py to fetch relevant articles from the web or news APIs.

Scoring & Sorting: article_sorting.py evaluates and prioritizes articles by relevance.

Summarization: summarizer.py utilizes LLMs to condense articles into concise summaries.

Insight Generation: insights.py derives key insights and takeaways.

Reporting: report_generator.py compiles a final structured report.

Dashboard: dashboard.py powers the homepage interface to view outputs.

## 🛠️ Setup Instructions

1. Clone the Repository

```css
git clone https://github.com/NomikaGajula/ai-insurance-agent.git
cd ai-insurance-agent
```

2. (Optional) Create a Virtual Environment

```css
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
```
3. Install Dependencies

```css
pip install -r requirements.txt
```

## 💼 Use Cases

📢 Insurance Agents – Get daily curated summaries on relevant topics.

🔍 Risk Analysts – Track climate, economic, and geopolitical trends.

💡 Decision Makers – Instantly extract insights from the flood of information – understand the impact, and know what actions to take.



