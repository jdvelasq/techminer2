def extract_noun_phrases(input_col, output_col, directory):

    pass


def _process__document_title__NLP___column(documents):
    documents = documents.copy()
    documents.document_title = documents.document_title.map(
        lambda x: x[0 : x.find("[")] if pd.isna(x) is False and x[-1] == "]" else x
    )
    # ---------------------------------------------------------------------
    module_path = os.path.dirname(__file__)
    file_path = os.path.join(module_path, "files/nlp_phrases.txt")
    with open(file_path, "r", encoding="utf-8") as file:
        nlp_stopwords = [line.strip() for line in file]
    # ---------------------------------------------------------------------
    documents = documents.assign(
        raw_nlp_document_title=documents.document_title.map(
            lambda x: "; ".join(
                [
                    phrase
                    for phrase in TextBlob(x).noun_phrases
                    if phrase not in nlp_stopwords and _check_nlp_phrase(phrase) is True
                ]
            )
            if pd.isna(x) is False
            else x
        )
    )
    return documents


# def _create__nlp_phrases__column(documents):
#     # -----------------------------------------------------------------------------------
#     def augment_list(documents, topics):
#         documents = documents.copy()
#         topics = topics.str.split(";")
#         topics = topics.map(
#             lambda x: [w.strip() for w in x] if isinstance(x, list) else x
#         )
#         documents = documents.assign(
#             raw_nlp_phrases=documents.raw_nlp_phrases
#             + topics.map(lambda x: x if isinstance(x, list) else [])
#         )
#         return documents

#     # -----------------------------------------------------------------------------------
#     documents = documents.assign(raw_nlp_phrases=[[] for _ in range(len(documents))])

#     if "raw_index_keywords" in documents.columns:
#         documents = augment_list(
#             documents=documents, topics=documents.raw_index_keywords.copy()
#         )

#     if "raw_author_keywords" in documents.columns:
#         documents = augment_list(
#             documents=documents, topics=documents.raw_author_keywords.copy()
#         )

#     if "raw_nlp_document_title" in documents.columns:
#         documents = augment_list(
#             documents=documents, topics=documents.raw_nlp_document_title.copy()
#         )

#     if "raw_nlp_abstract" in documents.columns:
#         documents = augment_list(
#             documents=documents, topics=documents.raw_nlp_abstract.copy()
#         )

#     documents.raw_nlp_phrases = documents.raw_nlp_phrases.map(
#         lambda x: "; ".join(sorted(set(x))) if isinstance(x, list) else x
#     )

#     documents.raw_nlp_phrases = documents.raw_nlp_phrases.map(
#         lambda x: pd.NA if len(x) == 0 else x
#     )

#     return documents


def _process__abstract__column____(documents):
    if "abstract" in documents.columns:
        # ---------------------------------------------------------------------
        module_path = os.path.dirname(__file__)
        file_path = os.path.join(module_path, "files/nlp_phrases.txt")
        with open(file_path, "r", encoding="utf-8") as file:
            nlp_stopwords = [line.strip() for line in file]
        # ---------------------------------------------------------------------
        documents = documents.copy()
        documents.abstract = documents.abstract.str.lower()
        documents.loc[
            documents.abstract == "[no abstract available]", "abstract"
        ] = pd.NA
        documents.abstract = documents.abstract.map(
            lambda x: x[0 : x.find("\u00a9")] if not pd.isna(x) else x
        )
        documents = documents.assign(
            raw_nlp_abstract=documents.abstract.map(
                lambda x: "; ".join(
                    [
                        phrase
                        for phrase in TextBlob(x).noun_phrases
                        if phrase not in nlp_stopwords
                        and _check_nlp_phrase(phrase) is True
                    ]
                )
                if pd.isna(x) is False
                else x
            )
        )
    return documents
