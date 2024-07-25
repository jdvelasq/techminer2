# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Apply Thesaurus 
===============================================================================

Cleans the organizations columns using the file organizations.txt, located in
the same directory as the documents.csv file.

>>> from techminer2.thesaurus.organizations import apply_thesaurus
>>> apply_thesaurus( # doctest: +SKIP
...     #
...     # DATABASE PARAMS:
...     root_dir="example/", 
... )
--INFO-- The example/thesauri/organizations.the.txt thesaurus file was applied to affiliations in all databases

"""
import glob
import os
import os.path

import pandas as pd  #  type: ignore

from .._core.load_inverted_thesaurus_as_dict import load_inverted_thesaurus_as_dict


def apply_thesaurus(
    #
    # DATABASE PARAMS:
    root_dir="./",
):
    """:meta private:"""

    # Read the thesaurus
    thesaurus_file = os.path.join(root_dir, "thesauri/organizations.the.txt")
    thesaurus = load_inverted_thesaurus_as_dict(thesaurus_file)

    # Apply thesaurus
    files = list(glob.glob(os.path.join(root_dir, "databases/_*.zip")))

    for file in files:
        records = pd.read_csv(file, encoding="utf-8", compression="zip")
        #
        #
        records = records.assign(organizations=records.affiliations.str.split("; "))
        records = records.assign(
            organizations=records.organizations.map(lambda x: ([thesaurus.get(y.strip(), y.strip()) for y in x] if isinstance(x, list) else x))
        )
        #
        records["organization_1st_author"] = records.organizations.str[0]
        #
        records = records.assign(organizations=records.organizations.map(lambda x: sorted(set(x)) if isinstance(x, list) else x))
        records = records.assign(organizations=records.organizations.str.join("; "))
        #
        #
        records.to_csv(file, sep=",", encoding="utf-8", index=False, compression="zip")

    print(f"--INFO-- The {thesaurus_file} thesaurus file was applied to affiliations in all databases")
