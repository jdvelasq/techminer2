# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Clean Thesaurus
===============================================================================

>>> from techminer2.prepare.thesaurus.descriptors import clean_thesaurus
>>> clean_thesaurus(
...     #
...     # DATABASE PARAMS:
...     root_dir="example/", 
... )
--INFO-- The example/thesauri/descriptors.the.txt thesaurus has been cleaned.

"""
import os.path
from functools import lru_cache  # type: ignore

import pandas as pd  # type: ignore
from nltk.stem import PorterStemmer  # type: ignore

THESAURUS_FILE = "thesauri/descriptors.the.txt"


def _create_data_frame_from_thesaurus(th_file):
    #
    # Creates a dataframe with the thesaurus with the following columns:
    #
    # - key: current key in the original thesaurus. This key is transformed into the fingerprint.
    # - fingerprint: new key for the cleaned thesaurus
    # - text: raw descriptor text
    #
    records = []
    with open(th_file, "r", encoding="utf-8") as file:

        for line in file.readlines():

            text = line.strip()

            if not line.startswith(" "):
                key = text
            else:
                records.append(
                    {
                        "key": key,
                        "fingerprint": key,
                        "text": text,
                    }
                )

    return pd.DataFrame(records)


#
# Optimized vesion for speed of the PorterStemmer
#
stemmer = PorterStemmer()


@lru_cache(maxsize=None)
def cached_stem(word):
    return stemmer.stem(word)


def _apply_porter_stemmer(data_frame):

    PARTICLES = [
        "_AIDED_",
        "_ASSISTED_",
        "_AND_",
        "_AND_THE_",
        "_APPLIED_TO_",
        "_AT_",
        "_BASED_",
        "_FOR_",
        "_IN_",
        "_LIKE_",
        "_OF_",
        "_OF_THE_",
        "_OF_USING_",
        "_ON_",
        "_S_",
        "_SIZED_",
        "_TO_",
        "_UNDER_",
        "_USING_",
    ]

    data_frame = data_frame.copy()

    #
    # Remove intermediate particles
    for particle in PARTICLES:
        data_frame["fingerprint"] = data_frame["fingerprint"].str.replace(
            particle,
            "_",
            regex=False,
        )

    data_frame["fingerprint"] = data_frame["fingerprint"].str.split("_")
    data_frame["fingerprint"] = data_frame["fingerprint"].map(
        lambda x: [z.strip() for z in x]
    )
    data_frame["fingerprint"] = data_frame["fingerprint"].map(
        lambda x: [cached_stem(z) for z in x]
    )
    data_frame["fingerprint"] = data_frame["fingerprint"].map(sorted)
    data_frame["fingerprint"] = data_frame["fingerprint"].str.join("_")

    return data_frame


def _compute_terms_by_key(data_frame):
    #
    data_frame = data_frame.copy()
    data_frame["n_terms"] = data_frame.groupby(["fingerprint", "key"]).transform(
        "count"
    )
    data_frame = data_frame.sort_values(
        ["fingerprint", "n_terms", "key"], ascending=True
    )
    return data_frame


def _replace_fingerprint(data_frame):
    #
    # replace the fingerprint for the most frequent key (i.e., the key with the highest number of terms)
    #
    data_frame = data_frame.copy()
    repl = {row.fingerprint: row.key for _, row in data_frame.iterrows()}
    data_frame["fingerprint"] = data_frame["fingerprint"].map(repl)

    return data_frame


def _save_thesaurus(data_frame, th_file):
    #
    # Creates a new thesaurus file
    #
    data_frame = data_frame.copy()
    data_frame = data_frame[["fingerprint", "text"]]
    data_frame = data_frame.drop_duplicates()
    data_frame = data_frame.sort_values(["fingerprint", "text"], ascending=True)
    data_frame = data_frame.groupby("fingerprint").agg(list)

    with open(th_file, "w", encoding="utf-8") as file:

        for key, row in data_frame.iterrows():

            file.write(key + "\n")

            for value in row.text:
                file.write("    " + value + "\n")


def clean_thesaurus(
    #
    # DATABASE PARAMS:
    root_dir="./",
):
    """:meta private:"""

    # Dictionary path
    th_file = os.path.join(root_dir, THESAURUS_FILE)

    data_frame = _create_data_frame_from_thesaurus(th_file)
    data_frame = _apply_porter_stemmer(data_frame)
    data_frame = _compute_terms_by_key(data_frame)
    data_frame = _replace_fingerprint(data_frame)

    _save_thesaurus(data_frame, th_file)

    print(f"--INFO-- The {th_file} thesaurus has been cleaned.")
