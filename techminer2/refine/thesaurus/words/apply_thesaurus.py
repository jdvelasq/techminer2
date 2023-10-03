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


>>> from techminer2.refine.words import apply_thesaurus
>>> apply_thesaurus(
...     #
...     # DATABASE PARAMS:
...     root_dir="example/", 
... )
--INFO-- Applying `words.txt` thesaurus to author/index keywords and abstract/title words

"""

import glob
import os
import os.path

import pandas as pd

from ...._common.thesaurus_lib import load_system_thesaurus_as_dict_reversed


def apply_thesaurus(
    #
    # DATABASE PARAMS:
    root_dir="./",
):
    """
    :meta private:
    """

    # pylint: disable=line-too-long
    print(
        "--INFO-- Applying `words.txt` thesaurus to author/index keywords and abstract/title words"
    )

    thesaurus_file = os.path.join(root_dir, "words.txt")
    thesaurus = load_system_thesaurus_as_dict_reversed(thesaurus_file)

    files = list(glob.glob(os.path.join(root_dir, "databases/_*.zip")))
    for file in files:
        data = pd.read_csv(file, encoding="utf-8", compression="zip")
        #
        for raw_column, column in [
            ("raw_author_keywords", "author_keywords"),
            ("raw_index_keywords", "index_keywords"),
            ("raw_keywords", "keywords"),
            ("raw_title_nlp_phrases", "title_nlp_phrases"),
            ("raw_abstract_nlp_phrases", "abstract_nlp_phrases"),
            ("raw_nlp_phrases", "nlp_phrases"),
            ("raw_descriptors", "descriptors"),
            ("raw_title_words", "title_words"),
            ("raw_abstract_words", "abstract_words"),
            ("raw_words", "words"),
        ]:
            if raw_column in data.columns:
                data[column] = data[raw_column].str.split("; ")
                data[column] = data[column].map(
                    lambda x: [thesaurus.get(y.strip(), y.strip()) for y in x]
                    if isinstance(x, list)
                    else x
                )
                data[column] = data[column].map(
                    lambda x: sorted(set(x)) if isinstance(x, list) else x
                )
                data[column] = data[column].str.join("; ")
        #
        data.to_csv(file, sep=",", encoding="utf-8", index=False, compression="zip")
