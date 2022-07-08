"""
Apply Country Thesaurus
===============================================================================

Cleans the country columns using the file countries.txt, located in
the same directory as the documents.csv file.

>>> from techminer2 import *
>>> directory = "data/regtech/"

>>> create_country_thesaurus(directory)

>>> apply_country_thesaurus(directory)


"""
import glob
import os
import os.path
import sys

import pandas as pd

from .thesaurus import read_textfile


def apply_country_thesaurus(directory="./"):
    """Apply country thesaurus."""

    # thesaurus preparation
    thesaurus_file = os.path.join(directory, "processed", "countries.txt")
    thesaurus = read_textfile(thesaurus_file)
    thesaurus = thesaurus.compile_as_dict()

    # apply thesaurus
    files = list(glob.glob(os.path.join(directory, "processed/_*.csv")))
    for file in files:
        records = pd.read_csv(file, encoding="utf-8")
        #
        records = records.assign(raw_countries=records.affiliations.str.split(";"))
        records = records.assign(
            raw_countries=records.raw_countries.map(
                lambda x: [thesaurus.apply_as_dict(y.strip()) for y in x]
                if isinstance(x, list)
                else x
            )
        )
        #
        records["country_1st_author"] = records.raw_countries.map(
            lambda w: w[0], na_action="ignore"
        )
        #
        records = records.assign(
            countries=records.raw_countries.map(
                lambda x: sorted(set(x)) if isinstance(x, list) else x
            )
        )
        records = records.assign(raw_countries=records.raw_countries.str.join("; "))
        records = records.assign(countries=records.countries.str.join("; "))
        #
        records.to_csv(file, sep=",", encoding="utf-8", index=False)

    sys.stdout.write(
        f"--INFO-- The {thesaurus_file} thesaurus file was applied to affiliations in all databases\n"
    )
