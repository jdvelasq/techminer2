# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Reset Thesaurus to Initial
===============================================================================


>>> from techminer2.thesaurus.countries import CreateThesaurus
>>> (
...     CreateThesaurus()
...     #
...     # DATABASE:
...     .where_directory_is("example/")
...     #
...     .build()
... )


"""
import pathlib
import sys

import pandas as pd  # type: ignore
import pkg_resources  # type: ignore

from ..._internals.log_message import internal__log_message
from ..._internals.mixins import ParamsMixin
from ...database._internals.io import internal__load_records
from .__apply_thesaurus import ApplyThesaurus as ApplyCountryThesaurus


class CreateThesaurus(
    ParamsMixin,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def step_01_get_thesaurus_file_path(self):
        return pathlib.Path(self.params.root_dir) / "thesaurus/countries.the.txt"

    # -------------------------------------------------------------------------
    def step_02_create_affiliations_data_frame(self, records):

        if "affiliations" not in records.columns:
            raise ValueError(
                "Column 'affiliations' do not exists in any databases or it is empty."
            )

        affiliations = records.affiliations
        affiliations = affiliations.dropna()
        affiliations = affiliations.str.split(";")
        affiliations = affiliations.explode()
        affiliations = affiliations.str.strip()
        affiliations = affiliations.drop_duplicates()

        frame = pd.DataFrame({"affiliations": affiliations})

        return frame

    # -------------------------------------------------------------------------
    def step_03_create_country_column_from_affiliations(self, affiliations):
        affiliations = affiliations.copy()
        affiliations = affiliations.assign(country=affiliations.affiliations)
        return affiliations

    # -------------------------------------------------------------------------
    def step_04_extract_country_name_from_text(self, affiliations):
        """Extracts the country component from the 'country' column."""

        affiliations = affiliations.copy()
        affiliations["country"] = (
            affiliations["country"].str.split(",").str[-1].str.strip()
        )
        return affiliations

    # -------------------------------------------------------------------------
    def step_05_homogenize_country_names(self, affiliations):
        """Fix variations in country names."""

        replacements = [
            ("Bosnia and Herz.", "Bosnia and Herzegovina"),
            ("Brasil", "Brazil"),
            ("Czech Republic", "Czechia"),
            ("Espana", "Spain"),
            ("Macao", "China"),
            ("Macau", "China"),
            ("N. Cyprus", "Cyprus"),
            ("Peoples R China", "China"),
            ("Rusia", "Russia"),
            ("Russian Federation", "Russia"),
            ("Syrian Arab Republic", "Syria"),
            ("United States of America", "United States"),
            ("USA", "United States"),
            ("Viet-Nam", "Vietnam"),
            ("Viet Nam", "Vietnam"),
        ]

        #
        # Replaces the names in affiliations
        affiliations = affiliations.copy()
        for pat, repl in replacements:
            affiliations["country"] = affiliations["country"].str.replace(
                pat, repl, regex=False
            )

        #
        # Returns the affiliations with the fixed country names
        return affiliations

    # -------------------------------------------------------------------------
    def step_06_check_country_names(self, affiliations):
        """Extract the country based on a regex."""

        #
        # Loads country names from thesaurus
        file_path = pkg_resources.resource_filename(
            "techminer2",
            "package_data/thesaurus/geography/alpha3_to_country.the.txt",
        )
        countries = []
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                if line.startswith(" "):
                    countries.append(line.strip())

        #
        # Checks country names
        affiliations = affiliations.copy()
        affiliations["country"] = affiliations["country"].map(
            lambda x: x if x in countries else "[UNKNWON]"
        )
        return affiliations

    # -------------------------------------------------------------------------
    def step_07_group_affiliations_by_country(self, affiliations):
        affiliations = affiliations.copy()
        affiliations = affiliations.sort_values(["country", "affiliations"])
        affiliations = affiliations.groupby("country", as_index=False).agg(
            {"affiliations": list}
        )
        return affiliations

    # -------------------------------------------------------------------------
    def step_08_create_thesaurus_file(self, affiliations, file_path):

        with open(file_path, "w", encoding="utf-8") as file:
            for _, row in affiliations.iterrows():
                file.write(row.country + "\n")
                for aff in row.affiliations:
                    file.write("    " + aff + "\n")

    # -------------------------------------------------------------------------
    def build(self):
        """:meta private:"""

        file_path = self.step_01_get_thesaurus_file_path()

        # -------------------------------------------------------------------------
        sys.stdout.write("\nINFO  Creating thesaurus file.")
        sys.stdout.write(f"\n        Thesaurus file: {file_path}.")
        sys.stdout.write("\n          Source field: 'affiliations'.")
        sys.stdout.flush()

        # -------------------------------------------------------------------------

        records = internal__load_records(params=self.params)
        #
        affiliations = self.step_02_create_affiliations_data_frame(records)
        affiliations = self.step_03_create_country_column_from_affiliations(
            affiliations
        )
        affiliations = self.step_04_extract_country_name_from_text(affiliations)
        affiliations = self.step_05_homogenize_country_names(affiliations)
        affiliations = self.step_06_check_country_names(affiliations)
        affiliations = self.step_07_group_affiliations_by_country(affiliations)
        #
        self.step_08_create_thesaurus_file(affiliations, file_path)

        # -------------------------------------------------------------------------
        ApplyCountryThesaurus().update(**self.params.__dict__).with_prompt_flag(
            -1
        ).build()

        # -------------------------------------------------------------------------
        # internal__log_message(msgs="  Done.", prompt_flag=-1)


# =============================================================================
