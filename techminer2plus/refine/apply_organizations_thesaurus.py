# flake8: noqa
"""
Apply Organizations Thesaurus 
===============================================================================

Cleans the organizations columns using the file organizations.txt, located in
the same directory as the documents.csv file.


>>> root_dir = "data/regtech/"

>>> from techminer2 import vantagepoint
>>> vantagepoint.refine.apply_organizations_thesaurus(root_dir)
--INFO-- The data/regtech/organizations.txt thesaurus file was \
applied to affiliations in all databases


# pylint: disable=line-too-long
"""
import glob
import os
import os.path
import sys

import pandas as pd

from ..thesaurus import load_system_thesaurus_as_dict_reversed


def apply_organizations_thesaurus(root_dir="./"):
    """Apply 'organizations.txt' thesaurus."""

    # Read the thesaurus
    thesaurus_file = os.path.join(root_dir, "organizations.txt")
    thesaurus = load_system_thesaurus_as_dict_reversed(thesaurus_file)

    # Apply thesaurus
    files = list(glob.glob(os.path.join(root_dir, "databases/_*.csv")))

    for file in files:
        records = pd.read_csv(file, encoding="utf-8")
        #
        #
        records = records.assign(
            raw_organizations=records.affiliations.str.split(";")
        )
        records = records.assign(
            raw_organizations=records.raw_organizations.map(
                lambda x: [thesaurus.get(y.strip(), y.strip()) for y in x]
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
        records = records.assign(
            organizations=records.organizations.str.join("; ")
        )
        #
        #
        records.to_csv(file, sep=",", encoding="utf-8", index=False)

    sys.stdout.write(
        f"--INFO-- The {thesaurus_file} thesaurus file was applied to "
        "affiliations in all databases\n"
    )
