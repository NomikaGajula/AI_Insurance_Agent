# summarizer.py
# import openai
import os 
import streamlit as st
import google.generativeai as genai

# from dotenv import load_dotenv
# from openai import AsyncOpenAI
# load_dotenv()
# openai.api_key = os.getenv("open_apikey")

# async def generate_summary(article):
#     prompt = f"""
#     Summarize the following article in 3-4 bullet points. 
#     Be concise and highlight key points relevant to climate risk or insurance.

#     Title: {article['title']}
#     Content: {article['content'] or article['description'] or ''}
#     """
#     client = AsyncOpenAI()
#     response = await client.chat.completions.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}])

    # response = openai.ChatCompletion.create(
    #     model="gpt-4",
    #     messages=[{"role": "user", "content": prompt}]
    # )
    # return response['choices'][0]['message']['content']
# from transformers import pipeline

# Load the summarization pipeline once (can be outside the function if you're calling multiple times)
# summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

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
    # generated = insight_generator(prompt, max_length=100, num_return_sequences=1, do_sample=True)[0]['generated_text']
    # Extract the insight from the generated text (assumes it's the second line)
    summary = response.text
    # generated.split("\n")[1] if "\n" in generated else generated
    print(summary)
    return summary.strip()






# def load_summarizer():
#     try:
#         # Load the summarization pipeline
#         summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
#     except Exception as e:
#         st.error(f"Error loading model: {e}")
# summarizer = load_summarizer()

# def generate_summary(article):
#     if summarizer is None:
#         return "Unable to generate summary - model loading failed."
#     content = article.get('content') or article.get('description') or ''
#     full_text = f"Title: {article.get('title', '')}\nContent: {content}"

#     # Summarize the article
#     try:
#         summary = summarizer(full_text, max_length=150, min_length=50, do_sample=False)
        
#         # Format the output as bullet points
#         summarized_text = summary[0]['summary_text']
#         bullet_points = [f"- {point.strip()}" for point in summarized_text.split('. ') if point]
        
#         return "\n".join(bullet_points)
#     except Exception as e:
#         return f"Error during summarization: {str(e)}"
#     # summary = summarizer(full_text, max_length=150, min_length=50, do_sample=False)

#     # Format the output as bullet points
#     # summarized_text = summary[0]['summary_text']
#     # bullet_points = [f"- {point.strip()}" for point in summarized_text.split('. ') if point]
    
#     # return "\n".join(bullet_points)