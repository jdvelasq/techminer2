# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# mypy: ignore-errors
"""
Check Thesaurus
===============================================================================


## >>> from techminer2.prepare.thesaurus.descriptors import check_thesaurus
## >>> check_thesaurus(
## ...     #
## ...     # DATABASE PARAMS:
## ...     root_dir="example/", 
## ... )
--INFO-- Checking `descriptors.the.txt` integrity.

"""
import os
import os.path

import pandas as pd  # type: ignore

from .._internals.load_reversed_thesaurus_as_mapping import (
    internal__load_reversed_thesaurus_as_mapping,
)

THESAURUS_FILE = "thesauri/descriptors.the.txt"


def check_thesaurus(
    #
    # DATABASE PARAMS:
    root_dir="./",
):
    """:meta private:"""

    # pylint: disable=line-too-long
    print("--INFO-- Checking `descriptors.the.txt` integrity.")

    #
    # Loads the terms to check
    thesaurus_file = os.path.join(root_dir, THESAURUS_FILE)
    thesaurus = internal__load_reversed_thesaurus_as_mapping(thesaurus_file)
    terms = list(thesaurus.keys())

    #
    # Loads the descriptors
    file = os.path.join(root_dir, "databases/_main.csv.zip")
    data = pd.read_csv(file, encoding="utf-8", compression="zip")
    raw_descriptors = data.raw_descriptors.copy()
    raw_descriptors = (
        raw_descriptors.dropna()
        .str.split("; ")
        .explode()
        .str.strip()
        .drop_duplicates()
        .tolist()
    )

    #
    # Computes the set union between terms and descriptors
    union = set(terms).union(set(raw_descriptors))
    if len(union) != len(terms) or len(union) != len(raw_descriptors):
        if len(raw_descriptors) > len(terms):
            print(set(raw_descriptors) - set(terms))
        else:
            print(set(terms) - set(raw_descriptors))

    # union must be equal to terms and equal to descriptors
    assert len(union) == len(terms)
    assert len(union) == len(raw_descriptors)
