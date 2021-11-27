"""
Abstract concordances
===============================================================================

Abstract concordances exploration tool.


>>> from techminer import *
>>> directory = "/workspaces/techminer-api/data/"
>>> abstract_concordances('fintech', directory).head(5)
                                                        text
record_no                                                   
2015-0001  The virtual special issue (vsi) of electronic ...
2015-0002  Therefore, it is our purpose to suggest biomet...
2016-0000  There is currently no consensus about what the...
2016-0001  This study applies the lens of actor-network t...
2016-0002  This paper examined the acceptance of payment-...

"""

import os
import textwrap

import pandas as pd


def abstract_concordances(text, directory="./"):

    file_name = os.path.join(directory, "abstracts.csv")
    abstracts = pd.read_csv(file_name)
    documents = pd.read_csv(os.path.join(directory, "documents.csv"))

    regex = r"\b" + text + r"\b"
    abstracts = abstracts[abstracts.text.str.contains(regex, regex=True)]
    abstracts = abstracts[["record_no", "text"]]
    abstracts["text"] = abstracts["text"].str.capitalize()
    abstracts["text"] = abstracts["text"].str.replace(text, text.upper())
    abstracts["text"] = abstracts["text"].str.replace(text.capitalize(), text.upper())
    abstracts = abstracts.groupby("record_no").agg(lambda x: ". ".join(x))
    abstracts["text"] = abstracts["text"] + "."

    with open(os.path.join(directory, "abstract_concordantes.txt"), "w") as f:
        for i, row in abstracts.iterrows():
            paragraph = textwrap.fill(
                row["text"],
                width=90,
            )
            document_id = documents[documents.record_no == i].document_id
            document_id = document_id.iloc[0]
            print("*** " + document_id, file=f)
            print(paragraph, file=f)
            print("\n", file=f)

    return abstracts
