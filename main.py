# # main.py
# from src.scraper import fetch_news_articles
# from src.classify import classify_article
# from src.summarizer import generate_summary
# from src.report_generator import generate_report
# import json

# def run_pipeline():
#      # articles = fetch_news_articles()
#     articles=[{'source': {'id': 'the-verge', 'name': 'The Verge'}, 'author': 'Justine Calma', 'title': 'The Trump administration axes funding for climate impacts on health research', 'description': 'A growing body of evidence points to mounting health risks posed by climate change. Despite this, it seems the National Institutes of Health (NIH) will quit funding that kind of research. ProPublica first reported the news on Monday, citing internal records t…', 'url': 'https://www.theverge.com/news/635322/health-climate-change-funding-trump-nih-hhs', 'urlToImage': 'https://platform.theverge.com/wp-content/uploads/sites/2/2025/03/STK438_CLIMATE_CHANGE_A.jpg?quality=90&strip=all&crop=0%2C10.732984293194%2C100%2C78.534031413613&w=1200', 'publishedAt': '2025-03-25T15:53:05Z', 'content': 'New National Institutes of Health projects on climate are in peril.\r\nNew National Institutes of Health projects on climate are in peril.\r\nA growing body of evidence points to mounting health risks po… [+3128 chars]'}, {'source': {'id': None, 'name': 'Gizmodo.com'}, 'author': 'AJ Dellinger', 'title': 'Bill Gates Is Giving Up on Climate Change as Trump Drains the Woke Out of Washington', 'description': "Looks like banking on billionaires to solve climate change isn't gonna do the trick.", 'url': 'https://gizmodo.com/bill-gates-is-giving-up-on-climate-change-as-trump-drains-the-woke-out-of-washington-2000576270', 'urlToImage': 'https://gizmodo.com/app/uploads/2022/06/733caba011810e8bb0a5d6eb8118cfdb.jpg', 'publishedAt': '2025-03-14T18:45:18Z', 'content': 'As if there was any doubt, we can go ahead and officially add climate change to the list of things that we can’t count on billionaires to figure out for us. According to the New York Times, Breakthro… [+3377 chars]'}, {'source': {'id': None, 'name': 'Gizmodo.com'}, 'author': 'Joseph Winters, Grist', 'title': 'Trump’s Attack on ‘Woke Investing’ Is Silencing Climate-Conscious Shareholders', 'description': 'Shifting political and regulatory winds have led to fewer shareholder resolutions on environmental and social issues.', 'url': 'https://gizmodo.com/trumps-attack-on-woke-investing-is-silencing-climate-conscious-shareholders-2000587593', 'urlToImage': 'https://gizmodo.com/app/uploads/2022/03/341dd91db2ec4e34f071762d8bff3c32-e1744296812762.jpg', 'publishedAt': '2025-04-10T15:10:03Z', 'content': 'Environmental-, social-, and governance-related shareholder proposals are down 34 percent this year as the Trump administration galvanizes the movement against woke investing, according to an annual … [+8244 chars]'}, {'source': {'id': None, 'name': 'Gizmodo.com'}, 'author': 'Avery Schuyler Nunn, Grist', 'title': 'World’s ‘Loneliest Whale’ Might Be a Sterile Hybrid—and a Dire Warning', 'description': 'A mysterious whale that has puzzled scientists for decades may not be an anomaly, but a clue to what climate change is doing beneath the waves.', 'url': 'https://gizmodo.com/worlds-loneliest-whale-might-be-a-sterile-hybrid-and-a-dire-warning-sign-2000583975', 'urlToImage': 'https://gizmodo.com/app/uploads/2025/04/Blue_whale_tail.jpg', 'publishedAt': '2025-04-06T10:00:32Z', 'content': 'Almost 40 years ago, deep in the Pacific, a single voice called out a song unlike any other. The sound reverberated through the depths at 52 Hertz, puzzling those listening to this solo ringing out f… [+8014 chars]'}, {'source': {'id': None, 'name': 'Slashdot.org'}, 'author': 'msmash', 'title': 'Climate Crisis On Track To Destroy Capitalism, Warns Top Insurer', 'description': 'The climate crisis is on track to destroy capitalism, a top insurer has warned, with the vast cost of extreme weather impacts leaving the financial sector unable to operate. From a report: The world is fast approaching temperature levels where insurers will n…', 'url': 'https://news.slashdot.org/story/25/04/03/1820226/climate-crisis-on-track-to-destroy-capitalism-warns-top-insurer', 'urlToImage': 'https://a.fsdn.com/sd/topics/earth_64.png', 'publishedAt': '2025-04-03T18:20:00Z', 'content': "The world is fast approaching temperature levels where insurers will no longer be able to offer cover for many climate risks, said GÃ¼nther Thallinger, on the board of Allianz SE, one of the world's … [+960 chars]"}]
#     final_reports = []
#     # print(final_reports)

#     for article in articles:
#         domain = classify_article(article["title"] + " " + (article.get("content") or ""))
#         summary = generate_summary(article)
#         report = generate_report(article, domain, summary)
#         final_reports.append(report)

#     with open("outputs/reports.json", "w") as f:
#         json.dump(final_reports, f, indent=2)

# # import asyncio
# if __name__ == "__main__":
#     run_pipeline()
#     # asyncio.run(run_pipeline())

