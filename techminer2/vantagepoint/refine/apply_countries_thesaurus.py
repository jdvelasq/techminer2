# flake8: noqa
"""
Apply Countries Thesaurus 
===============================================================================

Cleans the country columns using the file countries.txt, located in
the same directory as the documents.csv file.


>>> root_dir = "data/regtech/"

>>> from techminer2 import vantagepoint
>>> vantagepoint.refine.apply_countries_thesaurus(root_dir)
--INFO-- The data/regtech/processed/countries.txt thesaurus file was applied to affiliations in all databases


# pylint: disable=line-too-long
"""
import glob
import os
import os.path
import sys

import pandas as pd

from ...thesaurus_utils import load_thesaurus_as_dict_reversed


def apply_countries_thesaurus(root_dir="./"):
    """Apply country thesaurus."""

    # thesaurus preparation
    thesaurus_file = os.path.join(root_dir, "processed", "countries.txt")
    thesaurus = load_thesaurus_as_dict_reversed(thesaurus_file)

    # apply thesaurus
    files = list(glob.glob(os.path.join(root_dir, "processed/_*.csv")))
    for file in files:
        records = pd.read_csv(file, encoding="utf-8")
        #
        records["raw_countries"] = (
            records.astype(str)
            .affiliations.str.split(";")
            .map(
                lambda affiliations: [
                    thesaurus.get(affiliation.strip(), affiliation.strip())
                    for affiliation in affiliations
                ]
            )
        )

        # records = records.assign(
        #     raw_countries=records.raw_countries.map(
        #         lambda affiliations: [thesaurus[affiliation] for affiliation in affiliations]
        #         if isinstance(x, list)
        #         else x
        #     )
        # )
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
        records = records.assign(
            raw_countries=records.raw_countries.str.join("; ")
        )
        records = records.assign(countries=records.countries.str.join("; "))
        #
        records.to_csv(file, sep=",", encoding="utf-8", index=False)

    sys.stdout.write(
        f"--INFO-- The {thesaurus_file} thesaurus file was applied to "
        "affiliations in all databases\n"
    )
