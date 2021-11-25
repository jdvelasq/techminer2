"""
Abstract screening
===============================================================================

Abstract text exploration tool.

Captures n-words around the keyword.


>>> from techminer import *
>>> directory = "/workspaces/techminer-api/tests/data/"
>>> abstract_screening(directory, text='fintech').head(10)
                                                          text
2022-0002-3  for the project gamified FINTECH project for e...
2022-0004-0  the vigorous development of FINTECH has brough...
2022-0004-5  promote the development of FINTECH, which in t...
2022-0006-1  the sustainability profile of FINTECH companie...
2022-0006-2  the kbw and nasdaq FINTECH indices, and the na...
2022-0006-4  the market value of FINTECH companies is posit...
2022-0007-1  as well as in FINTECH, specifically targeting ...
2022-0007-3  question of whether the FINTECH development is...
2022-0007-4  encouraging, and confirm that FINTECH developm...
2022-0007-5  the potential endogeneity of FINTECH developme...

"""


import os

import pandas as pd


def abstract_screening(directory, text, left=4, right=4):

    file_name = os.path.join(directory, "abstracts.csv")
    abstracts = pd.read_csv(file_name)
    abstracts = abstracts[abstracts.text.str.contains(text)]
    regex = (
        r"((?:\w+\W+){1,"
        + str(left)
        + "}"
        + r"\b"
        + text
        + r"\b(?:\W+\w+){1,"
        + str(right)
        + "})"
    )
    abstracts["text"] = abstracts["text"].str.extract(regex)
    abstracts["text"] = abstracts["text"].str.replace(text, text.upper())
    abstracts.index = abstracts.record_no + "-" + abstracts.line_no.astype(str)
    abstracts = abstracts[["text"]]
    abstracts = abstracts.dropna()

    with open(os.path.join(directory, "abstract_screening.txt"), "w") as f:
        for i, row in abstracts.iterrows():
            print(i, " --- ", row["text"], file=f)

    return abstracts
