# summarizer.py
import time
import os 
import streamlit as st
import google.generativeai as genai

# from dotenv import load_dotenv
# load_dotenv()

gemini_api_key = st.secrets.get("summarization_api")
# gemini_api_key = os.getenv("genAI_API_KEY")
genai.configure(api_key=gemini_api_key)
# print(gemini_api_key)
model = genai.GenerativeModel("gemini-2.0-flash-lite")

def generate_summary(article,domain):
    time.sleep(2)  # Optional delay, likely to avoid API throttling

     # Prompt: concise summary tailored to the domain or insurance context
    prompt = (
        f"Summarize the following article in 3-4 bullet points. "
        f"Be concise and highlight key points relevant to {domain} or insurance.\n\n"
        f"Title: {article['title']}\n"
        f"Content: {article['content'] or article['description'] or ''}"
    )
    # prompt =f"Summarize the following article in 3-4 bullet points. Be concise and highlight key points relevant to {domain} or insurance.Title: {article['title']} Content: {article['content'] or article['description'] or ''}"
    # Generate summary using Gemini model
    response = model.generate_content(
    contents=prompt
    )
    
    # Extract text content from response
    summary = response.text

    # print(summary)

    return summary.strip()

article={
    "source": {
      
      "name": "BBC News"
    },
    
    "title": "Brazil to host Prince William's Earthshot Prize",
    "description": "The climate prize ceremony will come just before Brazil hosts the COP30 climate summit in November.",
    "url": "https://www.bbc.com/news/articles/c2kv0kpyx1yo",
    "urlToImage": "https://ichef.bbci.co.uk/news/1024/branded_news/ff3c/live/06939240-10cd-11f0-8fbb-bfd213c39946.jpg",
    "publishedAt": "2025-04-04T02:18:09Z",
    "content": "The Prince of Wales' Earthshot Prize will be held in Brazil later this year, Kensington Palace has announced, in the same month the country hosts the COP30 UNclimate change conference.\r\nThe main awar\u2026 [+2481 chars]"
  }
generate_summary(article,"climate risk")