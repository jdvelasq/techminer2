import os

import pandas as pd

from ..utils import logging
from .porter_stemmer import porter_stemmer
from .thesaurus import Thesaurus, load_file_as_dict, text_clustering


def create_keywords_thesaurus(directory):
    """
    Createa a keywords thesaurus from the keywords in the articles.

    """
    logging.info("Creating keywords thesaurus ...")

    # --------------------------------------------------------------------------
    # Loads documents.csv
    filename = os.path.join(directory, "documents.csv")
    if not os.path.isfile(filename):
        raise FileNotFoundError(f"The file '{filename}' does not exist.")
    data = pd.read_csv(filename, sep=",", encoding="utf-8")
    # --------------------------------------------------------------------------

    thesaurus_file = os.path.join(directory, "keywords.txt")

    words_list = []

    if "raw_author_keywords" in data.columns:
        words_list += data.raw_author_keywords.tolist()

    if "raw_index_keywords" in data.columns:
        words_list += data.raw_index_keywords.tolist()

    if "raw_nlp_document_title" in data.columns:
        words_list += data.raw_nlp_document_title.tolist()

    if "raw_nlp_abstract" in data.columns:
        words_list += data.raw_nlp_abstract.tolist()

    #
    # Rules for keywords
    #
    words_list = [words for words in words_list if not pd.isna(words)]
    words_list = [word for words in words_list for word in words.split(";")]
    words_list = [word for word in words_list if len(word.strip()) > 2]
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

    if os.path.isfile(thesaurus_file):

        #  Loads existent thesaurus
        dict_ = load_file_as_dict(thesaurus_file)

        #  Selects the new words to cluster
        clustered_words = [word for word in dict_.values()]
        print(clustered_words[:5])
        words_list = [word for word in words_list if word not in clustered_words]

        if len(words_list) > 0:

            th = text_clustering(pd.Series(words_list))

            # old_values = list([value for values in dict_.values() for value in values])

            # for key, values in th._thesaurus.items():
            #     if key in old_values:
            #         print(key, values)
            #         old_key = {k: v for k, v in dict_.items() if key in v}
            #         old_key = list(old_key.keys())[0]
            #         dict_[old_key].extend(values)
            #         dict_[old_key] = list(set(dict_[old_key]))

            th = Thesaurus(
                x={**th._thesaurus, **dict_},
                ignore_case=True,
                full_match=False,
                use_re=False,
            )
            th.to_textfile(thesaurus_file)

    else:
        #
        # Creates a new thesaurus
        #
        text_clustering(pd.Series(words_list)).to_textfile(thesaurus_file)

    logging.info(f"Thesaurus file '{thesaurus_file}' created.")
