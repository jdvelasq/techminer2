"""
Keyword Concordances
===============================================================================

Abstract concordances exploration tool.


>>> from techminer2 import *
>>> directory = "data/regtech/"
>>> keyword_concordances('structural equation model', top_n=10, directory=directory)
- INFO - Abstract concordances report generated.
                                We analyzed the data with a  structural equation model  (sem) to test the hypotheses, including the relationshi ...
...  model, five hypotheses were developed and tested using  structural equation model  techniques (sem-pls).
                              The data analysis method used  structural equation model  with warppls 6.0 software.
                                      For the analysis, the  structural equation model  (sem) was used.
      To analyze the causal relationship between variables,  structural equation model  (sem) was implemented.
         The research design is a quantitative method using  structural equation model  (sem).
                                         Analysis data with  structural equation model  (sem) using smart pls v2.0.
                                                             structural equation model  (sem) was used to analyze and verify the study variables.
... roach using a questionnaire to collect the data and use  structural equation model  to analyse it.
                                                      Using  structural equation model  to analyze the study's conceptual model, our results co ...


"""

import textwrap
from os.path import isfile, join

import pandas as pd

from . import logging
from ._read_records import read_filtered_records
from .thesaurus import load_file_as_dict


def keyword_concordances(keyword, top_n=50, directory="./"):

    # ---< Sort abstracts by importance >------------------------------------------------
    documents = read_filtered_records(directory)
    record_no2citation = dict(
        zip(documents["record_no"], documents["global_citations"])
    )
    abstracts = pd.read_csv(join(directory, "processed", "abstracts.csv"))
    abstracts["citations"] = abstracts["record_no"].map(record_no2citation)
    abstracts = abstracts.sort_values(
        ["citations", "record_no", "line_no"], ascending=[False, True, True]
    )

    # ----< loads keywords >-------------------------------------------------------------
    thesaurus_file = join(directory, "processed", "keywords.txt")
    if isfile(thesaurus_file):
        th = load_file_as_dict(thesaurus_file)
    else:
        raise FileNotFoundError("The file {} does not exist.".format(thesaurus_file))

    # extract keys for thesaurus
    reversed_th = {value: key for key, values in th.items() for value in values}
    th_keys = []

    th_keys.append(reversed_th[keyword])
    expanded_keywords = [text for key in th_keys for text in th[key]]

    # ---< Selects the abstracts >-------------------------------------------------------
    regex = [r"\b" + word + r"\b" for word in expanded_keywords]
    regex = "|".join(regex)
    abstracts = abstracts[abstracts.text.str.contains(regex, regex=True)]
    abstracts = abstracts[["record_no", "text"]]
    abstracts["text"] = abstracts["text"].str.capitalize()
    for word in expanded_keywords:
        abstracts["text"] = abstracts["text"].str.replace(
            r"\b" + word + r"\b", word.upper(), regex=True
        )
        abstracts["text"] = abstracts["text"].str.replace(
            r"\b" + word.capitalize() + r"\b", word.upper(), regex=True
        )

    # ---< Writes the report >-----------------------------------------------------------
    with open(join(directory, "keyword_concordances.txt"), "w") as out_file:

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
    expanded_keywords = [word.upper() for word in expanded_keywords]

    regex = [r"\b" + word + r"\b" for word in expanded_keywords]
    regex = "(" + "|".join(regex) + ")"
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
                keyword,
                row["right_context"],
            )
        )
