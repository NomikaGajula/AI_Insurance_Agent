# classify.py

def classify_article(article_text):
    categories = {
        "Climate Risk": ["climate", "wildfire", "flood", "disaster", "temperature"],
        "InsureTech": ["AI", "blockchain", "automation", "startup", "technology"],
        "Policies": ["regulation", "policy", "compliance", "TNFD", "law"],
        "Business Exposure": ["insurance", "claims", "loss", "underwriting"]
    }

    for domain, keywords in categories.items():
        if any(word.lower() in article_text.lower() for word in keywords):
            return domain
    return "Uncategorized"
