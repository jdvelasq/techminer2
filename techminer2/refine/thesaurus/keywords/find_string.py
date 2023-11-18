# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Find String 
===============================================================================

Finds a string in the terms of a thesaurus.


>>> from techminer2.refine.thesaurus.keywords import find_string
>>> find_string(
...     #
...     # SEARCH PARAMS:
...     contains='ARTIFICIAL_INTELLIGENCE',
...     startswith=None,
...     endswith=None,
...     #
...     # DATABASE PARAMS:
...     root_dir="example/", 
... )
--INFO-- The file example/thesauri/keywords.the.txt has been reordered.

"""
import os.path
import re

import pandas as pd

from ...._common.thesaurus_lib import load_system_thesaurus_as_dict

THESAURUS_FILE = "thesauri/keywords.the.txt"


def find_string(
    #
    # SEARCH PARAMS:
    contains=None,
    startswith=None,
    endswith=None,
    #
    # DATABASE PARAMS:
    root_dir="./",
):
    """
    :meta private:
    """

    th_file = os.path.join(root_dir, THESAURUS_FILE)
    if not os.path.isfile(th_file):
        raise FileNotFoundError(f"The file {th_file} does not exist.")

    th_dict = load_system_thesaurus_as_dict(th_file)

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
            #
            # startswith:
            result.append(
                pdf[
                    pdf.text.str.contains(
                        re.compile("^" + word + "_"),
                        regex=True,
                    )
                ]
            )
            #
            result.append(
                pdf[
                    pdf.text.str.contains(
                        re.compile("^" + word + r"\b"),
                        regex=True,
                    )
                ]
            )
            #
            # endswith:
            result.append(
                pdf[
                    pdf.text.str.contains(
                        re.compile("_" + word + "$"),
                        regex=True,
                    )
                ]
            )
            #
            result.append(
                pdf[
                    pdf.text.str.contains(
                        re.compile(r"\b" + word + "$"),
                        regex=True,
                    )
                ]
            )
            #
            # contains:
            result.append(
                pdf[
                    pdf.text.str.contains(
                        re.compile("_" + word + "_"),
                        regex=True,
                    )
                ]
            )
            #
            result.append(
                pdf[
                    pdf.text.str.contains(
                        re.compile(r"\b" + word + "_"),
                        regex=True,
                    )
                ]
            )
            #
            result.append(
                pdf[
                    pdf.text.str.contains(
                        re.compile("_" + word + r"\b"),
                        regex=True,
                    )
                ]
            )
            #
            result.append(
                pdf[
                    pdf.text.str.contains(
                        re.compile(r"\b" + word + r"\b"),
                        regex=True,
                    )
                ]
            )
            #
    elif startswith is not None:
        if isinstance(startswith, str):
            startswith = [startswith]
        for word in startswith:
            #
            result.append(
                pdf[
                    pdf.text.str.contains(
                        re.compile("^" + word + "_"),
                        regex=True,
                    )
                ]
            )
            #
            result.append(
                pdf[
                    pdf.text.str.contains(
                        re.compile("^" + word + r"\b"),
                        regex=True,
                    )
                ]
            )
            #
    elif endswith is not None:
        if isinstance(endswith, str):
            endswith = [endswith]
        for word in endswith:
            #
            result.append(
                pdf[
                    pdf.text.str.contains(
                        re.compile("_" + word + "$"),
                        regex=True,
                    )
                ]
            )
            #
            result.append(
                pdf[
                    pdf.text.str.contains(
                        re.compile(r"\b" + word + "$"),
                        regex=True,
                    )
                ]
            )
            #

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
