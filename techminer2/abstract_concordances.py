"""
Abstract Concordances
=========================================================================================

Abstract concordances exploration tool.


>>> from techminer2 import *
>>> directory = "data/"
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

from ._read_records import read_filtered_records
from .load_abstracts import load_abstracts


def abstract_concordances(
    text,
    top_n=50,
    directory="./",
):
    """Checks the occurrence contexts of a given text in the abstract's phrases."""

    abstracts = load_abstracts(directory)
    abstracts = abstracts.sort_values(
        ["global_citations", "record_no", "line_no"], ascending=[False, True, True]
    )
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
    contexts = abstracts["phrase"].str.extract(
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
    abstracts = abstracts[abstracts.phrase.str.contains(regex, regex=True)]
    abstracts["phrase"] = abstracts["phrase"].str.capitalize()
    abstracts["phrase"] = abstracts["phrase"].str.replace(
        r"\b" + text + r"\b", text.upper(), regex=True
    )
    abstracts["phrase"] = abstracts["phrase"].str.replace(
        r"\b" + text.capitalize() + r"\b", text.upper(), regex=True
    )

    return abstracts
