"""
Clean Institutions
===============================================================================

Cleans the institutions columns using the file institutions.txt, located in 
the same directory as the documents.csv file.

>>> from techminer2 import *
>>> directory = "/workspaces/techminer2/data/"
>>> clean_institutions(directory)
2021-11-08 18:33:47 - INFO - Applying thesaurus to institutions ...
2021-11-08 18:33:47 - INFO - Extract and cleaning institutions.
2021-11-08 18:33:47 - INFO - Extracting institution of first author ...
2021-11-08 18:33:49 - INFO - The thesaurus was applied to institutions.

"""


import os
import sys

currentdir = os.getcwd()
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

# pylint: disable=no-member

import os

import pandas as pd

from .text.thesaurus import read_textfile
from .utils import logging, map_


def clean_institutions(directory):
    """
    Cleans all the institution fields in the records in the given directory using the
    institutions thesaurus (institutions.txt file).

    """

    logging.info("Applying thesaurus to institutions ...")

    # --------------------------------------------------------------------------
    # Loads documents.csv
    filename = os.path.join(directory, "documents.csv")
    if not os.path.isfile(filename):
        raise FileNotFoundError(f"The file '{filename}' does not exist.")
    documents = pd.read_csv(filename, sep=",", encoding="utf-8")
    # --------------------------------------------------------------------------

    if directory[-1] != "/":
        directory = directory + "/"

    #
    # Loads the thesaurus
    #
    thesaurus_file = directory + "institutions.txt"
    th = read_textfile(thesaurus_file)
    th = th.compile_as_dict()

    #
    # Copy affiliations to institutions
    #
    documents["institutions"] = documents.affiliations.map(
        lambda w: w.lower().strip(), na_action="ignore"
    )

    #
    # Cleaning
    #
    logging.info("Extract and cleaning institutions.")
    documents["institutions"] = map_(
        documents, "institutions", lambda w: th.apply_as_dict(w, strict=True)
    )

    logging.info("Extracting institution of first author ...")
    documents["institution_1st_author"] = documents.institutions.map(
        lambda w: w.split(";")[0] if isinstance(w, str) else w
    )

    # --------------------------------------------------------------------------
    documents.to_csv(
        directory + "documents.csv",
        sep=",",
        encoding="utf-8",
        index=False,
    )
    # --------------------------------------------------------------------------
    logging.info("The thesaurus was applied to institutions.")
