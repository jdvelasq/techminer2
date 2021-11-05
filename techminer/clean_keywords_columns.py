"""
Cleaning keywords columns
===============================================================================

"""
# pylint: disable=no-member
# pylint: disable=invalid-name

from os.path import isfile

import pandas as pd

from .utils import *
from .utils.thesaurus import read_textfile


def clean_keywords_columns(directory):
    """
    Clean all keywords columns in the records using a thesaurus (keywrords.txt).

    """

    logging.info("Applying thesaurus to keywords ...")

    if directory[-1] != "/":
        directory += "/"

    # --------------------------------------------------------------------------
    # Loads documents.csv
    filename = directory + "documents.csv"
    if not os.path.isfile(filename):
        raise FileNotFoundError(f"The file '{filename}' does not exist.")
    documents = pd.read_csv(filename, sep=",", encoding="utf-8")
    # --------------------------------------------------------------------------

    thesaurus_file = directory + "keywords.txt"
    if isfile(thesaurus_file):
        th = read_textfile(thesaurus_file)
        th = th.compile_as_dict()
    else:
        raise FileNotFoundError("The file {} does not exist.".format(thesaurus_file))

    #
    # Author keywords cleaning
    #
    if "author_aeywords" in documents.columns:
        documents["author_keywords_cl"] = map_(
            documents, "author_keywords", th.apply_as_dict
        )

    #
    # Index keywords cleaning
    #
    if "index_keywords" in documents.columns:
        documents["index_keywords_cl"] = map_(
            documents, "index_keywords", th.apply_as_dict
        )

    #
    # keywords new field creation
    #
    if "author_keywords" in documents.columns and "index_keywords" in documents.columns:
        documents["keywords"] = (
            documents.author_keywords.map(lambda w: "" if pd.isna(w) else w)
            + ";"
            + documents.index_keywords.map(lambda w: "" if pd.isna(w) else w)
        )
        documents["keywords"] = documents.keywords.map(
            lambda w: None if w[0] == ";" and len(w) == 1 else w
        )
        documents["keywords"] = documents.keywords.map(
            lambda w: w[1:] if w[0] == ";" else w, na_action="ignore"
        )
        documents["keywords"] = documents.keywords.map(
            lambda w: w[:-1] if w[-1] == ";" else w, na_action="ignore"
        )
        documents["keywords"] = documents.keywords.map(
            lambda w: ";".join(sorted(set(w.split(";")))), na_action="ignore"
        )

    #
    # keywords_cl new field creation
    #
    if (
        "author_keywords_cl" in documents.columns
        and "index_keywords_cl" in documents.columns
    ):
        documents["keywords_cl"] = (
            documents.author_keywords_cl.map(lambda w: "" if pd.isna(w) else w)
            + ";"
            + documents.index_keywords_cl.map(lambda w: "" if pd.isna(w) else w)
        )
        documents["keywords_cl"] = documents.keywords_cl.map(
            lambda w: pd.NA if w[0] == ";" and len(w) == 1 else w
        )
        documents["keywords_cl"] = documents.keywords_cl.map(
            lambda w: w[1:] if w[0] == ";" else w, na_action="ignore"
        )
        documents["keywords_cl"] = documents.keywords_cl.map(
            lambda w: w[:-1] if w[-1] == ";" else w, na_action="ignore"
        )
        documents["keywords_cl"] = documents.keywords_cl.map(
            lambda w: ";".join(sorted(set(w.split(";")))), na_action="ignore"
        )

    #
    # Title keywords
    #
    if "title_keywords" in documents.columns:
        documents["title_keywords_cl"] = map_(
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
        directory + "documents.csv",
        sep=",",
        encoding="utf-8",
        index=False,
    )
    # --------------------------------------------------------------------------
    logging.info("The thesaurus was applied to keywords.")
