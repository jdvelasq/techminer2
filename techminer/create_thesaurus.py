"""
Create thesaurus
===============================================================================

"""
from os.path import isfile

import pandas as pd

from .utils import *

# from .utils.thesaurus import Thesaurus, load_file_as_dict, text_clustering


def _create_thesaurus_from_records(
    records,
    thesaurus_filepath,
    column,
    sep,
):
    logging.info("Creating thesaurus ...")
    words_list = records[column]
    words_list = words_list.dropna()

    if sep is not None:
        words_list = words_list.str.split(sep)
        words_list = words_list.explode()

    if isfile(thesaurus_filepath):
        #
        # Loads existent thesaurus
        #
        dict_ = load_file_as_dict(thesaurus_filepath)
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
            th_.to_textfile(thesaurus_filepath)
    else:
        #
        # Creates a new thesaurus
        #
        text_clustering(pd.Series(words_list)).to_textfile(thesaurus_filepath)

    logging.info(f"Thesaurus file '{thesaurus_filepath}' created.")


def _create_thesaurus_from_directory(
    thesaurus_filepath,
    directory,
    column,
    sep,
):
    """
    Create a thesaurus from a directory of records.

    """
    return _create_thesaurus_from_records(
        thesaurus_filepath=thesaurus_filepath,
        records=load_filtered_documents(directory),
        column=column,
        sep=sep,
    )


# ---< PUBLIC FUNCTIONS >---------------------------------------------------#


def create_thesaurus(
    thesaurus_filepath,
    dirpath_or_records,
    column,
    sep="; ",
):
    """
    Createa a keywords thesaurus from the specified column.



    """
    if isinstance(dirpath_or_records, str):
        return _create_thesaurus_from_directory(
            thesaurus_filepath=thesaurus_filepath,
            directory=dirpath_or_records,
            column=column,
            sep=sep,
        )
    elif isinstance(dirpath_or_records, pd.DataFrame):
        return _create_thesaurus_from_records(
            thesaurus_filepath=thesaurus_filepath,
            records=dirpath_or_records,
            column=column,
            sep=sep,
        )
    else:
        raise TypeError("dirpath_or_records must be a string or a pandas.DataFrame")
