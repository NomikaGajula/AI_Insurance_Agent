# from transformers import pipeline
# from google import genai
import google.generativeai as genai

import os
import json
import streamlit as st
# insight_generator = pipeline("text-generation", model="gpt2")
# json_file_path = 'outputs/reports.json'
gemini_api_key=st.secrets["genAI_API_KEY"]
# gemini_api_key = os.getenv("genAI_API_KEY")
genai.configure(api_key=gemini_api_key)
# print(gemini_api_key)
model = genai.GenerativeModel("gemini-2.0-flash-lite")

# client = genai.Client(api_key=gemini_api_key)

def generate_insight(summary, domain):
    prompt = f"News Summary: {summary}Based on the above news, what are the key strategic or operational implications for companies operating in the {domain} segment of the insurance and reinsurance industry? Please provide a few concise, high-level insights focusing on: Potential risks or opportunities Impact on current business models or practices, Possible actions or responses by industry players, Keep it sharp, actionable, and industry-aware."
    response = model.generate_content(
    # model="gemini-2.0-flash-lite",
    contents=prompt,
    )
    # generated = insight_generator(prompt, max_length=100, num_return_sequences=1, do_sample=True)[0]['generated_text']
    # Extract the insight from the generated text (assumes it's the second line)
    insight = response.text
    # generated.split("\n")[1] if "\n" in generated else generated
    print(insight)
    return insight.strip()
# Open and load the JSON file
# with open(json_file_path, 'r') as file:
#     data = json.load(file)
# for article in data:
#     insight=generate_insight(article["summary"],article["domain"])
#     print(insight)
