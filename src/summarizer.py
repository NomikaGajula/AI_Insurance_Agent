# summarizer.py
# import openai
import os 
from dotenv import load_dotenv
# from openai import AsyncOpenAI
load_dotenv()
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
from transformers import pipeline

# Load the summarization pipeline once (can be outside the function if you're calling multiple times)
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def generate_summary(article):
    content = article.get('content') or article.get('description') or ''
    full_text = f"Title: {article.get('title', '')}\nContent: {content}"

    # Summarize the article
    summary = summarizer(full_text, max_length=150, min_length=50, do_sample=False)

    # Format the output as bullet points
    summarized_text = summary[0]['summary_text']
    bullet_points = [f"- {point.strip()}" for point in summarized_text.split('. ') if point]
    
    return "\n".join(bullet_points)