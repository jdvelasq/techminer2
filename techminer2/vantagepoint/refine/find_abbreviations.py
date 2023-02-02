"""
Find Abbreviations
===============================================================================

Finds string abbreviations in the keywords of a thesaurus.

>>> directory = "data/regtech/"

>>> from techminer2 import vantagepoint
>>> vantagepoint.refine.find_abbreviations(
...     "keywords.txt",
...     directory=directory,
... )
--INFO-- The file data/regtech/processed/keywords.txt has been reordered.


"""
import sys
from os.path import isfile, join

import pandas as pd

from ..._lib._thesaurus import load_file_as_dict


def find_abbreviations(
    thesaurus_file="keywords.txt",
    directory="./",
):
    """Find abbreviations and reorder the thesaurus to reflect the search."""

    def extract_abbreviation(x):
        if "(" in x:
            abbreviation = x[x.find("(") + 1 : x.find(")")]
            return abbreviation
        return None

    # ----< Load and reverse the thesaurus >------------------------------------------------------
    th_file = join(directory, "processed", thesaurus_file)
    if isfile(th_file):
        th = load_file_as_dict(th_file)
    else:
        raise FileNotFoundError(f"The file {th_file} does not exist.")
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

        try:
            keywords = df[
                df.text.map(lambda x: x == abbreviation)
                | df.text.str.contains("(" + abbreviation + ")", regex=False)
                | df.text.map(lambda x: x == "(" + abbreviation + ")")
                | df.text.str.contains("\b" + abbreviation + "\b", regex=True)
            ]

            keywords = keywords.key.drop_duplicates()

            if len(keywords) > 1:
                results.append(keywords.to_list())

        except:
            print("Manual check: " + abbreviation)

    # ----< remove found keywords >-----------------------------------------------------------------
    results = [value for result in results for value in result]
    findings = {key: th[key] for key in results}
    for key in findings.keys():
        th.pop(key)

    # ----< save the thesaurus >--------------------------------------------------------------------
    with open(th_file, "w", encoding="utf-8") as file:

        for key in findings.keys():
            # print(key)
            file.write(key + "\n")
            for item in findings[key]:
                file.write("    " + item + "\n")
                # print("    " + item)

        for key in sorted(th.keys()):
            file.write(key + "\n")
            for item in th[key]:
                file.write("    " + item + "\n")

    sys.stdout.write(f"--INFO-- The file {th_file} has been reordered.\n")
