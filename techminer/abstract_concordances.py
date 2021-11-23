"""
Abstract concordances
===============================================================================

Abstract concordances exploration tool.


>>> from techminer import *
>>> directory = "/workspaces/techminer-api/tests/data/"
>>> abstract_concordances(directory, text='fintech').head(10)

"""

import os
import textwrap

import pandas as pd


def abstract_concordances(directory, text):

    file_name = os.path.join(directory, "abstracts.csv")
    abstracts = pd.read_csv(file_name)
    documents = pd.read_csv(os.path.join(directory, "documents.csv"))

    regex = r"\b" + text + r"\b"
    abstracts = abstracts[abstracts.text.str.contains(regex, regex=True)]
    abstracts = abstracts[["document_id", "text"]]
    abstracts["text"] = abstracts["text"].str.capitalize()
    abstracts["text"] = abstracts["text"].str.replace(text, text.upper())
    abstracts["text"] = abstracts["text"].str.replace(text.capitalize(), text.upper())
    abstracts = abstracts.groupby("document_id").agg(lambda x: ". ".join(x))
    abstracts["text"] = abstracts["text"] + "."

    with open(os.path.join(directory, "abstract_concordantes.txt"), "w") as f:
        for i, row in abstracts.iterrows():
            paragraph = textwrap.fill(
                row["text"],
                width=90,
            )
            wos_document_id = documents[documents.document_id == i].wos_document_id
            wos_document_id = wos_document_id.iloc[0]
            print("*** " + wos_document_id, file=f)
            print(paragraph, file=f)
            print("\n", file=f)

    return abstracts
