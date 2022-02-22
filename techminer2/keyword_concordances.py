"""
Keyword Concordances
===============================================================================

Abstract concordances exploration tool.


>>> from techminer2 import *
>>> directory = "/workspaces/techminer2/data/"
>>> keyword_concordances('fintech', top_n=10, directory=directory)


"""

import textwrap
from os.path import isfile, join

import pandas as pd

from . import logging
from .thesaurus import load_file_as_dict


def keyword_concordances(keywords, top_n=50, directory="./"):

    # ---< Sort abstracts by importance >------------------------------------------------
    documents = pd.read_csv(join(directory, "documents.csv"))
    record_no2citation = dict(
        zip(documents["record_no"], documents["global_citations"])
    )
    abstracts = pd.read_csv(join(directory, "abstracts.csv"))
    abstracts["citations"] = abstracts["record_no"].map(record_no2citation)
    abstracts = abstracts.sort_values(
        ["citations", "record_no", "line_no"], ascending=[False, True, True]
    )

    # ----< loads keywords >-------------------------------------------------------------
    thesaurus_file = join(directory, "keywords.txt")
    if isfile(thesaurus_file):
        th = load_file_as_dict(thesaurus_file)
    else:
        raise FileNotFoundError("The file {} does not exist.".format(thesaurus_file))

    # extract keys for thesaurus
    reversed_th = {value: key for key, values in th.items() for value in values}
    th_keys = []

    if isinstance(keywords, str):
        keywords = [keywords]

    for keyword in keywords:
        th_keys.append(reversed_th[keyword])
    expanded_keywords = [text for key in th_keys for text in th[key]]

    # ---< Selects the abstracts >-------------------------------------------------------
    regex = [r"\b" + keyword + r"\b" for keyword in expanded_keywords]
    regex
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
