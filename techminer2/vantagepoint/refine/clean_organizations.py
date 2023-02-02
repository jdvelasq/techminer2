"""
Clean Organizations
===============================================================================

Cleans the organizations columns using the file organizations.txt, located in
the same directory as the documents.csv file.


>>> directory = "data/regtech/"

>>> from techminer2 import vantagepoint
>>> vantagepoint.refine.clean_organizations(directory)
--INFO-- The data/regtech/processed/organizations.txt thesaurus file was applied to affiliations in all databases



"""
import glob
import os
import os.path
import sys

import pandas as pd

from ..._lib._thesaurus import read_textfile


def clean_organizations(directory="./"):
    """Apply 'organizations.txt' thesaurus."""

    # Read the thesaurus
    thesaurus_file = os.path.join(directory, "processed", "organizations.txt")
    thesaurus = read_textfile(thesaurus_file)
    thesaurus = thesaurus.compile_as_dict()

    # Apply thesaurus
    files = list(glob.glob(os.path.join(directory, "processed/_*.csv")))

    for file in files:
        records = pd.read_csv(file, encoding="utf-8")
        #
        #
        records = records.assign(raw_organizations=records.affiliations.str.split(";"))
        records = records.assign(
            raw_organizations=records.raw_organizations.map(
                lambda x: [thesaurus.apply_as_dict(y.strip()) for y in x]
                if isinstance(x, list)
                else x
            )
        )
        #
        records["organization_1st_author"] = records.raw_organizations.map(
            lambda w: w[0], na_action="ignore"
        )
        #
        records = records.assign(
            organizations=records.raw_organizations.map(
                lambda x: sorted(set(x)) if isinstance(x, list) else x
            )
        )
        records = records.assign(
            raw_organizations=records.raw_organizations.str.join("; ")
        )
        records = records.assign(organizations=records.organizations.str.join("; "))
        #
        #
        records.to_csv(file, sep=",", encoding="utf-8", index=False)

    sys.stdout.write(
        f"--INFO-- The {thesaurus_file} thesaurus file was applied to affiliations in all databases\n"
    )
