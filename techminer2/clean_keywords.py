"""
Clean Keywords
===============================================================================

Cleans the keywords columns using the file keywords.txt, located in 
the same directory as the documents.csv file.

>>> from techminer2 import *
>>> directory = "/workspaces/techminer2/data/"
>>> clean_keywords(directory)
- INFO - Applying thesaurus to 'raw_author_keywords' column ...
- INFO - Applying thesaurus to 'raw_index_keywords' column...
- INFO - Applying thesaurus to 'raw_nlp_document_title' column...
- INFO - Applying thesaurus to 'raw_nlp_abstract' column...
- INFO - Applying thesaurus to 'raw_nlp_phrases' column...
- INFO - The thesaurus was applied to all keywords.


"""
# pylint: disable=no-member
# pylint: disable=invalid-name

from os.path import isfile, join

import pandas as pd

from .common import logging
from .common.map_ import map_
from .text_api.thesaurus import read_textfile


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

    if "raw_nlp_document_title" in documents.columns:
        logging.info("Applying thesaurus to 'raw_nlp_document_title' column...")
        documents["nlp_document_title"] = map_(
            documents, "raw_nlp_document_title", th.apply_as_dict
        )

    if "raw_nlp_abstract" in documents.columns:
        logging.info("Applying thesaurus to 'raw_nlp_abstract' column...")
        documents["nlp_abstract"] = map_(
            documents, "raw_nlp_abstract", th.apply_as_dict
        )

    if "raw_nlp_phrases" in documents.columns:
        logging.info("Applying thesaurus to 'raw_nlp_phrases' column...")
        documents["nlp_phrases"] = map_(documents, "raw_nlp_phrases", th.apply_as_dict)

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
