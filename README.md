# AI_Insurance_Agent
ai-insurance-agent/
│
├── data/                     # Optional: for storing raw/scraped articles
│
├── notebooks/                # Optional: for experimenting in Jupyter notebooks
│
├── src/
│   ├── scraper.py            # Web/news API scraping logic
│   ├── classify.py           # Classify article into domain (e.g., Climate Risk)
│   ├── summarizer.py         # LLM-based summary generation
│   ├── report_generator.py   # Generate final structured report
│
├── outputs/
│   └── reports.json          # Structured outputs
│
├── requirements.txt
├── README.md
└── main.py                   # Orchestrates the full flow
