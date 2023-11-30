# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Words Frequency
===============================================================================

Suggest thesurus words to analyze based on frequency.

>>> from techminer2.refine.thesaurus.descriptors import words_frequency
>>> words_frequency(
...     #
...     # DATABASE PARAMS:
...     root_dir="example/", 
... ).head(10)
FINANCIAL     146
FINTECH       145
TECHNOLOGY     70
SERVICES       59
INNOVATION     51
NEW            38
INDUSTRY       37
RESEARCH       36
MOBILE         33
MARKET         32
Name: words, dtype: int64

"""
import os
import os.path

import pandas as pd


def words_frequency(
    #
    # DATABASE PARAMS:
    root_dir="./",
):
    """:meta private:"""

    descriptors_list = []

    file = os.path.join(root_dir, "databases/_main.csv.zip")
    data = pd.read_csv(file, encoding="utf-8", compression="zip")
    if "raw_descriptors" in data.columns:
        descriptors_list.append(data["raw_descriptors"])

    descriptors = pd.concat(descriptors_list, ignore_index=True)
    descriptors = descriptors.dropna()
    descriptors = descriptors.str.split(";")
    descriptors = descriptors.explode()
    descriptors = descriptors.str.strip()
    descriptors = descriptors.str.replace("_", " ")
    descriptors = descriptors.str.split(" ")
    descriptors = descriptors.explode()
    descriptors = descriptors.str.strip()
    descriptors = descriptors.rename("words")

    return descriptors.value_counts()
