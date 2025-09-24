# import requests, pandas as pd

# API_KEY = "54edfd393a21e0ecbc23a06544266e10"
# INST_TOKEN = "YOUR_INST_TOKEN"  # if provided by your institution

# headers = {
#     "X-ELS-APIKey": API_KEY,
#     "Accept": "application/json",
#     # Optional but often required off-campus:
#     # "X-ELS-Insttoken": INST_TOKEN,
# }

# url = "https://api.elsevier.com/content/search/scopus"
# params = {
#     "query": 'TITLE-ABS-KEY("photovoltaic" AND reliability) AND PUBYEAR > 2020',
#     "view": "COMPLETE",
#     "count": 25,
#     "cursor": "*",  # start cursor-based pagination
# }

# items = []
# while True:
#     r = requests.get(url, headers=headers, params=params, timeout=60)
#     r.raise_for_status()
#     data = r.json()["search-results"]

#     entries = data.get("entry", [])
#     for e in entries:
#         items.append(
#             {
#                 "eid": e.get("eid"),
#                 "title": e.get("dc:title"),
#                 "doi": e.get("prism:doi"),
#                 "coverDate": e.get("prism:coverDate"),
#                 "publicationName": e.get("prism:publicationName"),
#                 "citedby_count": e.get("citedby-count"),
#             }
#         )

#     # get next cursor (if any)
#     next_links = [l for l in data.get("link", []) if l.get("@ref") == "next"]
#     if not next_links:
#         break
#     # when using 'link' pagination, pass 'cursor' param from 'next' href querystring:
#     next_href = next_links[0]["@href"]
#     params = {**params, "cursor": next_href.split("cursor=")[1]}

# pd.DataFrame(items).to_csv("scopus_results.csv", index=False)
