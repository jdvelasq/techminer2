"""
Clean Keywords
===============================================================================

Cleans the keywords columns using the file keywords.txt, located in 
the same directory as the documents.csv file.

>>> from techminer2 import *
>>> directory = "/workspaces/techminer-api/data/"
>>> clean_keywords(directory)
2021-11-08 18:48:08 - INFO - Applying thesaurus to 'raw_author_keywords' column ...
2021-11-08 18:48:08 - INFO - Applying thesaurus to 'raw_index_keywords' column...
2021-11-08 18:48:08 - INFO - Applying thesaurus to 'raw_keywords' column...
2021-11-08 18:48:10 - INFO - The thesaurus was applied to keywords.


"""
# pylint: disable=no-member
# pylint: disable=invalid-name

from os.path import isfile, join

import pandas as pd

from .text.thesaurus import read_textfile
from .utils import logging, map_


def clean_keywords(directory):
    """
    Clean all keywords columns in the records using a thesaurus (keywrords.txt).

    """

    # --------------------------------------------------------------------------
    # Loads documents.csv
    filename = join(directory, "documents.csv")
    if not isfile(filename):
        raise FileNotFoundError(f"The file '{filename}' does not exist.")
    documents = pd.read_csv(filename, sep=",", encoding="utf-8")
    # --------------------------------------------------------------------------

    thesaurus_file = join(directory, "keywords.txt")
    if isfile(thesaurus_file):
        th = read_textfile(thesaurus_file)
        th = th.compile_as_dict()
    else:
        raise FileNotFoundError("The file {} does not exist.".format(thesaurus_file))

    #
    # Author keywords cleaning
    #
    if "raw_author_keywords" in documents.columns:
        logging.info("Applying thesaurus to 'raw_author_keywords' column ...")
        documents["author_keywords"] = map_(
            documents, "raw_author_keywords", th.apply_as_dict
        )

    #
    # Index keywords cleaning
    #
    if "raw_index_keywords" in documents.columns:
        logging.info("Applying thesaurus to 'raw_index_keywords' column...")
        documents["index_keywords"] = map_(
            documents, "raw_index_keywords", th.apply_as_dict
        )

    if "keywords" in documents.columns:
        logging.info("Applying thesaurus to 'raw_keywords' column...")
        documents["keywords"] = map_(documents, "raw_keywords", th.apply_as_dict)

    #
    # Title keywords
    #
    if "title_keywords" in documents.columns:
        documents["title_keywords_cleaned"] = map_(
            documents, "title_keywords", th.apply_as_dict
        )

    #
    # Abstract
    #
    for column in [
        "abstract_author_keywords",
        "abstract_index_keywords",
        "abstract_keywords",
    ]:
        if column in documents.columns:
            documents[column + "_cl"] = map_(documents, column, th.apply_as_dict)

    #
    # Saves!
    #
    # datastore.to_csv(datastorefile, index=False)
    # --------------------------------------------------------------------------
    documents.to_csv(
        join(directory, "documents.csv"),
        sep=",",
        encoding="utf-8",
        index=False,
    )
    # --------------------------------------------------------------------------
    logging.info("The thesaurus was applied to all keywords.")
