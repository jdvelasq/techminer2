"""
Create a thesaurus from a column
===============================================================================

>>> from techminer2 import *
>>> directory = "data/"

>>> create_thesaurus(
...     column="author_keywords",
...     output_file="test_keywords.txt",
...     directory=directory,
... )
--INFO-- Creating a thesaurus file from `author_keywords` column in all databases
--INFO-- The thesaurus file data/processed/test_keywords.txt was created


# >>> apply_thesaurus(
...     thesaurus_file="keywords.txt", 
...     input_column="author_keywords",
...     output_column="author_keywords_thesaurus", 
...     strict=False,
...     directory=directory, 
... )


"""
import glob
import os
import os.path
import sys

import pandas as pd

from .thesaurus import Thesaurus, load_file_as_dict, text_clustering


def create_thesaurus(
    column,
    output_file=None,
    sep=";",
    directory="./",
):
    """Create a thesaurus from a column of a dataframe."""

    if output_file is None:
        output_file = column + ".txt"
    output_file = os.path.join(directory, "processed", output_file)

    words_list = []
    files = list(glob.glob(os.path.join(directory, "processed/_*.csv")))
    for file in files:
        data = pd.read_csv(file, encoding="utf-8")
        if column in data.columns:
            words_list += data[column].tolist()
    if len(words_list) == 0:
        raise ValueError(
            f"Column '{column}' do not exists in any database or it is empty."
        )

    sys.stdout.write(
        f"--INFO-- Creating a thesaurus file from `{column}` column in all databases\n"
    )

    words_list = pd.Series(words_list)
    words_list = words_list.dropna()

    if sep is not None:
        words_list = words_list.str.split(sep)
        words_list = words_list.explode()

    if os.path.isfile(output_file):
        #
        # Loads existent thesaurus
        #
        dict_ = load_file_as_dict(output_file)
        clustered_words = [word for key in dict_.keys() for word in dict_[key]]
        words_list = [word for word in words_list if word not in clustered_words]

        if len(words_list) > 0:

            th_ = text_clustering(pd.Series(words_list))

            th_ = Thesaurus(
                x={**th_._thesaurus, **dict_},
                ignore_case=True,
                full_match=False,
                use_re=False,
            )
            th_.to_textfile(output_file)
    else:
        #
        # Creates a new thesaurus
        #
        text_clustering(pd.Series(words_list)).to_textfile(output_file)

    sys.stdout.write(f"--INFO-- The thesaurus file {output_file} was created\n")
