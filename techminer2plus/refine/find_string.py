# flake8: noqa
"""
Find String 
===============================================================================

Finds a string in the terms of a thesaurus.


>>> root_dir = "data/regtech/"

>>> import techminer2plus
>>> techminer2plus.refine.find_string(
...     contains='ARTIFICIAL_INTELLIGENCE',
...     root_dir=root_dir,
... )
--INFO-- The file data/regtech/descriptors.txt has been reordered.

"""
import os.path

import pandas as pd

from ..thesaurus_lib import load_system_thesaurus_as_dict


# pylint: disable=too-many-locals
# pylint: disable=too-many-branches
def find_string(
    thesaurus_file="descriptors.txt",
    contains=None,
    startswith=None,
    endswith=None,
    root_dir="./",
):
    """Find the specified keyword and reorder the thesaurus file."""

    th_file = os.path.join(root_dir, thesaurus_file)
    if not os.path.isfile(th_file):
        raise FileNotFoundError(f"The file {th_file} does not exist.")

    th_dict = load_system_thesaurus_as_dict(th_file)

    reversed_th = {
        value: key for key, values in th_dict.items() for value in values
    }

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

    print(f"--INFO-- The file {th_file} has been reordered.")
