"""
Apply institutions thesaurus
===============================================================================

Cleans the institutions columns using the file institutions.txt, located in
the same directory as the documents.csv file.

>>> from techminer2 import *
>>> directory = "data/regtech/"

>>> create_institutions_thesaurus(directory)
--INFO-- Creating institutions thesaurus
--INFO-- Affiliations without country detected - check file data/processed/ignored_affiliations.txt
--INFO-- Affiliations without country detected - check file data/ignored_affiliations.txt
--INFO-- Thesaurus file 'data/processed/institutions.txt' created

>>> apply_institutions_thesaurus(directory)
--INFO-- Applying thesaurus to institutions
--INFO-- The thesaurus was applied to institutions in all databases


"""
import glob
import os
import os.path
import sys

import pandas as pd

from .map_ import map_
from .thesaurus import read_textfile


def apply_institutions_thesaurus(directory="./"):
    """
    Cleans all the institution fields in the records in the given directory using the
    institutions thesaurus (institutions.txt file).

    """
    sys.stdout.write("--INFO-- Applying thesaurus to institutions\n")

    # Read the thesaurus
    thesaurus_file = os.path.join(directory, "processed", "institutions.txt")
    th = read_textfile(thesaurus_file)
    th = th.compile_as_dict()

    files = list(glob.glob(os.path.join(directory, "processed/_*.csv")))

    for file in files:
        records = pd.read_csv(file, encoding="utf-8")
        records["institutions"] = records.affiliations.map(
            lambda w: w.lower().strip(), na_action="ignore"
        )
        records["institutions"] = map_(
            records, "institutions", lambda w: th.apply_as_dict(w, strict=True)
        )
        records["institution_1st_author"] = records.institutions.map(
            lambda w: w.split(";")[0] if isinstance(w, str) else w
        )
        records.to_csv(file, sep=",", encoding="utf-8", index=False)

    sys.stdout.write(
        "--INFO-- The thesaurus was applied to institutions in all databases\n"
    )
