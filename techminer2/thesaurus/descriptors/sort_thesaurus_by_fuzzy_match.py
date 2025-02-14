# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-bramcbes
"""
Fuzzy Search 
===============================================================================


## >>> from techminer2.prepare.thesaurus.descriptors import fuzzy_search
## >>> fuzzy_search(
## ...     #
## ...     # SEARCH PARAMS:
## ...     patterns='INTELIGEN',
## ...     threshold=70,
## ...     #
## ...     # DATABASE PARAMS:
## ...     root_dir="example/", 
## ... )
ARTIFICIAL_INTELLIGENCE
     AI
     ARTIFICIAL_INTELLIGENCE
INTELLIGENT
INTELLIGENT_ROBOTS





"""
import os.path

import pandas as pd  # type: ignore
from fuzzywuzzy import process  # type: ignore

from .._internals.load_thesaurus_as_dict import internal__load_thesaurus_as_dict

THESAURUS_FILE = "thesauri/descriptors.the.txt"


def fuzzy_search(
    #
    # SEARCH PARAMS:
    patterns,
    threshold=80,
    #
    # DATABASE PARAMS:
    root_dir="./",
):
    """:meta private:"""

    th_file = os.path.join(root_dir, THESAURUS_FILE)
    if not os.path.isfile(th_file):
        raise FileNotFoundError(f"The file {th_file} does not exist.")

    th_dict = internal__load_thesaurus_as_dict(th_file)

    reversed_th = {value: key for key, values in th_dict.items() for value in values}

    pdf = pd.DataFrame(
        {
            "text": reversed_th.keys(),
            "key": reversed_th.values(),
        }
    )

    pdf["text"] = pdf.text.str.replace("_", " ").str.lower()

    result = []

    if isinstance(patterns, str):
        patterns = [patterns]

    patterns = [pattern.lower() for pattern in patterns]

    for pattern in patterns:
        potential_matches = process.extract(pattern, pdf.text, limit=None)
        for potential_match in potential_matches:
            if potential_match[1] >= threshold:
                result.append(pdf[pdf.text.str.contains(potential_match[0])])

    if len(result) == 0:
        print("--INFO-- No matches found for the current thresold")
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
