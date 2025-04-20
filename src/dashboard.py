import streamlit as st
import time
from scraper import fetch_news_articles
from summarizer import generate_summary
from report_generator import generate_report
from article_scoring import score_article_with_gemini
from insights import generate_insight

queries = {
    "climate_risk": ["climate change", "natural disasters", "hurricanes", "wildfires", "floods", "climate risk", "insurance impact"],
    "insuretech": ["InsurTech", "insurance technology", "startups", "AI in insurance", "digital transformation in insurance", "blockchain insurance"],
    "policies": ["insurance policy", "regulations", "insurance laws", "policy changes", "regulatory updates"],
    "business_exposure": ["business exposure", "corporate risk", "market exposure", "business interruption insurance", "insurance for businesses"]
}
def process_article(args):
    article, domain = args
    summary = generate_summary(article, domain)
    score = score_article_with_gemini(article["title"], summary)
    return generate_report(article, domain, summary, score)

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
             # Fetch articles for each keyword in the query
            articles=fetch_news_articles(keyword)
            for article in articles:
                
                # Generate a summary for the article based on the domain
                summary = generate_summary(article,domain)
                
                # Score the article's impact on the insurance industry using Gemini
                score=score_article_with_gemini(article["title"],summary)

                # Generate a report combining the article, summary, domain, and score
                report = generate_report(article, domain, summary, score)

                # Collect all processed articles
                all_articles.append(report)
        sorted_articles = sorted(all_articles, key=lambda a: a["insurance_impact_score"], reverse=True)[:5]
        
        # print(sorted_articles)

        for article in sorted_articles:
            title = article["title"]
            summary = article["summary"]
            source = article["source"]
            date = article["published_at"]

            #Generating Insight from the context
            insight = generate_insight(summary, domain_query)
        
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
if __name__ == "__main__":
    home_page()