"""Filter NLP phrases"""

# import os
# import pathlib

# import pandas as pd  # type: ignore
# import requests
# from nltk.stem import PorterStemmer  # type: ignore

# from ..._message import message


# def filter_nlp_phrases(root_dir):
#     """
#     :meta private:
#     """

#     def read_all_nlp_phrases(root_dir):
#         #
#         # Get nlp phrase appareances from all files
#         databases_dir = pathlib.Path(root_dir) / "databases"
#         nlp_phrases = pd.Series()
#         for column in [
#             "raw_keywords",
#             "raw_title_nlp_phrases",
#             "raw_abstract_nlp_phrases",
#         ]:
#             files = list(databases_dir.glob("_*.zip"))
#             for file in files:
#                 data = pd.read_csv(file, encoding="utf-8", compression="zip")
#                 if column not in data.columns:
#                     continue
#                 file_nlp_phrases = data[column].dropna()
#                 file_nlp_phrases = file_nlp_phrases.dropna().str.split(";").explode().str.strip()
#                 nlp_phrases = pd.concat([nlp_phrases, file_nlp_phrases])

#         return nlp_phrases

#     def read_main_nlp_phrases(root_dir):
#         #
#         # Get nlp phrase appareances from all files
#         file = pathlib.Path(root_dir) / "databases/_main.csv.zip"
#         nlp_phrases = pd.Series()
#         for column in [
#             "raw_keywords",
#             "raw_title_nlp_phrases",
#             "raw_abstract_nlp_phrases",
#         ]:
#             data = pd.read_csv(file, encoding="utf-8", compression="zip")
#             if column not in data.columns:
#                 continue
#             file_nlp_phrases = data[column].dropna()
#             file_nlp_phrases = file_nlp_phrases.dropna().str.split(";").explode().str.strip()
#             nlp_phrases = pd.concat([nlp_phrases, file_nlp_phrases])

#         return nlp_phrases.drop_duplicates().to_list()

#     def select_stopwords_from_nlp_phrases(nlp_phrases):
#         #
#         # Transforms the pandas series to a data frame
#         nlp_phrases = nlp_phrases.copy()
#         nlp_phrases = nlp_phrases.to_frame()
#         nlp_phrases.columns = ["nlp_phrase"]

#         #
#         # Computes the fingerprint key
#         stemmer = PorterStemmer()

#         nlp_phrases["fingerprint"] = nlp_phrases["nlp_phrase"].str.translate(str.maketrans("-", " "))
#         nlp_phrases["fingerprint"] = nlp_phrases["fingerprint"].str.split(" ")
#         #
#         # ***
#         nlp_phrases["fingerprint"] = nlp_phrases["fingerprint"].map(lambda x: [stemmer.stem(w) for w in x])
#         # nlp_phrases["fingerprint"] = nlp_phrases["fingerprint"].swifter.apply(
#         #     lambda x: [stemmer.stem(w) for w in x]
#         # )
#         #
#         #
#         nlp_phrases["fingerprint"] = nlp_phrases["fingerprint"].map(set)
#         nlp_phrases["fingerprint"] = nlp_phrases["fingerprint"].map(sorted)
#         nlp_phrases["fingerprint"] = nlp_phrases["fingerprint"].map(" ".join)
#         nlp_phrases["OCC"] = 1

#         #
#         # Computes the occurrences and select terms with occ > 1
#         nlp_phrases["appareances"] = nlp_phrases.groupby("fingerprint")["OCC"].transform("sum")
#         stopword_nlp_phrases = nlp_phrases.loc[nlp_phrases["appareances"] < 2, :]
#         stopword_nlp_phrases = stopword_nlp_phrases.nlp_phrase.drop_duplicates().to_list()

#         return stopword_nlp_phrases

#     def get_nlp_stopwords_from_github(nlp_phrases):
#         owner = "jdvelasq"
#         repo = "techminer2"
#         path = "settings/nlp_stopwords.txt"
#         url = f"https://raw.githubusercontent.com/{owner}/{repo}/main/{path}"

#         response = requests.get(url, timeout=5)
#         github_stopwords = response.text.split("\n")
#         github_stopwords = [org.strip() for org in github_stopwords]
#         github_stopwords = [w for w in github_stopwords if w in nlp_phrases]
#         return github_stopwords

#     def save_to_stopwords_txt_file(root_dir, stopwords):
#         #
#         # Reads the current content of the stopwords.txt
#         file_path = os.path.join(root_dir, "stopwords.txt")
#         with open(file_path, "r", encoding="utf-8") as file:
#             content = file.readlines()
#         content = [w.strip() for w in content]

#         #
#         # Adds the current stopwords to the file
#         content += stopwords
#         content = sorted(set(content))

#         #
#         # Updates the stopwords.txt file
#         with open(file_path, "w", encoding="utf-8") as file:
#             file.write("\n".join(content))

#     def extract_countries_from_nlp_phrases(nlp_phrases):
#         #
#         # Loads country codes from GitHub
#         owner = "jdvelasq"
#         repo = "techminer2"
#         path = "settings/country_codes.txt"
#         url = f"https://raw.githubusercontent.com/{owner}/{repo}/main/{path}"
#         response = requests.get(url, timeout=5)
#         country_codes = response.text

#         #
#         # Extracts country names from the country codes
#         country_codes = country_codes.split("\n")
#         countries = []
#         for line in country_codes:
#             if line[0] == " ":
#                 countries.append(line.strip())

#         #
#         # Selects countries in nlp phrases
#         countries = [w.upper().replace(" ", "_") for w in countries]
#         countries = [country for country in countries if country in nlp_phrases]

#         return countries

#     #
#     # MAIN CODE:
#     #
#     # The methodology is based on Emergence scoring to identify frontier R&D
#     # topics and key players, Porter et al (2019) Technological Forecasting
#     # & Social Change.
#     #

#     message("Filtering nlp phrases")

#     #
#     # Selects the stopwords from GitHub and countries using only
#     # nlp phrases on main
#     main_nlp_phrases = read_main_nlp_phrases(root_dir)
#     stopwords = get_nlp_stopwords_from_github(main_nlp_phrases)
#     stopwords += extract_countries_from_nlp_phrases(main_nlp_phrases)

#     #
#     # Selects stopwords by frequency using all databases
#     all_nlp_phrases = read_all_nlp_phrases(root_dir)
#     candidate_stopwords = select_stopwords_from_nlp_phrases(all_nlp_phrases)
#     candidate_stopwords = [w for w in candidate_stopwords if w in main_nlp_phrases]

#     save_to_stopwords_txt_file(root_dir, stopwords)
