"""
Abstract screening
===============================================================================

Abstract text exploration tool.

Captures n-words around the keyword.


>>> from techminer import *
>>> directory = "/workspaces/techminer-api/data/"
>>> abstract_screening('fintech', directory).head(10)
                                                          text
2021-0042-0  implementation of financial technology (FINTEC...
2021-0042-1  sector ought to embrace FINTECH to diversify t...
2021-0042-3  compliant regulation to govern FINTECH-related...
2021-0042-5  framework especially for islamic FINTECH firms...
2021-0043-0                  the FINTECH innovation of e-money
2021-0044-7  comprehensive study of the FINTECH documents n...
2021-0025-1  of the use of FINTECH finance by businesses, with
2021-0025-2                more likely to seek FINTECH finance
2021-0025-4     the relative desirability of FINTECH financing
2021-0025-5  the relative benefits of FINTECH finance for i...


"""


import os

import pandas as pd


def abstract_screening(text, directory="./", left=4, right=4):

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
