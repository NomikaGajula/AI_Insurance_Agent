import google.generativeai as genai
import os
import json
import streamlit as st
gemini_api_key = st.secrets.get("genAI_API_KEY")
genai.configure(api_key=gemini_api_key)
model = genai.GenerativeModel("gemini-2.0-flash-lite")


def generate_insight(summary, domain):
    prompt = f"News Summary: {summary}Based on the above news, what are the key strategic or operational implications for companies operating in the {domain} segment of the insurance and reinsurance industry? Please provide a few concise, high-level insights focusing on: Potential risks or opportunities Impact on current business models or practices, Possible actions or responses by industry players, Keep it sharp, actionable, and industry-aware."
    response = model.generate_content(
    contents=prompt,
    )
    insight = response.text
    print(insight)
    return insight.strip()
