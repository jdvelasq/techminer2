"""
Abstract concordances
===============================================================================

Abstract concordances exploration tool.


>>> from techminer import *
>>> directory = "/workspaces/techminer-api/data/"
>>> abstract_concordances('fintech', top_n=10, directory=directory)
- INFO - Abstract concordances report generated.
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

import os
import textwrap

import pandas as pd

from .utils import logging


def abstract_concordances(text, top_n=50, directory="./"):

    # ---< Sort abstracts by importance >------------------------------------------------
    documents = pd.read_csv(os.path.join(directory, "documents.csv"))
    record_no2citation = dict(
        zip(documents["record_no"], documents["global_citations"])
    )
    abstracts = pd.read_csv(os.path.join(directory, "abstracts.csv"))
    abstracts["citations"] = abstracts["record_no"].map(record_no2citation)
    abstracts = abstracts.sort_values(
        ["citations", "record_no", "line_no"], ascending=[False, True, True]
    )

    # ---< Selects the abstracts >-------------------------------------------------------
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

    # ---< Writes the report >-----------------------------------------------------------
    with open(os.path.join(directory, "abstract_concordantes.txt"), "w") as out_file:
        for _, row in abstracts.iterrows():

            paragraph = textwrap.fill(
                row["text"],
                width=90,
            )
            document_id = documents[
                documents.record_no == row.record_no
            ].document_id.tolist()[0]

            print("*** " + document_id, file=out_file)
            print(paragraph, file=out_file)
            print("", file=out_file)
    logging.info("Abstract concordances report generated.")

    # ---< Display results >-------------------------------------------------------------
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
    for _, row in contexts.head(top_n).iterrows():
        print(
            "{:>60s} {:s} {:s}".format(
                row["left_context"],
                text,
                row["right_context"],
            )
        )
