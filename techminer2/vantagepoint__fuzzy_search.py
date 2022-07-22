"""
Fuzzy Search (of a string in a thesaurus)
===============================================================================

Finds a string in the terms of a thesaurus using fuzzy search.


>>> directory = "data/regtech/"

>>> from techminer2 import vantagepoint__fuzzy_search
>>> vantagepoint__fuzzy_search(
...     thesaurus_file="keywords.txt",
...     patterns='intelligencia',
...     threshold=80,
...     directory=directory,
... )
ambient intelligence
artificial general intelligence (agi)
     artificial general intelligence (agi)
     artificial general intelligences
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
artificial narrow intelligence (ani)
augmented intelligence
augmented intelligence collaboration
business intelligence
     business intelligence
     business intelligence (bi)
business process intelligence
collective intelligence
     collective intelligence
     collective intelligences
competitive intelligence
computational intelligence
     computational intelligence
     intelligent computers
     intelligent computing
cyber threat intelligence
financial intelligence units
intelligence
intelligence activities
intelligence control
     intelligence control
     intelligent control
intelligence decision
intelligence services
     intelligence services
     intelligent services
intelligence systems
     intelligence systems
     intelligent systems
responsible artificial intelligence
risk intelligence
social media intelligence


"""
import os.path
import sys

import pandas as pd
from fuzzywuzzy import process

from ._thesaurus import load_file_as_dict


def vantagepoint__fuzzy_search(
    thesaurus_file,
    patterns,
    threshold=80,
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

    if isinstance(patterns, str):
        patterns = [patterns]

    for pattern in patterns:
        potential_matches = process.extract(pattern, pdf.text, limit=None)
        for potential_match in potential_matches:
            if potential_match[1] >= threshold:
                result.append(pdf[pdf.text.str.contains(potential_match[0])])

    if len(result) == 0:
        sys.stdout.write("--INFO-- No matches found for the current thresold\n")
        return

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
