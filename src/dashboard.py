import streamlit as st
import os
import re
import sys
import time
import json
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import json
from scraper import fetch_news_articles
from classify import classify_article
from summarizer import generate_summary
from report_generator import generate_report
from article_scoring import score_article_with_gemini
from datetime import datetime
from insights import generate_insight
# json_file_path = 'outputs/reports.json'
# with open(json_file_path, 'r') as file:
#     data = json.load(file)
queries = {
    "climate_risk": ["climate change", "natural disasters", "hurricanes", "wildfires", "floods", "climate risk", "insurance impact"],
    "insuretech": ["InsurTech", "insurance technology", "startups", "AI in insurance", "digital transformation in insurance", "blockchain insurance"],
    "policies": ["insurance policy", "regulations", "insurance laws", "policy changes", "regulatory updates"],
    "business_exposure": ["business exposure", "corporate risk", "market exposure", "business interruption insurance", "insurance for businesses"]
}
# queries = {
#     # "climate_risk": ["climate change", "natural disasters"]
#     # "insuretech": ["InsurTech", "insurance technology", "startups", "AI in insurance", "digital transformation in insurance", "blockchain insurance"],
#     "policies": ["insurance policy", "regulations", "insurance laws"],
#     # "business_exposure": ["business exposure", "corporate risk", "market exposure", "business interruption insurance", "insurance for businesses"]
# }
# def escape_markdown(text):
#     return re.sub(r'([\\`*_{}[\]()#+\-!])', r'\\\1', text)
def home_page():
    st.title("Insurance News Dashboard")
    st.markdown("""
    Welcome to the **Insurance News Dashboard**. This app helps you track the latest news and insights from the world of **Insurance**.
    
    Select a domain below to get started!
    """)

    # Navigation
    selected_domain = st.selectbox(
        "Select Domain",
        ["-- Select Domain --","Climate Risk", "InsureTech", "Policies", "Business Exposure"]
    )
    
    # Display news based on selected domain
    if selected_domain != "-- Select Domain --":
        st.markdown(
    f"""
    <div style="
        font-size: 20px;
        font-weight: 600;
        color: #333333;
        padding: 8px 4px;
        border-bottom: 1px solid #dddddd;
        margin-bottom: 20px;
    ">
        Showing news for {selected_domain}
    </div>
    """,
    unsafe_allow_html=True
)
        display_news(selected_domain)
    else:
        st.warning("Please select a domain to continue.")
    # if selected_domain:
    #     st.markdown(f"### Showing news for **{selected_domain}**")
        # display_news(selected_domain)
def likely_insurance_related(text):
    insurance_triggers = [
        "insurance", "insurer", "insured", "claim", "coverage", 
        "risk", "damage", "loss", "recovery", "catastrophe", "policy"
    ]
    return any(word in text.lower() for word in insurance_triggers)
def stream_text(label, text, delay=0.8):
    container = st.empty()
    chunks = text.split('. ')
    streamed_text = f"**{label}**\n\n"

    for chunk in chunks:
        if chunk.strip():
            streamed_text += chunk.strip() + '. '
            container.markdown(streamed_text)
            time.sleep(delay)

def display_news(domain):
    # Get the relevant keyword query for the selected domain
    domain_query = queries.get(domain.lower().replace(" ", "_"))
    
    if domain_query:
        all_articles = []
        for keyword in domain_query:
            articles=fetch_news_articles(keyword)
            # likely_insurance_related(article["content"])
                # for article in 
            with open("outputs/reports.json", "w") as f:
                json.dump(articles, f, indent=2)
            count=0
            reporting_t=[]
            for article in articles:
                count=count+1
                # if(likely_insurance_related(article["content"])):
                domain = domain
                # classify_article(article["title"] + " " + (article.get("content") or ""))
                summary = generate_summary(article)
                score=score_article_with_gemini(article["title"],summary)
                report = generate_report(article, domain, summary, score)
                all_articles.append(report)
                with open("outputs/reports2.json", "w") as f:
                    json.dump(report, f, indent=2)
            print("at the end count is ",count)
        # all_articles.append(report)
        sorted_articles = sorted(all_articles, key=lambda a: a["insurance_impact_score"], reverse=True)[:5]
        print("Articles are")
        print(sorted_articles)
        # articles = get_news_articles(keyword).get("articles", [])
        for article in sorted_articles:
            # Extract article details
            # title = article.get("title", "No title")
            # summary = article.get("summary", "No description")
            # # url = article.get("source", "No URL")
            # source = article.get("source", {}).get("name", "Unknown Source")
            # date = article.get("published_at", datetime.now().strftime('%Y-%m-%d'))
            title = article["title"]
            summary = article["summary"]
            # url = article.get("source", "No URL")
            source = article["source"]
            date = article["published_at"]
            # Summarize and generate insights
            # summary = summarize_article(description)
            insight = generate_insight(summary, "Climate Risk")
            # Placeholder for fact-checking (You can integrate a fact-checking API)
            # fact_check_percentage = 85  # Example: this can be dynamically calculated or fetched from a service
            
            # Display the article with insights and fact-checking score
            # st.markdown(f"**Title:** {title}")
            st.markdown(
               f"""
               <div style="
                   background-color: #f0f2f6;
                   padding: 10px;
                   border-left: 5px solid #4a90e2;
                   border-radius: 5px;
                   margin-bottom: 10px;
               ">
                   <strong>Title:</strong> {title}
               </div>
               """,
               unsafe_allow_html=True
           )
            st.markdown(f"**Source:** {source} | **Date:** {date}")
            stream_text("**Summary:**", summary)
            stream_text("**Insight:**", insight)

            # st.markdown(f"**Summary:** {summary}")
            # st.markdown(f"**Insight:** {insight}")
            # st.markdown(f"**Fact-Check Score:** {fact_check_percentage}%")
            # st.markdown(f"[Read More]({url})")
if __name__ == "__main__":
    home_page()