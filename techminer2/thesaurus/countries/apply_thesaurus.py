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

>>> from techminer2.thesaurus.countries import apply_thesaurus
>>> apply_thesaurus( # doctest: +SKIP
...     #
...     # DATABASE PARAMS:
...     root_dir="example/", 
...     )
--INFO-- The example/thesauri/countries.the.txt thesaurus file was applied to affiliations in all databases
--INFO-- The /Volumes/GitHub/techminer2/techminer2/thesauri_data/country-to-region.the.txt thesaurus file was applied to affiliations in all databases
--INFO-- The /Volumes/GitHub/techminer2/techminer2/thesauri_data/country-to-subregion.the.txt thesaurus file was applied to affiliations in all databases



"""
import glob
import os
import os.path
import sys

import pandas as pd  # type: ignore
import pkg_resources  # type: ignore

from .._core.load_inverted_thesaurus_as_dict import load_inverted_thesaurus_as_dict
from .._core.load_thesaurus_as_dict import load_thesaurus_as_dict


def apply_thesaurus(
    #
    # DATABASE PARAMS:
    root_dir="./",
):
    """:meta private:"""

    # ---------------------------------------------------------------------------------
    # countries thesaurus preparation
    thesaurus_file = os.path.join(root_dir, "thesauri/countries.the.txt")
    thesaurus = load_inverted_thesaurus_as_dict(thesaurus_file)

    # apply countries thesaurus
    files = list(glob.glob(os.path.join(root_dir, "databases/_*.zip")))
    for file in files:
        records = pd.read_csv(file, encoding="utf-8", compression="zip")
        #
        records["countries"] = (
            records.astype(str)
            .affiliations.str.split(";")
            .map(lambda affiliations: [thesaurus.get(affiliation.strip(), affiliation.strip()) for affiliation in affiliations])
        )
        #
        records["country_1st_author"] = records.countries.str[0]
        #
        records["countries"] = records["countries"].map(set, na_action="ignore")
        records["countries"] = records["countries"].map(sorted, na_action="ignore")
        records["countries"] = records["countries"].str.join("; ")
        #
        records.to_csv(file, sep=",", encoding="utf-8", index=False, compression="zip")

    sys.stdout.write(f"--INFO-- The {thesaurus_file} thesaurus file was applied to affiliations in all databases\n")

    # ---------------------------------------------------------------------------------
    # regions thesaurus preparation
    thesaurus_file = pkg_resources.resource_filename("techminer2", "thesauri_data/country-to-region.the.txt")

    # thesaurus_file = os.path.join(root_dir, "thesauri/country-to-region.the.txt")
    thesaurus = load_thesaurus_as_dict(thesaurus_file)
    thesaurus = {k: v[0] for k, v in thesaurus.items()}

    # apply countries thesaurus
    files = list(glob.glob(os.path.join(root_dir, "databases/_*.zip")))
    for file in files:
        records = pd.read_csv(file, encoding="utf-8", compression="zip")
        #
        records["regions"] = (
            records.astype(str)
            .countries.str.split(";")
            .map(lambda countries: [thesaurus.get(country.strip(), country.strip()) for country in countries])
        )
        #
        records["regions"] = records["regions"].map(set, na_action="ignore")
        records["regions"] = records["regions"].map(sorted, na_action="ignore")
        records["regions"] = records["regions"].str.join("; ")
        #
        records.to_csv(file, sep=",", encoding="utf-8", index=False, compression="zip")

    sys.stdout.write(f"--INFO-- The {thesaurus_file} thesaurus file was applied to affiliations in all databases\n")

    # ---------------------------------------------------------------------------------
    # regions thesaurus preparation
    thesaurus_file = pkg_resources.resource_filename("techminer2", "thesauri_data/country-to-subregion.the.txt")
    # thesaurus_file = os.path.join(root_dir, "thesauri/country-to-subregion.the.txt")
    thesaurus = load_thesaurus_as_dict(thesaurus_file)
    thesaurus = {k: v[0] for k, v in thesaurus.items()}

    # apply countries thesaurus
    files = list(glob.glob(os.path.join(root_dir, "databases/_*.zip")))
    for file in files:
        records = pd.read_csv(file, encoding="utf-8", compression="zip")
        #
        records["subregions"] = (
            records.astype(str)
            .countries.str.split(";")
            .map(lambda countries: [thesaurus.get(country.strip(), country.strip()) for country in countries])
        )
        #
        records["subregions"] = records["subregions"].map(set, na_action="ignore")
        records["subregions"] = records["subregions"].map(sorted, na_action="ignore")
        records["subregions"] = records["subregions"].str.join("; ")
        #
        records.to_csv(file, sep=",", encoding="utf-8", index=False, compression="zip")

    sys.stdout.write(f"--INFO-- The {thesaurus_file} thesaurus file was applied to affiliations in all databases\n")
