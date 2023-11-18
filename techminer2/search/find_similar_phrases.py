# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Find Similar Phrases
===============================================================================




>>> from techminer2.search import find_similar_phrases
>>> find_similar_phrases(
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
TI: FINTECH, REGTECH, and the RECONCEPTUALIZATION of FINANCIAL_REGULATION
<BLANKLINE>
whilst the PRINCIPAL_REGULATORY_OBJECTIVES (e.g., FINANCIAL_STABILITY,
PRUDENTIAL_SAFETY and SOUNDNESS, CONSUMER_PROTECTION and
MARKET_INTEGRITY, and MARKET_COMPETITION and DEVELOPMENT) remain, their
MEANS of APPLICATION are increasingly inadequate.
<BLANKLINE>
----------------------------------------------------------------------------------------------------
SIMILARITY: 0.252
AR: Hu Z., 2019, SYMMETRY, V11
TI: ADOPTION_INTENTION of FINTECH_SERVICES for BANK_USERS: an EMPIRICAL_EXAMINATION with an extended TECHNOLOGY_ACCEPTANCE_MODEL
<BLANKLINE>
along with the DEVELOPMENT of FINTECH, many SCHOLARS have studied how
INFORMATION_TECHNOLOGY is applied to FINANCIAL_SERVICES with a FOCUS on
extended METHODS for APPLICATION.
<BLANKLINE>
----------------------------------------------------------------------------------------------------
SIMILARITY: 0.252
AR: Jagtiani J., 2018, J ECON BUS, V100, P1
TI: FINTECH: the IMPACT on CONSUMERS and REGULATORY_RESPONSES
<BLANKLINE>
REGULATORS around the GLOBE are working diligently and thoughtfully to
provide CONSUMER_PROTECTION and to maintain FINANCIAL_STABILITY while at
the same TIME to create an ENVIRONMENT for SAFE_FINTECH_INNOVATIONS.
<BLANKLINE>


"""
import os
import os.path
import re
import textwrap

import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity  # type: ignore
from textblob import TextBlob  # type: ignore

from .._common.thesaurus_lib import load_system_thesaurus_as_dict_reversed
from ..read_records import read_records
from .extract_descriptors_from_text import extract_descriptors_from_text

TEXTWRAP_WIDTH = 73
THESAURUS_FILE = "thesauri/words.the.txt"


def find_similar_phrases(
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

    records = _extract_keywords(records, root_dir)
    records["phrase_no"] = range(len(records))
    tf_matrix = records.explode("keyword")
    tf_matrix = _build_tf_matrix(tf_matrix)

    #
    # Prepare text
    words = extract_descriptors_from_text(text, root_dir)

    df_text = pd.DataFrame(
        data=[[0] * len(tf_matrix.columns)], columns=tf_matrix.columns
    )
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


def _load_thesaurus(root_dir):
    th_file = os.path.join(root_dir, THESAURUS_FILE)
    if not os.path.isfile(th_file):
        raise FileNotFoundError(f"The file {th_file} does not exist.")
    thesaurus = load_system_thesaurus_as_dict_reversed(th_file)
    return thesaurus


def _build_tf_matrix(records):
    """
    :meta private:
    """
    records = records.copy()
    records["OCC"] = 1
    records = records.pivot(index="phrase_no", columns="keyword", values="OCC")
    records = records.fillna(0)
    return records


def _extract_keywords(records, root_dir):
    """
    :meta private:
    """

    # -----------------------------------------------------------------------------------------
    # Obtains a regex for descriptors
    thesaurus = _load_thesaurus(root_dir)
    descriptors = list(thesaurus.values())
    descriptors = [d.translate(str.maketrans("_", " ")) for d in descriptors]
    descriptors = [d.lower().strip() for d in descriptors]
    descriptors = sorted(descriptors, key=lambda x: len(x.split(" ")), reverse=True)
    descriptors = [re.escape(d) for d in descriptors]
    descriptors = "|".join(descriptors)
    regex = re.compile(r"\b(" + descriptors + r")\b")
    # -----------------------------------------------------------------------------------------

    abstracts = records[["article", "document_title", "abstract"]].dropna()
    abstracts["abstract"] = abstracts["abstract"].apply(
        lambda paragraph: TextBlob(paragraph).sentences
    )
    abstracts = abstracts.explode("abstract")
    abstracts["phrase"] = abstracts["abstract"]
    abstracts["phrase"] = abstracts["phrase"].map(str)
    abstracts["abstract"] = abstracts["abstract"].map(str)

    # -----------------------------------------------------------------------------------------
    #
    abstracts["abstract"] = abstracts["abstract"].str.lower().str.replace("_", " ")
    abstracts["abstract"] = abstracts["abstract"].apply(
        lambda sentence: re.sub(
            regex, lambda z: z.group().upper().replace(" ", "_"), sentence
        )
    )
    abstracts["abstract"] = abstracts["abstract"].apply(
        lambda text: sorted(set(str(t) for t in TextBlob(text).words))
    )
    abstracts["abstract"] = abstracts["abstract"].apply(
        lambda descriptors: [
            t for t in descriptors if t == t.upper() and t[0] not in "0123456789"
        ]
    )
    #
    # -----------------------------------------------------------------------------------------
    abstracts["abstract"] = abstracts["abstract"].apply(
        lambda x: pd.NA if x == [] else x
    )
    abstracts = abstracts.dropna()
    abstracts = abstracts.rename(columns={"abstract": "keyword"})
    return abstracts
