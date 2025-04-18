# summarizer.py
# import openai
import os 
import streamlit as st
import google.generativeai as genai

# from dotenv import load_dotenv
# from openai import AsyncOpenAI
# load_dotenv()
# openai.api_key = os.getenv("open_apikey")


gemini_api_key = st.secrets.get("summarization_api")
# gemini_api_key = os.getenv("summarization_api")
genai.configure(api_key=gemini_api_key)
# print(gemini_api_key)
model = genai.GenerativeModel("gemini-2.0-flash-lite")

def generate_summary(article):
    prompt = prompt = f"""
#     Summarize the following article in 3-4 bullet points. 
#     Be concise and highlight key points relevant to climate risk or insurance.

#     Title: {article['title']}
#     Content: {article['content'] or article['description'] or ''}
#     """
    response = model.generate_content(
    # model="gemini-2.0-flash-lite",
    contents=prompt
    )
    summary = response.text
    # generated.split("\n")[1] if "\n" in generated else generated
    print(summary)
    return summary.strip()

