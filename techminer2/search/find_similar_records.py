# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Find Similar Records
===============================================================================


>>> from techminer2.search import find_similar_records
>>> find_similar_records(
...     record_no=1,
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
No: 1
AR: Goldstein I., 2019, REV FINANC STUD, V32, P1647
TI: to FINTECH and beyond
<BLANKLINE>
FINTECH is about the introduction of NEW_TECHNOLOGIES into the
FINANCIAL_SECTOR, and IT is now revolutionizing the FINANCIAL_INDUSTRY.
in 2017, when the academic FINANCE COMMUNITY was not actively researching
FINTECH, the EDITORIAL_TEAM of the REVIEW of FINANCIAL_STUDIES launched a
COMPETITION to develop RESEARCH_PROPOSALS focused on this topic. this
SPECIAL_ISSUE is the result. in this INTRODUCTORY_ARTICLE, we describe
the RECENT_FINTECH_PHENOMENON and the NOVEL_EDITORIAL_PROTOCOL employed
for this SPECIAL_ISSUE following the registered reports format.we discuss
what we learned from the submitted proposals about the field of FINTECH
and which ones we selected to be completed and ultimately come out in
this SPECIAL_ISSUE. we also provide several observations to help guide
FUTURE_RESEARCH in the emerging area of FINTECH. (JEL_G00, G21, g23, G28,
l51, o31).  the author(s) 2019.
<BLANKLINE>
----------------------------------------------------------------------------------------------------
SIMILARITY: 0.217
No: 32
AR: Zavolokina L., 2016, INT CONF INF SYST ICIS
TI: FINTECH   what's in a name?
<BLANKLINE>
FINTECH, the word which originates from marriage of "FINANCE" and
"TECHNOLOGY", designates currently a novel, innovative and emerging field
which ATTRACTS_ATTENTION from the publicity. at the moment there is no
UNIVERSAL_UNDERSTANDING and DEFINITION of FINTECH in the RESEARCH,
however, the topic is widely addressed by the english_ and
german_speaking press. in this study we aim to make insights into how the
press and other POPULAR_MEDIA understand and FRAME_FINTECH, discussing
definitions that represents the meaning of IT for the press, and deliver
the CONCEPTUAL_FRAMEWORK to be used in RESEARCH and
SCIENTIFIC_LITERATURE. in doing so, we also IDENTIFY_DRIVERS of FINTECH
and put them in the CONTEXT of financial and DIGITAL_INNOVATION_RESEARCH.
thereby, we provide OBJECTIVE_UNDERSTANDING of FINTECH, how IT is
reflected in the POPULAR_MEDIA.
<BLANKLINE>
----------------------------------------------------------------------------------------------------
SIMILARITY: 0.217
No: 3
AR: Zavolokina L., 2016, FINANCIAL INNOV, V2
TI: the FINTECH_PHENOMENON: antecedents of FINANCIAL_INNOVATION perceived by the POPULAR_PRESS
<BLANKLINE>
the FINANCIAL_INDUSTRY has been strongly influenced by DIGITALIZATION in
the past few years reflected by the emergence of FINTECH, which
represents the marriage of FINANCE and INFORMATION_TECHNOLOGY. FINTECH
provides OPPORTUNITIES for the creation of NEW_SERVICES and
BUSINESS_MODELS and poses challenges to
TRADITIONAL_FINANCIAL_SERVICE_PROVIDERS. therefore, FINTECH has become a
subject of debate among practitioners, investors, and researchers and is
highly visible in the POPULAR_MEDIA. in this study, we unveil the DRIVERS
motivating the FINTECH_PHENOMENON perceived by the english and german
POPULAR_PRESS including the subjects discussed in the CONTEXT of FINTECH.
this study is the first one to reflect the MEDIA_PERSPECTIVE on the
FINTECH_PHENOMENON in the RESEARCH. in doing so, we extend the growing
KNOWLEDGE on FINTECH and contribute to a COMMON_UNDERSTANDING in the
financial and DIGITAL_INNOVATION_LITERATURE. these STUDY_CONTRIBUTES to
RESEARCH in the areas of INFORMATION_SYSTEMS, FINANCE and
interdisciplinary SOCIAL_SCIENCES. moreover, IT brings VALUE to
practitioners (ENTREPRENEURS, investors, regulators, etc.), who explore
the field of FINTECH.  2016, the author(s).
<BLANKLINE>


"""
import textwrap

from nltk.stem import WordNetLemmatizer
from sklearn.metrics.pairwise import cosine_similarity
from textblob import TextBlob

from .._core.read_filtered_database import read_filtered_database

TEXTWRAP_WIDTH = 73


def find_similar_records(
    record_no,
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

    #
    # Load the abstracts
    records = read_filtered_database(
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        sort_by=None,
        **filters,
    )
    records = records.dropna(subset=["abstract"])

    #
    #
    records["paragraph"] = records["abstract"].copy()
    records["paragraph"] = records["paragraph"].str.lower()

    records = records.loc[records.paragraph != "[no abstract available]", :]

    records["paragraph"] = records["paragraph"].str.replace("_", " ")

    #
    #
    records = paragraph_to_meaningful_words(records)
    tf_matrix = build_tf_matrix(records)
    similarity = cosine_similarity(tf_matrix, tf_matrix.loc[record_no:record_no, :])
    records["similarity"] = similarity
    records = records.sort_values(by="similarity", ascending=False)
    records = records[records["similarity"] > 0.0]
    records = records.head(top_n)

    for _, row in records.head(top_n).iterrows():
        print("-" * 100)
        print("SIMILARITY: " + str(round(row.similarity, 3)))
        print("No: " + str(row.art_no))
        print("AR: " + row.article)
        print("TI: " + row.document_title)
        print()
        print(textwrap.fill(str(row.abstract), width=TEXTWRAP_WIDTH))
        print()


def paragraph_to_meaningful_words(records):
    """
    :meta private:
    """

    lemmatizer = WordNetLemmatizer()

    def to_lemma(tag):
        if tag[1][:2] == "NN":
            return (lemmatizer.lemmatize(tag[0], pos="n"), tag[1])

        if tag[1][:2] == "VB":
            return (lemmatizer.lemmatize(tag[0], pos="v"), tag[1])

        if tag[1][:2] == "RB":
            return (lemmatizer.lemmatize(tag[0], pos="r"), tag[1])

        if tag[1][:2] == "JJ":
            return (lemmatizer.lemmatize(tag[0], pos="a"), tag[1])

    records = records.copy()
    records = records[["art_no", "article", "document_title", "abstract", "paragraph"]].dropna()

    #
    # Split the  abstract in sentences
    records["paragraph"] = records["paragraph"].apply(lambda paragraph: TextBlob(paragraph).sentences)

    #
    # Extracts the meaningful words from each sentence
    records["paragraph"] = records["paragraph"].apply(lambda sentences: [sentence.tags for sentence in sentences])

    records["paragraph"] = records["paragraph"].apply(
        lambda sentences: [tag for sentence in sentences for tag in sentence if tag[1][:2] in ["NN", "VB", "RB", "JJ"]]
    )

    records["paragraph"] = records["paragraph"].apply(lambda tags: [to_lemma(tag) for tag in tags])

    records["paragraph"] = records["paragraph"].apply(lambda tags: [tag[0] for tag in tags])

    records["paragraph"] = records["paragraph"].apply(set)
    records["paragraph"] = records["paragraph"].apply(sorted)

    return records


def build_tf_matrix(records):
    """
    :meta private:
    """
    records = records.copy()
    records = records.explode("paragraph")
    records["OCC"] = 1
    records = records.pivot(index="art_no", columns="paragraph", values="OCC")
    records = records.fillna(0)
    return records
