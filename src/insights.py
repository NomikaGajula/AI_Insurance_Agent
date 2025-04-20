import google.generativeai as genai
import os
import json
import time
import streamlit as st
gemini_api_key = st.secrets.get("genAI_API_KEY")
# from dotenv import load_dotenv
# load_dotenv()
# load_dotenv(dotenv_path=".env")

# gemini_api_key = os.getenv("genAI_API_KEY")
genai.configure(api_key=gemini_api_key)
model = genai.GenerativeModel("gemini-2.0-flash-lite")

def generate_insight(summary, domain):
    time.sleep(2)  # Artificial delay, possibly to respect rate limits or API pacing

        # Constructing a clear and structured prompt for insight generation
    prompt = (
        f"News Summary: {summary}\n\n"
        f"Based on the above news, what are the key strategic or operational implications for companies "
        f"operating in the {domain} segment of the insurance and reinsurance industry?\n\n"
        f"Please provide a few concise, high-level insights focusing on:\n"
        f"- Potential risks or opportunities\n"
        f"- Impact on current business models or practices\n"
        f"- Possible actions or responses by industry players\n\n"
        f"Keep it sharp, actionable, and industry-aware."
    )
    # prompt = f"News Summary: {summary}Based on the above news, what are the key strategic or operational implications for companies operating in the {domain} segment of the insurance and reinsurance industry? Please provide a few concise, high-level insights focusing on: Potential risks or opportunities Impact on current business models or practices, Possible actions or responses by industry players, Keep it sharp, actionable, and industry-aware."
    # Generate the response using the Gemini model
    response = model.generate_content(
    contents=prompt,
    )
    
    # Extract the insight from the response object
    insight = response.text

    # print(insight)
    return insight.strip()

summary="""Here's a concise summary of the article in bullet points:

*   **Brazil will host the Earthshot Prize:** Prince William's environmental initiative will take place in Brazil later this year.
*   **Timing aligns with COP30:** The Earthshot Prize event coincides with Brazil hosting the COP30 UN climate change conference.
*   **Focus on environmental solutions:** The Earthshot Prize recognizes and awards solutions to pressing environmental challenges."""
generate_insight(summary,"climate risk")