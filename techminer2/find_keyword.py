"""
Find Keyword
===============================================================================

Finds a string in the terms of a thesaurus.

>>> from techminer2 import *
>>> directory = "data/"

>>> find_keyword(
...     thesaurus_file="author_keywords.txt",
...     contains='artificial intelligence',
...     directory=directory,
... )
artificial intelligence
     artificial intelligence
     artificial intelligence (ai)
artificial intelligence & law
artificial intelligence (ai) governance
artificial intelligence in education
responsible artificial intelligence

"""
import os.path

import pandas as pd

from .thesaurus import load_file_as_dict


def find_keyword(
    thesaurus_file,
    contains=None,
    startswith=None,
    endswith=None,
    directory="./",
):
    """Find the specified keyword and reorder the thesaurus to reflect the search."""

    th_file = os.path.join(directory, "processed", thesaurus_file)
    if os.path.isfile(th_file):
        th = load_file_as_dict(th_file)
    else:
        raise FileNotFoundError("The file {} does not exist.".format(th_file))

    reversed_th = {value: key for key, values in th.items() for value in values}

    df = pd.DataFrame(
        {
            "text": reversed_th.keys(),
            "key": reversed_th.values(),
        }
    )

    if contains is not None:
        result = []
        if isinstance(contains, str):
            contains = [contains]
        for word in contains:
            result.append(df[df.text.str.contains(word)])
        df = pd.concat(result)
    elif startswith is not None:
        result = []
        if isinstance(startswith, str):
            startswith = [startswith]
        for word in startswith:
            result.append(df[df.text.str.startswith(word)])
        df = pd.concat(result)
    elif endswith is not None:
        result = []
        if isinstance(endswith, str):
            endswith = [endswith]
        for word in endswith:
            result.append(df[df.text.str.endswith(word)])
        df = pd.concat(result)
    else:
        raise ValueError("No filter provided")

    keys = df.key.drop_duplicates()

    findings = {key: th[key] for key in sorted(keys)}

    for key, items in sorted(findings.items()):
        print(key)
        if len(items) > 1:
            for item in sorted(items):
                print("    ", item)

    # reorder the thesaurus to reflect the search
    for key in findings.keys():
        th.pop(key)

    with open(th_file, "w", encoding="utf-8") as file:

        for key in sorted(findings.keys()):
            file.write(key + "\n")
            for item in findings[key]:
                file.write("    " + item + "\n")

        for key in sorted(th.keys()):
            file.write(key + "\n")
            for item in th[key]:
                file.write("    " + item + "\n")
