# report_generator.py
def generate_report(article, domain, summary, score):
    return {
        "domain": domain,
        "title": article["title"],
        "summary": summary,
        "source": article["url"],
        "published_at": article["publishedAt"],
        "insurance_impact_score":score
    }
