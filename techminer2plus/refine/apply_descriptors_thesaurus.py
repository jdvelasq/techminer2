# flake8: noqa
"""
Apply Key Concepts Thesaurus 
===============================================================================

Cleans the keywords columns using the `keywords.txt` file.


>>> root_dir = "data/regtech/"

>>> import techminer2plus
>>> techminer2plus.refine.apply_descriptors_thesaurus(root_dir)
--INFO-- Applying `descriptors.txt` thesaurus to author/index keywords and abstract/title words


# pylint: disable=line-too-long
"""
# pylint: disable=no-member
# pylint: disable=invalid-name

import glob
import os
import os.path

import pandas as pd

from ..thesaurus import load_system_thesaurus_as_dict_reversed


def apply_descriptors_thesaurus(root_dir="./"):
    """Clean all words columns in the records using a descriptors.txt."""

    # pylint: disable=line-too-long
    print(
        "--INFO-- Applying `descriptors.txt` thesaurus to author/index keywords and abstract/title words"
    )

    thesaurus_file = os.path.join(root_dir, "descriptors.txt")
    thesaurus = load_system_thesaurus_as_dict_reversed(thesaurus_file)

    files = list(glob.glob(os.path.join(root_dir, "databases/_*.csv")))
    for file in files:
        data = pd.read_csv(file, encoding="utf-8")
        #
        for raw_column, column in [
            ("raw_author_keywords", "author_keywords"),
            ("raw_index_keywords", "index_keywords"),
            ("raw_keywords", "keywords"),
            ("raw_title_nlp_phrases", "title_nlp_phrases"),
            ("raw_abstract_nlp_phrases", "abstract_nlp_phrases"),
            ("raw_nlp_phrases", "nlp_phrases"),
            ("raw_descriptors", "descriptors"),
        ]:
            if raw_column in data.columns:
                data[column] = data[raw_column].str.split(";")
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
        data.to_csv(file, sep=",", encoding="utf-8", index=False)
