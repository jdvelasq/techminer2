# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Find Similar Phrases
===============================================================================

## >>> from techminer2.database.search import find_similar_phrases
## >>> documents = find_similar_phrases(
## ...     text=(
## ...         "whilst the PRINCIPAL_REGULATORY_OBJECTIVES (e.g., FINANCIAL_STABILITY, "
## ...         "PRUDENTIAL_SAFETY and soundness, CONSUMER_PROTECTION and MARKET_INTEGRITY, "
## ...         "and MARKET_COMPETITION and DEVELOPMENT) remain, their means of application "
## ...         "are increasingly inadequate."
## ...     ),
## ...     top_n=3,
## ...     #
## ...     # DATABASE PARAMS:
## ...     root_dir="example/",
## ...     database="main",
## ...     year_filter=(None, None),
## ...     cited_by_filter=(None, None),
## ... )
## >>> for i in range(3):
## ...     print(documents[i])
100.0%
AR Arner D.W., 2017, NORTHWEST J INTL LAW BUS, V37, P373
TI FinTech, regTech, and the reconceptualization of financial regulation
AB whilst the PRINCIPAL_REGULATORY_OBJECTIVES ( e.g., FINANCIAL_STABILITY ,
   PRUDENTIAL_SAFETY and soundness , CONSUMER_PROTECTION and MARKET_INTEGRITY ,
   and MARKET_COMPETITION and DEVELOPMENT ) remain , their means of application
   are increasingly inadequate .
<BLANKLINE>
37.8%
AR Jagtiani J., 2018, J ECON BUS, V100, P1
TI Fintech: The Impact on Consumers and Regulatory Responses
AB regulators around the globe are working diligently and thoughtfully to provide
   CONSUMER_PROTECTION and to maintain FINANCIAL_STABILITY while at the same
   time to create an ENVIRONMENT for SAFE_FINTECH_INNOVATIONS .
<BLANKLINE>
37.8%
AR Saksonova S., 2017, EUR RES STUD, V20, P961
TI Fintech as financial innovation - The possibilities and problems of implementation
AB this PAPER_AIMS to evaluate FINTECH_LEVEL of DEVELOPMENT in latvia compared to
   EUROPE .
<BLANKLINE>

"""
import os
import os.path
import re
import textwrap

import pandas as pd  # type: ignore
from sklearn.metrics.pairwise import cosine_similarity  # type: ignore
from textblob import TextBlob  # type: ignore

# from ..database.load.load__database import load__filtered_database
from ...thesaurus._internals.load_reversed_thesaurus_as_mapping import \
    internal__load_reversed_thesaurus_as_mapping
from .deprecated.extract_descriptors_from_text import \
    extract_descriptors_from_text

TEXTWRAP_WIDTH = 79
THESAURUS_FILE = "data/thesaurus/descriptors.the.txt"


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
    """:meta private:"""

    if text.strip() == "":
        return

    #
    # Prepare abstracts

    records = load__filtered_database(
        root_dir=root_dir,
        database=database,
        record_years_range=year_filter,
        record_citations_range=cited_by_filter,
        records_order_by=None,
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

    documents = []
    for _, row in records.iterrows():
        text = str(round(100 * row.similarity, 1)) + "%\n"
        text += "AR " + row.record_id + "\n"
        text += "TI " + row.raw_document_title + "\n"
        text += "AB " + textwrap.fill(
            str(row.phrase),
            width=TEXTWRAP_WIDTH,
            initial_indent="",
            subsequent_indent=" " * 3,
            fix_sentence_endings=True,
        )
        text += "\n"
        documents.append(text)

    return documents


def _load_thesaurus(root_dir):
    th_file = os.path.join(root_dir, THESAURUS_FILE)
    if not os.path.isfile(th_file):
        raise FileNotFoundError(f"The file {th_file} does not exist.")
    thesaurus = internal__load_reversed_thesaurus_as_mapping(th_file)
    return thesaurus


def _build_tf_matrix(records):
    records = records.copy()
    records["OCC"] = 1
    records = records.pivot(index="phrase_no", columns="keyword", values="OCC")
    records = records.fillna(0)
    return records


def _extract_keywords(records, root_dir):

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

    abstracts = records[["record_id", "raw_document_title", "abstract"]].dropna()
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
