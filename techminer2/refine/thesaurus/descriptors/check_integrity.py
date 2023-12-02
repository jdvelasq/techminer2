# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Apply Thesaurus 
===============================================================================


>>> from techminer2.refine.thesaurus.descriptors import apply_thesaurus
>>> apply_thesaurus(
...     #
...     # DATABASE PARAMS:
...     root_dir="example/", 
... )
--INFO-- Applying `keywords.txt` thesaurus to author/index keywords and abstract/title words

"""

import glob
import os
import os.path

import pandas as pd

from ...._common.thesaurus_lib import load_system_thesaurus_as_dict_reversed

THESAURUS_FILE = "thesauri/descriptors.the.txt"


def check_integrity(
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
    thesaurus = load_system_thesaurus_as_dict_reversed(thesaurus_file)
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

    # union must be equal to terms and equal to descriptors
    assert len(union) == len(terms)
    assert len(union) == len(raw_descriptors)
