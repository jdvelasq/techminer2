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
----------------------------------------------------------------------------------------------------
SIMILARITY: 1.0
AR: Arner D.W., 2017, NORTHWEST J INTL LAW BUS, V37, P373
TI: FINTECH, REGTECH, and the reconceptualization of FINANCIAL_REGULATION
<BLANKLINE>
whilst the principal regulatory objectives (e.g., financial stability,
prudential safety and soundness, consumer protection and market
integrity, and market competition and development) remain, their means of
application are increasingly inadequate.
<BLANKLINE>
----------------------------------------------------------------------------------------------------
SIMILARITY: 0.302
AR: Anagnostopoulos I., 2018, J ECON BUS, V100, P7
TI: FINTECH and REGTECH: impact on regulators and BANKS
<BLANKLINE>
these should be of interest to regulatory standard setters, investors,
international organisations and other academics who are researching
regulatory and competition issues, and their manifestation within the
financial and social contexts.
<BLANKLINE>
----------------------------------------------------------------------------------------------------
SIMILARITY: 0.277
AR: Arner D.W., 2017, NORTHWEST J INTL LAW BUS, V37, P373
TI: FINTECH, REGTECH, and the reconceptualization of FINANCIAL_REGULATION
<BLANKLINE>
regulatory change and technological developments following the 2008
global financial crisis are changing the nature of financial markets,
services, and institutions.
<BLANKLINE>





"""
import os
import os.path
import re
import textwrap

import pandas as pd  # type: ignore
from nltk.stem import PorterStemmer  # type: ignore
from sklearn.metrics.pairwise import cosine_similarity  # type: ignore
from textblob import TextBlob  # type: ignore

from .._core.read_filtered_database import read_filtered_database
from ..thesaurus._core.load_inverted_thesaurus_as_dict import load_inverted_thesaurus_as_dict

TEXTWRAP_WIDTH = 73
THESAURUS_FILE = "thesauri/descriptors.the.txt"


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
    """:meta private:"""

    if text.strip() == "":
        return

    #
    # Prepare abstracts

    records = read_filtered_database(
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        sort_by=None,
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
        print("TI: " + row.document_title)
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
    thesaurus = load_inverted_thesaurus_as_dict(th_file)
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
    # regex = re.compile(r"\b(" + descriptors + r")\b")

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
    records["abstract"] = records["abstract"].apply(lambda words: [thesaurus[w] if w in thesaurus else w for w in words])
    return records


def apply_porter_stemmer(records):
    """
    :meta private:
    """
    stemmer = PorterStemmer()
    records["abstract"] = records["abstract"].apply(lambda x: sorted(set(stemmer.stem(w) if w == w.lower() else w for w in x)))
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
    records["abstract"] = records["abstract"].apply(lambda words: [w for w in words if w not in stopwords])

    records["abstract"] = records["abstract"].apply(lambda words: [w for w in words if w[0] not in "0123456789"])

    records["abstract"] = records["abstract"].apply(lambda words: [w.replace("'", "") for w in words])

    records["abstract"] = records["abstract"].apply(lambda words: [w for w in words if len(w) > 2])

    return records


def extract_sentences(records):
    """
    :meta private:
    """
    abstracts = records[["article", "document_title", "abstract"]].dropna()

    #
    #
    #
    abstracts["abstract"] = abstracts["abstract"].str.lower().str.replace("_", " ")
    #
    #
    #

    abstracts["abstract"] = abstracts["abstract"].apply(lambda paragraph: TextBlob(paragraph).sentences)
    abstracts = abstracts.explode("abstract")
    abstracts["phrase"] = abstracts["abstract"]
    abstracts["abstract"] = abstracts["abstract"].apply(lambda sentence: sentence.words)

    return abstracts
