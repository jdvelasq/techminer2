import os

import pandas as pd

from . import logging
from .load_all_documents import load_all_documents
from .thesaurus import Thesaurus, read_textfile, text_clustering


def create_keywords_thesaurus(directory, use_nlp_phrases=False):
    """
    Createa a keywords thesaurus from the keywords in the articles.

    """
    logging.info("Creating keywords thesaurus ...")

    # --------------------------------------------------------------------------
    data = load_all_documents(directory)
    # --------------------------------------------------------------------------

    words_list = []

    if "raw_author_keywords" in data.columns:
        words_list += data.raw_author_keywords.tolist()

    if "raw_index_keywords" in data.columns:
        words_list += data.raw_index_keywords.tolist()

    if "raw_nlp_document_title" in data.columns and use_nlp_phrases:
        words_list += data.raw_nlp_document_title.tolist()

    if "raw_nlp_abstract" in data.columns and use_nlp_phrases:
        words_list += data.raw_nlp_abstract.tolist()

    #
    # Rules for keywords
    #
    words_list = [words for words in words_list if not pd.isna(words)]
    words_list = [word for words in words_list for word in words.split(";")]
    words_list = [word.strip() for word in words_list]
    words_list = [word for word in words_list if len(word) > 1]
    words_list = [
        word.replace('"', "")
        .replace(chr(8212), "")
        .replace(chr(8220), "")
        .replace(chr(8221), "")
        for word in words_list
    ]
    words_list = [
        word.replace("-", "") if word[0] == "-" and len(word) > 1 else word
        for word in words_list
    ]

    # ----< new algorithm >----------------------------------------------------
    # {palabra: clave_del_grupo}
    new_th = text_clustering(pd.Series(words_list)).to_dict()

    thesaurus_file = os.path.join(directory, "processed", "keywords.txt")
    if os.path.isfile(thesaurus_file):
        old_th = read_textfile(thesaurus_file).to_dict()
        new_th = {**new_th, **old_th}

    keys = list(set(new_th.values()))

    th = {key: [] for key in keys}

    for key, value in new_th.items():
        th[value].append(key)

    Thesaurus(
        x=th,
        ignore_case=True,
        full_match=False,
        use_re=False,
    ).to_textfile(thesaurus_file)

    logging.info(f"Thesaurus file '{thesaurus_file}' created.")
