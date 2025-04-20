# summarizer.py
import time
import os 
import streamlit as st
import google.generativeai as genai
from google.api_core.exceptions import ResourceExhausted


# from dotenv import load_dotenv
# load_dotenv()

gemini_api_key = st.secrets.get("summarization_api")
# gemini_api_key = os.getenv("genAI_API_KEY")
genai.configure(api_key=gemini_api_key)
# print(gemini_api_key)
model = genai.GenerativeModel("gemini-2.0-flash-lite")

def generate_summary(article,domain,max_retries=3):
    retries = 0
    base_delay = 2
    while retries <= max_retries:
       try:
          time.sleep(base_delay)
    # time.sleep(2)  # Optional delay, likely to avoid API throttling

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

          print(summary)

          return summary.strip()
       except ResourceExhausted as e:
           if "429" in str(e) and retries < max_retries:
                # Extract retry delay if available in the error message
                retry_seconds = 20  # Default retry time
                # You could parse the actual retry delay from the error message if needed
                
                # Streamlit-friendly notification
                if st.session_state.get('show_error_placeholder'):
                    error_placeholder = st.session_state.error_placeholder
                else:
                    error_placeholder = st.empty()
                    st.session_state.error_placeholder = error_placeholder
                    st.session_state.show_error_placeholder = True
                
                error_placeholder.warning(f"Rate limit exceeded. Retrying in {retry_seconds} seconds... (Attempt {retries+1}/{max_retries})")
              
                # Wait before retrying
                time.sleep(retry_seconds)
                retries += 1
                # Exponential backoff (optional)
                base_delay *= 2
           else:
            st.error(f"Error generating summary: {str(e)}")
            return "Unable to generate summary due to API rate limits. Please try again later."
        
       except Exception as e:
            st.error(f"Error generating summary: {str(e)}")
            return f"Error: {str(e)}"
    
    # If we've used all retries
    return "Unable to generate summary after multiple attempts. Please try again later."
