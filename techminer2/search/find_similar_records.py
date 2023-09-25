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
...     root_dir="data/regtech/",
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
----------------------------------------------------------------------------------------------------
SIMILARITY: 1.0
No: 1
AR: Teichmann F, 2023, TECHNOL SOC, V72
TI: REGTECH_POTENTIAL_BENEFITS and CHALLENGES for BUSINESSES
<BLANKLINE>
the last GLOBAL_FINANCIAL_CRISIS in 2008 fuelled the NEED for REGULATION
to avoid HISTORY repeating itself. NEW_REGULATORY_TECHNOLOGIES (REGTECH)
are helping to transform how COMPLIANCE_ISSUES are handled. this
STUDY_AIMS to highlight the BENEFITS of REGTECH_SOLUTIONS for COMPANIES
as well as the CHALLENGES of adopting these TECHNOLOGIES. IT also
ADDRESSES the MARKETS in FINANCIAL_INSTRUMENTS_DIRECTIVE (MIFID)
II_LEGISLATION, which has led to an INCREASE in the NUMBER of
REGTECH_COMPANIES. although these SYSTEMS of TECHNOLOGY OFFER COMPELLING
COMPLIANCE_TOOLS, they also pose SIGNIFICANT_RISKS. for this REASON, this
STUDY_AIMS to draw ATTENTION to the OPPORTUNITIES and POTENTIAL_PITFALLS
associated with REGTECH and propose RECOMMENDATIONS for addressing the
CHALLENGES related to IMPLEMENTING REGTECH_SOLUTIONS.  2022 ELSEVIER_LTD
<BLANKLINE>
----------------------------------------------------------------------------------------------------
SIMILARITY: 0.302
No: 45
AR: Butler T, 2018, J RISK MANG FINANCIAL INST, V11, P19
TI: on the ROLE of ontology based REGTECH for MANAGING RISK and COMPLIANCE_REPORTING in the AGE of REGULATION
<BLANKLINE>
this PAPER_ADDRESSES IMPORTANT_QUESTIONS such as: what CHALLENGES are
presented by NEW_REGULATION to BANKS_INFRASTRUCTURE, RISK_MANAGEMENT and
PROFITABILITY, and how can these CHALLENGES be best addressed? IT also
examines the POTENTIAL_IMPACT_FINTECH has on the RISKINESS of BANKS and
proposes REGTECH as the SOLUTION. following a BRIEF_OVERVIEW of the
IMPACT and COSTS of REGULATION since the FINANCIAL_CRISIS, the
PAPER_INTRODUCES_REGTECH in the CONTEXT of CHALLENGES FACING
FINANCIAL_INSTITUTIONS and the LIMITATIONS of GOVERNANCE, RISK and
COMPLIANCE (GRC) SYSTEMS. this PAPERS MAIN_CONTRIBUTION is in its
DELINEATION of a REGULATORY_COMPLIANCE and RISK_ONTOLOGY, the
TECHNOLOGIES that underpin IT and the related OBJECTIVE RISK CONTROL
(ORC) MODEL. the PAPER_ARGUES that these provide a PLATFORM on which
REGTECH can perform EFFECTIVE_RISK_MANAGEMENT and COMPLIANCE_REPORTING in
a global post CRISIS REGULATORY_ENVIRONMENT.  HENRY_STEWART_PUBLICATIONS
1752 8887 (2018).
<BLANKLINE>
----------------------------------------------------------------------------------------------------
SIMILARITY: 0.268
No: 44
AR: Nasir F, 2019, J ADV RES DYN CONTROL SYST, V11, P912
TI: REGTECH as a SOLUTION for COMPLIANCE_CHALLENGE: a REVIEW_ARTICLE
<BLANKLINE>
due to the GLOBAL_FINANCIAL_CRISIS of 2007 2008, several
FINANCIAL_REGULATIONS are BROUGHT by the REGULATORS with high REPORTING
STANDARDS, which are to be followed by FINANCIAL_INSTITUTIONS. every
YEAR, these REQUIREMENTS are increasing and IT has BECOME a CHALLENGE for
FINANCIAL_INSTITUTIONS to meet the REQUIREMENTS manually, due to the
HIGH_COST and increasing NUMBER of COMPLEX_COMPLIANCE_REQUIREMENTS. these
COMPLIANCE CHALLENGES created the MARKET for REGTECH, which is a PART of
FINTECH_INDUSTRY, where the REGTECH_INDUSTRY PROMISE to ACT as a SOLUTION
to reduce COMPLIANCE_COST and BURDEN for FINANCIAL_INSTITUTIONS as well
as REGULATORS. the PURPOSE of this PAPER is to PRESENT a
SYSTEMATIC_LITERATURE_REVIEW conducted, on applying REGTECH to reduce
COMPLIANCE_COST and BURDEN, while focusing on PROMISING_REGTECH_TOOLS and
VARIOUS_BENEFITS and CHALLENGES of REGTECH. the AREA of REGTECH is very
recent, which RESULTS in a GAP in LITERATURE and RESEARCH for the PURPOSE
of this REVIEW. FUTURE_AREAS for RESEARCH are provided in this PAPER.
2019, INSTITUTE of advanced SCIENTIFIC_RESEARCH, INC. all RIGHTS
reserved.
<BLANKLINE>



"""
import textwrap

from nltk.stem import WordNetLemmatizer
from sklearn.metrics.pairwise import cosine_similarity
from textblob import TextBlob

from .._read_records import read_records

TEXTWRAP_WIDTH = 73
THESAURUS_FILE = "words.txt"


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
    """
    :meta private:
    """

    #
    # Load the abstracts
    records = read_records(
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
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
        print("TI: " + row.title)
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
    records = records[["art_no", "article", "title", "abstract", "paragraph"]].dropna()

    #
    # Split the  abstract in sentences
    records["paragraph"] = records["paragraph"].apply(
        lambda paragraph: TextBlob(paragraph).sentences
    )

    #
    # Extracts the meaningful words from each sentence
    records["paragraph"] = records["paragraph"].apply(
        lambda sentences: [sentence.tags for sentence in sentences]
    )

    records["paragraph"] = records["paragraph"].apply(
        lambda sentences: [
            tag
            for sentence in sentences
            for tag in sentence
            if tag[1][:2] in ["NN", "VB", "RB", "JJ"]
        ]
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
