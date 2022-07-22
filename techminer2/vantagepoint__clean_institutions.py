"""
Clean Institutions
===============================================================================

Cleans the institutions columns using the file institutions.txt, located in
the same directory as the documents.csv file.


>>> directory = "data/regtech/"

>>> from techminer2 import vantagepoint__clean_institutions
>>> vantagepoint__clean_institutions(directory)
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


def vantagepoint__clean_institutions(directory="./"):
    """Apply institutions thesaurus."""

    # Read the thesaurus
    thesaurus_file = os.path.join(directory, "processed", "institutions.txt")
    thesaurus = read_textfile(thesaurus_file)
    thesaurus = thesaurus.compile_as_dict()

    # Apply thesaurus
    files = list(glob.glob(os.path.join(directory, "processed/_*.csv")))

    for file in files:
        records = pd.read_csv(file, encoding="utf-8")
        #
        #
        records = records.assign(raw_institutions=records.affiliations.str.split(";"))
        records = records.assign(
            raw_institutions=records.raw_institutions.map(
                lambda x: [thesaurus.apply_as_dict(y.strip()) for y in x]
                if isinstance(x, list)
                else x
            )
        )
        #
        records["institution_1st_author"] = records.raw_institutions.map(
            lambda w: w[0], na_action="ignore"
        )
        #
        records = records.assign(
            institutions=records.raw_institutions.map(
                lambda x: sorted(set(x)) if isinstance(x, list) else x
            )
        )
        records = records.assign(
            raw_institutions=records.raw_institutions.str.join("; ")
        )
        records = records.assign(institutions=records.institutions.str.join("; "))
        #
        #
        records.to_csv(file, sep=",", encoding="utf-8", index=False)

    sys.stdout.write(
        f"--INFO-- The {thesaurus_file} thesaurus file was applied to affiliations in all databases\n"
    )
