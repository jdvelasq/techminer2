"""
Find Abbreviations
===============================================================================

Finds string abbreviations in keywords.

>>> from techminer2 import *
>>> directory = "/workspaces/techminer2/data/"
>>> find_abbreviations(directory=directory)


"""
from os.path import isfile, join

import pandas as pd

from .thesaurus import load_file_as_dict


def find_abbreviations(
    directory="./",
):
    """
    Find abbreviations and reorder the thesaurus to reflect the search.

    """

    def extract_abbreviation(x):
        if "(" in x:
            abbreviation = x[x.find("(") + 1 : x.find(")")]
            return abbreviation
        return None

    # ----< Load and reverse the thesaurus >------------------------------------------------------
    thesaurus_file = join(directory, "keywords.txt")
    if isfile(thesaurus_file):
        th = load_file_as_dict(thesaurus_file)
    else:
        raise FileNotFoundError("The file {} does not exist.".format(thesaurus_file))
    reversed_th = {value: key for key, values in th.items() for value in values}

    # ----< search for abbreviations >-------------------------------------------------------------
    df = pd.DataFrame(
        {
            "text": reversed_th.keys(),
            "key": reversed_th.values(),
        }
    )
    df["abbreviation"] = df["text"].map(extract_abbreviation)

    # ----< filter by each abbreviation >----------------------------------------------------------
    abbreviations = df.abbreviation.dropna().drop_duplicates()

    results = []
    for abbreviation in abbreviations.to_list():

        keywords = df[
            df.text.map(lambda x: x == abbreviation)
            | df.text.str.contains("(" + abbreviation + ")", regex=False)
            | df.text.map(lambda x: x == "(" + abbreviation + ")")
            | df.text.str.contains("\b" + abbreviation + "\b", regex=True)
        ]

        keywords = keywords.key.drop_duplicates()

        if len(keywords) > 1:
            results.append(keywords.to_list())
            print(abbreviation)

    # ----< remove found keywords >-----------------------------------------------------------------
    results = [value for result in results for value in result]
    findings = {key: th[key] for key in results}
    for key in findings.keys():
        th.pop(key)

    # ----< save the thesaurus >--------------------------------------------------------------------
    with open(thesaurus_file, "w", encoding="utf-8") as file:

        for key in sorted(findings.keys()):
            print(key)
            file.write(key + "\n")
            for item in findings[key]:
                file.write("    " + item + "\n")
                print("    " + item)

        for key in sorted(th.keys()):
            file.write(key + "\n")
            for item in th[key]:
                file.write("    " + item + "\n")
