"""
Abstract Screening
===============================================================================

Abstract text exploration tool.

Captures n-words around the keyword.


>>> from techminer import *
>>> directory = "/workspaces/techminer-api/data/"
>>> abstract_screening('fintech', top_n=10, directory=directory)
                  industry overall, and many FINTECH start-ups are looking
                            hook up with the FINTECH revolution is at stake
                            We present a new FINTECH innovation mapping approach that
                influenced by blockchain and FINTECH innovations
 organisations, philanthropic investment and FINTECH companies
                         about what the term FINTECH means
                  explores the complexity of FINTECH, and attempts a definition
                     out the quintessence of FINTECH using both spheres
                        it is concluded that FINTECH is a new financial
                    Financial technology, or FINTECH, involves the design and


"""


import os

import pandas as pd


def abstract_screening(
    text,
    left=4,
    right=4,
    top_n=50,
    directory="./",
):

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

    # ---< Extracts the n-words around the keyword >-------------------------------------
    text = text.upper()
    regex = r"\b" + text + r"\b"

    left_context_regex = r"(?P<left_context>(?:\w+\W+){1," + str(left) + "})"
    right_context_regex = r"(?P<right_context>(?:\W+\w+){1," + str(right) + "})"
    contexts = abstracts["text"].str.extract(
        left_context_regex + regex + right_context_regex
    )
    contexts["left_context"] = contexts["left_context"].fillna("")
    contexts["right_context"] = contexts["right_context"].fillna("")
    # contexts["left_context"] = contexts["left_context"].str.strip()
    # contexts["right_context"] = contexts["right_context"].str.strip()
    left_max_len = max(contexts["left_context"].str.len())
    contexts["left_context"] = contexts["left_context"].str.rjust(left_max_len)
    contexts = contexts.assign(
        text=contexts.left_context + text + contexts.right_context
    )

    texts = contexts.text.head(top_n).tolist()

    for text in texts:
        print(text)

    # with open(os.path.join(directory, "abstract_screening.txt"), "w") as f:
    #     for i, row in abstracts.iterrows():
    #         print(i, " --- ", row["text"], file=f)

    # return abstracts
