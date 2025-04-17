import google.generativeai as genai
model = genai.GenerativeModel("gemini-2.0-flash-lite")

def score_article_with_gemini(title, description):
    prompt = f"""Article Title: {title}
    Article Description: {description}
    On a scale of 0 to 1, how much does this article impact the insurance industry (including providers or takers)? 
    Respond only with a number from 0 to 1."""
    
    try:
        response = model.generate_content(prompt)
        score_text = response.text.strip()
        score = float(score_text)
        return min(max(score, 0.0), 1.0)  # Clamp between 0 and 1
    except:
        return 0.0
