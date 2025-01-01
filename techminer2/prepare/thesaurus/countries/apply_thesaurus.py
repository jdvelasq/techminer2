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

## >>> from techminer2.prepare.thesaurus.countries import apply_thesaurus
## >>> apply_thesaurus( # doctest: +SKIP
## ...     #
## ...     # DATABASE PARAMS:
## ...     root_dir="example/", 
## ...     )
--INFO-- The example/thesauri/countries.the.txt thesaurus file was applied to affiliations in all databases
--INFO-- The /Volumes/GitHub/techminer2/techminer2/thesauri_data/country-to-region.the.txt thesaurus file was applied to affiliations in all databases
--INFO-- The /Volumes/GitHub/techminer2/techminer2/thesauri_data/country-to-subregion.the.txt thesaurus file was applied to affiliations in all databases



"""
import glob
import os
import os.path
import pathlib
import sys

import pandas as pd  # type: ignore
import pkg_resources  # type: ignore

from ..internals.thesaurus__read_as_dict import thesaurus__read_as_dict
from ..internals.thesaurus__read_reversed_as_dict import (
    thesaurus__read_reversed_as_dict,
)


def apply_thesaurus(
    #
    # DATABASE PARAMS:
    root_dir="./",
):
    """:meta private:"""

    def apply_countries_thesaurus():

        thesaurus_file = os.path.join(root_dir, "thesauri/countries.the.txt")
        thesaurus = thesaurus__read_reversed_as_dict(thesaurus_file)

        # apply countries thesaurus
        dataframe = pd.read_csv(
            pathlib.Path(root_dir) / "databases/database.csv.zip",
            encoding="utf-8",
            compression="zip",
        )

        #
        dataframe["countries"] = dataframe.astype(str).affiliations
        dataframe["countries"] = dataframe["countries"].str.split(";")
        dataframe["countries"] = dataframe["countries"].map(
            lambda affiliations: [
                thesaurus.get(affiliation.strip(), affiliation.strip())
                for affiliation in affiliations
            ]
        )

        #
        dataframe["country_1st_author"] = dataframe.countries.str[0]

        dataframe["countries"] = dataframe["countries"].map(set, na_action="ignore")
        dataframe["countries"] = dataframe["countries"].map(sorted, na_action="ignore")
        dataframe["countries"] = dataframe["countries"].str.join("; ")
        #

        dataframe.to_csv(
            pathlib.Path(root_dir) / "databases/database.csv.zip",
            sep=",",
            encoding="utf-8",
            index=False,
            compression="zip",
        )

        sys.stdout.write(
            f"--INFO-- The {thesaurus_file} thesaurus file was applied to affiliations in all databases\n"
        )

    #
    #
    #
    def apply_country_to_region_thesaurus():

        thesaurus_file = pkg_resources.resource_filename(
            "techminer2", "package_data/thesaurus/geography/country-to-region.the.txt"
        )

        thesaurus = thesaurus__read_as_dict(thesaurus_file)
        thesaurus = {k: v[0] for k, v in thesaurus.items()}

        # apply countries thesaurus
        dataframe = pd.read_csv(
            pathlib.Path(root_dir) / "databases/database.csv.zip",
            encoding="utf-8",
            compression="zip",
        )

        dataframe["regions"] = dataframe["countries"]
        dataframe["regions"] = dataframe["regions"].str.split("; ")
        dataframe["regions"] = dataframe["regions"].map(
            lambda countries: [
                thesaurus.get(country.strip(), country.strip()) for country in countries
            ],
            na_action="ignore",
        )

        #
        dataframe["regions"] = dataframe["regions"].map(set, na_action="ignore")
        dataframe["regions"] = dataframe["regions"].map(sorted, na_action="ignore")
        dataframe["regions"] = dataframe["regions"].str.join("; ")

        dataframe.to_csv(
            pathlib.Path(root_dir) / "databases/database.csv.zip",
            sep=",",
            encoding="utf-8",
            index=False,
            compression="zip",
        )
        sys.stdout.write(
            f"--INFO-- The {thesaurus_file} thesaurus file was applied to affiliations in all databases\n"
        )

    #
    #
    #
    def apply_country_to_subregion_thesaurus():

        thesaurus_file = pkg_resources.resource_filename(
            "techminer2",
            "package_data/thesaurus/geography/country-to-subregion.the.txt",
        )
        thesaurus = thesaurus__read_as_dict(thesaurus_file)
        thesaurus = {k: v[0] for k, v in thesaurus.items()}

        dataframe = pd.read_csv(
            pathlib.Path(root_dir) / "databases/database.csv.zip",
            encoding="utf-8",
            compression="zip",
        )

        dataframe["subregions"] = dataframe["countries"]
        dataframe["subregions"] = dataframe["subregions"].str.split("; ")
        dataframe["subregions"] = dataframe["subregions"].map(
            lambda countries: [
                thesaurus.get(country.strip(), country.strip()) for country in countries
            ],
            na_action="ignore",
        )

        #
        dataframe["subregions"] = dataframe["subregions"].map(set, na_action="ignore")
        dataframe["subregions"] = dataframe["subregions"].map(
            sorted, na_action="ignore"
        )
        dataframe["subregions"] = dataframe["subregions"].str.join("; ")

        dataframe.to_csv(
            pathlib.Path(root_dir) / "databases/database.csv.zip",
            sep=",",
            encoding="utf-8",
            index=False,
            compression="zip",
        )

        sys.stdout.write(
            f"--INFO-- The {thesaurus_file} thesaurus file was applied to affiliations in all databases\n"
        )

    #
    #
    # Main code
    #
    #
    apply_countries_thesaurus()
    apply_country_to_region_thesaurus()
    apply_country_to_subregion_thesaurus()
