"""
Clean Institutions
===============================================================================

Cleans the institutions columns using the file institutions.txt, located in
the same directory as the documents.csv file.

>>> from techminer2 import *
>>> directory = "/workspaces/techminer2/data/"
>>> clean_institutions(directory)
- INFO - Applying thesaurus to institutions ...
- INFO - Extract and cleaning institutions.
- INFO - Extracting institution of first author ...
- INFO - The thesaurus was applied to institutions.

"""


import os
import os.path

from . import logging
from ._read_records import read_all_records
from .map_ import map_
from .save_documents import save_documents
from .thesaurus import read_textfile


def clean_institutions(directory):
    """
    Cleans all the institution fields in the records in the given directory using the
    institutions thesaurus (institutions.txt file).

    """

    logging.info("Applying thesaurus to institutions ...")

    # --------------------------------------------------------------------------
    # Loads documents.csv
    documents = read_all_records(directory)

    #
    # Loads the thesaurus
    #
    thesaurus_file = os.path.join(directory, "processed", "institutions.txt")
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
    save_documents(documents, directory)
    logging.info("The thesaurus was applied to institutions.")
