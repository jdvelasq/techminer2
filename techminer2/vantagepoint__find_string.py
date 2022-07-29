"""
Find String (in a thesarus)
===============================================================================

Finds a string in the terms of a thesaurus.


>>> directory = "data/regtech/"

>>> from techminer2 import vantagepoint__find_string
>>> vantagepoint__find_string(
...     contains='artificial intelligence',
...     thesaurus_file="keywords.txt",
...     directory=directory,
... )
artificial intelligence
     artificial intelligence
     artificial intelligence (ai)
artificial intelligence & law
artificial intelligence (ai) governance
artificial intelligence agent
artificial intelligence course
     artificial intelligence course
     artificial intelligence courses
artificial intelligence in education
artificial intelligence technologies
     artificial intelligence technologies
     artificial intelligence technology
artificial intelligence tools
responsible artificial intelligence


"""
import os.path

import pandas as pd

from ._thesaurus import load_file_as_dict


def vantagepoint__find_string(
    contains=None,
    startswith=None,
    endswith=None,
    thesaurus_file="keywords.txt",
    directory="./",
):
    """Find the specified keyword and reorder the thesaurus to reflect the search."""

    th_file = os.path.join(directory, "processed", thesaurus_file)
    if os.path.isfile(th_file):
        th_dict = load_file_as_dict(th_file)
    else:
        raise FileNotFoundError(f"The file {th_file} does not exist.")

    reversed_th = {value: key for key, values in th_dict.items() for value in values}

    pdf = pd.DataFrame(
        {
            "text": reversed_th.keys(),
            "key": reversed_th.values(),
        }
    )

    result = []
    if contains is not None:
        if isinstance(contains, str):
            contains = [contains]
        for word in contains:
            result.append(pdf[pdf.text.str.contains(word)])
    elif startswith is not None:
        if isinstance(startswith, str):
            startswith = [startswith]
        for word in startswith:
            result.append(pdf[pdf.text.str.startswith(word)])
    elif endswith is not None:
        if isinstance(endswith, str):
            endswith = [endswith]
        for word in endswith:
            result.append(pdf[pdf.text.str.endswith(word)])
    else:
        raise ValueError("No filter provided")
    pdf = pd.concat(result)

    keys = pdf.key.drop_duplicates()

    findings = {key: th_dict[key] for key in sorted(keys)}

    # reorder the thesaurus to reflect the search
    for key in findings.keys():
        th_dict.pop(key)

    with open(th_file, "w", encoding="utf-8") as file:

        for key in sorted(findings.keys()):
            file.write(key + "\n")
            for item in findings[key]:
                file.write("    " + item + "\n")

        for key in sorted(th_dict.keys()):
            file.write(key + "\n")
            for item in th_dict[key]:
                file.write("    " + item + "\n")

    for key, items in sorted(findings.items()):
        print(key)
        if len(items) > 1:
            for item in sorted(items):
                print("    ", item)
