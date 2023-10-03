# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Find Similar Records
===============================================================================




>>> from techminer2.search import tfidf_find_similar_phrases
>>> tfidf_find_similar_phrases(
...     text=(
...         "whilst the PRINCIPAL_REGULATORY_OBJECTIVES (e.g., FINANCIAL_STABILITY, "
...         "PRUDENTIAL_SAFETY and soundness, CONSUMER_PROTECTION and MARKET_INTEGRITY, "
...         "and MARKET_COMPETITION and DEVELOPMENT) remain, their means of application "
...         "are increasingly inadequate."
...     ),
...     top_n=3,
...     #
...     # DATABASE PARAMS:
...     root_dir="example/", 
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )


>>> tfidf_find_similar_phrases(
...     text=(
...         "Butler (2019) emphasizes the importance of semantic standards in realizing "
...         "the full benefits of RegTech, as demonstrated by initiatives like the Bank "
...         "of England/FCA RegTech Sprint."
...     ),
...     top_n=3,
...     #
...     # DATABASE PARAMS:
...     root_dir="example/", 
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )


>>> text = (
...    "They highlight the limited adoption of Regulatory Technology (RegTech) and "
...    "Electronic Signatures in Palestine's banking sector, proposing the establishment "
...    "of an independent Electronic Transactions Unit as a solution. They emphasize the "
...    "need for RegTech in achieving regulatory compliance, risk management, and reporting "
...    "in the face of changing regulations and digital dynamics. Additionally, the papers "
...    "delve into ethical concerns surrounding the application of Artificial Intelligence (AI) "
...    "in finance and suggest that RegTech, combined with Islamic finance principles, can "
...    "mitigate these ethical issues. Overall, the papers underscore the transformative "
...    "potential of RegTech while discussing its benefits, challenges, and implications "
...    "for diverse sectors, ultimately aiming to improve compliance, efficiency, and ethical "
...    "practices in the financial industry."
... )
>>> text = text.split(".")
>>> for phrase in text:
...     print("=" * 100)
...     print(phrase.strip())
...     tfidf_find_similar_phrases(
...         text=phrase.strip(),
...         top_n=5,
...         #
...         # DATABASE PARAMS:
...         root_dir="data/regtech/",
...         database="main",
...         year_filter=(None, None),
...         cited_by_filter=(None, None),
...    )






"""
import os
import os.path
import re
import textwrap

import pandas as pd
from nltk.stem import PorterStemmer
from sklearn.metrics.pairwise import cosine_similarity
from textblob import TextBlob

from .._common._read_records import read_records
from .._common.thesaurus_lib import load_system_thesaurus_as_dict_reversed

TEXTWRAP_WIDTH = 73
THESAURUS_FILE = "words.txt"


def tfidf_find_similar_phrases(
    text,
    top_n=5,
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=None,
    cited_by_filter=None,
    **filters,
):
    """
    :meta private:
    """

    if text.strip() == "":
        return

    #
    # Prepare abstracts

    records = read_records(
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    records = extract_sentences(records)
    ### records = remove_stopwords(records)
    ### records = apply_thesaurus_to_abstract(root_dir, records)
    records = remove_duplicated_words(records)
    ### records = apply_porter_stemmer(records)

    records["phrase_no"] = range(len(records))
    tf_matrix = records.explode("abstract")
    tf_matrix = build_tf_matrix(tf_matrix)

    #
    # Prepare text
    words = prepare_text(root_dir, text)
    # words = apply_thesaurus_to_text(root_dir, words)
    words = [w for w in words if w in tf_matrix.columns]

    df_text = pd.DataFrame(data=[[0] * len(tf_matrix.columns)], columns=tf_matrix.columns)
    for word in words:
        df_text[word] = 1

    similarity = cosine_similarity(tf_matrix, df_text)
    similarity = [s[0] for s in similarity]
    records["similarity"] = similarity

    records = records.sort_values(by="similarity", ascending=False)
    records = records[records["similarity"] > 0.0]

    for _, row in records.head(top_n).iterrows():
        print("-" * 100)
        print("SIMILARITY: " + str(round(row.similarity, 3)))
        print("AR: " + row.article)
        print("TI: " + row.title)
        print()
        print(textwrap.fill(str(row.phrase), width=TEXTWRAP_WIDTH))
        print()


def apply_thesaurus_to_text(root_dir, words):
    """
    :meta private:
    """
    thesaurus = load_thesaurus(root_dir)
    words = [thesaurus[w] if w in thesaurus else w for w in words]
    return words


def load_thesaurus(root_dir):
    th_file = os.path.join(root_dir, THESAURUS_FILE)
    if not os.path.isfile(th_file):
        raise FileNotFoundError(f"The file {th_file} does not exist.")
    thesaurus = load_system_thesaurus_as_dict_reversed(th_file)
    return thesaurus


def prepare_text(root_dir, text):
    """
    :meta private:
    """

    #
    # Obtains a regex for descriptors
    thesaurus = load_thesaurus(root_dir)
    descriptors = list(thesaurus.values())
    descriptors = [d.translate(str.maketrans("_", " ")) for d in descriptors]
    descriptors = [d.lower().strip() for d in descriptors]
    descriptors = sorted(descriptors, key=lambda x: len(x.split(" ")), reverse=True)
    descriptors = [re.escape(d) for d in descriptors]
    descriptors = "|".join(descriptors)
    regex = re.compile(r"\b(" + descriptors + r")\b")

    #
    # Highlight the text with the descriptors
    text = text.lower().replace("_", " ")
    #### text = re.sub(regex, lambda z: z.group().upper().replace(" ", "_"), text)

    #
    # Obtain the words in the phase
    words = TextBlob(text).sentences[0].words

    #
    # Load and prepare the stopwords
    ### stopwords = load_stopwords()
    ### stopwords = [word.lower() for word in stopwords]

    ### words = [w for w in words if w not in stopwords]
    ### words = [w for w in words if w[0] not in "0123456789"]
    words = [w.replace("'", "") for w in words]
    ### words = [w for w in words if len(w) > 2]

    #
    # Apply Porter Stemmer
    ### stemmer = PorterStemmer()
    ### words = sorted(set(stemmer.stem(word) if word == word.lower() else word for word in words))

    return words


def apply_thesaurus_to_abstract(root_dir, records):
    """
    :meta private:
    """
    thesaurus = load_thesaurus(root_dir)
    records["abstract"] = records["abstract"].apply(
        lambda words: [thesaurus[w] if w in thesaurus else w for w in words]
    )
    return records


def apply_porter_stemmer(records):
    """
    :meta private:
    """
    stemmer = PorterStemmer()
    records["abstract"] = records["abstract"].apply(
        lambda x: sorted(set(stemmer.stem(w) if w == w.lower() else w for w in x))
    )
    return records


def build_tf_matrix(records):
    """
    :meta private:
    """
    records = records.copy()
    records["OCC"] = 1
    records = records.pivot(index="phrase_no", columns="abstract", values="OCC")
    records = records.fillna(0)
    return records


def remove_duplicated_words(records):
    """
    :meta private:
    """
    records["abstract"] = records["abstract"].apply(lambda x: sorted(set(x)))
    return records


def load_stopwords():
    """
    :meta private:
    """
    module_path = os.path.dirname(__file__)
    file_path = os.path.join(module_path, "../word_lists/stopwords.txt")
    with open(file_path, "r", encoding="utf-8") as file:
        stopwords = file.read().split("\n")
    stopwords = [w.strip() for w in stopwords]
    stopwords = [w for w in stopwords if w != ""]
    return stopwords


def remove_stopwords(records):
    """
    :meta private:
    """
    stopwords = load_stopwords()
    stopwords = [word.lower() for word in stopwords]
    records["abstract"] = records["abstract"].apply(
        lambda words: [w for w in words if w not in stopwords]
    )

    records["abstract"] = records["abstract"].apply(
        lambda words: [w for w in words if w[0] not in "0123456789"]
    )

    records["abstract"] = records["abstract"].apply(
        lambda words: [w.replace("'", "") for w in words]
    )

    records["abstract"] = records["abstract"].apply(lambda words: [w for w in words if len(w) > 2])

    return records


def extract_sentences(records):
    """
    :meta private:
    """
    abstracts = records[["article", "title", "abstract"]].dropna()

    #
    #
    #
    abstracts["abstract"] = abstracts["abstract"].str.lower().str.replace("_", " ")
    #
    #
    #

    abstracts["abstract"] = abstracts["abstract"].apply(
        lambda paragraph: TextBlob(paragraph).sentences
    )
    abstracts = abstracts.explode("abstract")
    abstracts["phrase"] = abstracts["abstract"]
    abstracts["abstract"] = abstracts["abstract"].apply(lambda sentence: sentence.words)

    return abstracts
