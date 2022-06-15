"""
Abstract Concordances
=========================================================================================

Abstract concordances exploration tool.


>>> from techminer2 import *
>>> directory = "/workspaces/techminer2/data/"
>>> abstract_concordances(
...     'fintech',
...     top_n=10,
...     directory=directory,
... )
                             The industry overall, and many  FINTECH  start-ups are looking for new pathways to successful bu ...
...  able to figure out how to effectively hook up with the  FINTECH  revolution is at stake.
                                           We present a new  FINTECH  innovation mapping approach that enables the assessment ...
... robo-advisory and services influenced by blockchain and  FINTECH  innovations.
... development organisations, philanthropic investment and  FINTECH  companies.
        There is currently no consensus about what the term  FINTECH  means.
... g more than 200 scholarly articles referencing the term  FINTECH  and covering a period of more than 40 years.
... tion concentrates on extracting out the quintessence of  FINTECH  using both spheres.
... rreviewed definitions of the term, it is concluded that  FINTECH  is a new financial industry that applies technology to  ...
                                   Financial technology, or  FINTECH , involves the design and delivery of financial products ...

"""

from .load_abstracts import load_abstracts
from .load_filtered_documents import load_filtered_documents


def abstract_concordances(
    text,
    top_n=50,
    directory="./",
):
    """Checks the occurrence contexts of a given text in the abstract's phrases."""

    abstracts = load_abstracts(directory)
    abstracts = _adds_citations_to_abstracts(abstracts, directory)
    abstracts = _select_abstracts(abstracts, text)
    abstracts = abstracts.head(top_n)
    contexts = _extract_contexts(abstracts, text)
    _print_concordances(contexts, text)


def _print_concordances(contexts, text):
    """Prints the report."""
    for _, row in contexts.iterrows():
        print(f"{row['left_context']:>60} {text.upper()} {row['right_context']}")


def _extract_contexts(abstracts, text):
    text = text.upper()
    regex = r"\b" + text + r"\b"
    contexts = abstracts["text"].str.extract(
        r"(?P<left_context>[\s \S]*)" + regex + r"(?P<right_context>[\s \S]*)"
    )

    contexts["left_context"] = contexts["left_context"].fillna("")
    contexts["right_context"] = contexts["right_context"].fillna("")
    contexts["left_context"] = contexts["left_context"].map(
        lambda x: "... " + x[-56:] if len(x) > 60 else x
    )
    contexts["right_context"] = contexts["right_context"].map(
        lambda x: x[:56] + " ..." if len(x) > 60 else x
    )
    return contexts


def _select_abstracts(abstracts, text):
    """Selects the abstracts."""

    regex = r"\b" + text + r"\b"
    abstracts = abstracts[abstracts.text.str.contains(regex, regex=True)]
    abstracts = abstracts[["record_no", "text"]]
    abstracts["text"] = abstracts["text"].str.capitalize()
    abstracts["text"] = abstracts["text"].str.replace(
        r"\b" + text + r"\b", text.upper(), regex=True
    )
    abstracts["text"] = abstracts["text"].str.replace(
        r"\b" + text.capitalize() + r"\b", text.upper(), regex=True
    )

    return abstracts


def _adds_citations_to_abstracts(abstracts, directory):
    """Adds citations to abstracts."""

    documents = load_filtered_documents(directory)
    record_no2citation = dict(
        zip(documents["record_no"], documents["global_citations"])
    )
    abstracts["citations"] = abstracts["record_no"].map(record_no2citation)
    abstracts = abstracts.sort_values(
        ["citations", "record_no", "line_no"], ascending=[False, True, True]
    )
    return abstracts
