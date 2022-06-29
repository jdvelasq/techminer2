def _check_nlp_phrase(phrase):

    valid_tag_types = [
        ["JJ", "JJ", "NN"],
        ["JJ", "JJ", "NNS"],
        ["JJ", "NN", "NN", "NN"],
        ["JJ", "NN", "NN"],
        ["JJ", "NN", "NNS"],
        ["JJ", "NN"],
        ["JJ", "NNS", "NN"],
        ["JJ", "NNS"],
        ["JJ"],
        ["NN", "CC", "NN"],
        ["NN", "CD"],
        ["NN", "IN", "NN"],
        ["NN", "IN", "NNS"],
        ["NN", "JJ", "NN"],
        ["NN", "NN", "NN"],
        ["NN", "NN", "NNS"],
        ["NN", "NN"],
        ["NN", "NNS"],
        ["NN", "TO", "VB"],
        ["NN", "VBG"],
        ["NN"],
        ["VBG", "NN"],
        ["VBG", "NNS"],
        ["VBG"],
        ["VBN", "NN", "NN"],
        ["VBN", "NN"],
    ]

    if phrase[0] in string.punctuation:
        return False

    if phrase[0].isdigit():
        return False

    tags = [tag[1] for tag in TextBlob(phrase).tags]

    if tags not in valid_tag_types:
        return False

    return True


# def extract_nlp_to_check():
#     if "abstract" in documents.columns:
#         # ---------------------------------------------------------------------
#         module_path = os.path.dirname(__file__)
#         file_path = os.path.join(module_path, "files/nlp_phrases.txt")
#         with open(file_path, "r", encoding="utf-8") as file:
#             nlp_stopwords = [line.strip() for line in file]
#         # ---------------------------------------------------------------------
#         documents = documents.copy()
#         documents = documents.assign(
#             raw_nlp_abstract=documents.abstract.map(
#                 lambda x: "; ".join(
#                     [
#                         phrase
#                         for phrase in TextBlob(x).noun_phrases
#                         if phrase not in nlp_stopwords
#                         and _check_nlp_phrase(phrase) is True
#                     ]
#                 )
#                 if pd.isna(x) is False
#                 else x
#             )
#         )
#     return documents
