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


## >>> from techminer2.thesaurus.organizations import ResetThesaurusToInitial
## >>> (
## ...     ResetThesaurusToInitial()
## ...     #
## ...     # DATABASE:
## ...     .where_directory_is("example/")
## ...     #
## ...     .build()
## ... )
--INFO-- The thesaurus file 'example/thesaurus/organizations.the.txt' has been reseted.

"""
import pathlib
import re

import pandas as pd  # type: ignore

from ..._internals.log_message import internal__log_message
from ..._internals.mixins import Params, ParamsMixin
from ...package_data.text_processing import internal__load_text_processing_terms
from .._internals import (
    internal__generate_system_thesaurus_file_path,
    internal__generate_user_thesaurus_file_path,
    internal__load_thesaurus_as_data_frame,
    internal__load_thesaurus_as_mapping,
)

# names sorted by proirity
NAMES = [
    "Min",  # ministry, ministerio
    "Univ",  # university, universidad, univedade, ...
    "Bank",  # bank, banco
    "Banco",
    "AG",  # agency, agencia
    "Counc",  # council, concilio, consejo
    "Conc",  # concilio, consejo
    "Com",  # comission, comision
    "Consortium",
    "Politec",  # polytechnic, politecnico
    "Polytech",  # polytechnic, politecnico
    "Hosp",  # hospital
    "Assn",  # association
    "Asoc",  # asociacion
    "Soc",
    "Consor",
    "Co",
    "Org",
    "Inc",
    "Ltd",
    "Off",
    "Corp",
    "Gob",
    "Gov",
    "Found",
    "Fund",
    "Inst",
    "Coll",
    "Sch",
]


class ResetThesaurusToInitialState(
    ParamsMixin,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def step_01_generate_file_path(self):
        params = Params().update(
            thesaurus_file="countries.the.txt",
            root_dir=self.params.root_dir,
        )
        file_path = internal__generate_user_thesaurus_file_path(params)
        return file_path

    # -------------------------------------------------------------------------
    def step_02_generate_data_frame_from_country_thesaurus(self, file_path):

        params = Params().update(
            thesaurus_file="countries.the.txt",
            root_dir=self.params.root_dir,
        )
        file_path = internal__generate_user_thesaurus_file_path(params)
        data_frame = internal__load_thesaurus_as_data_frame(file_path)
        data_frame = data_frame.rename(
            columns={"key": "country", "value": "raw_affiliation"}
        )
        return data_frame

    # -------------------------------------------------------------------------
    def step_03_add_country_alpta3_code_column(self, data_frame):

        file_path = internal__generate_system_thesaurus_file_path(
            "geography/country_to_alpha3.the.txt"
        )
        mapping = internal__load_thesaurus_as_data_frame(file_path)

        data_frame = data_frame.copy()
        data_frame["code"] = "unknown"
        for country, code in mapping.items():
            data_frame.loc[data_frame.country == country, "code"] = code

        return data_frame

    # -------------------------------------------------------------------------
    def step_04_add_candidate_organization_column(self, data_frame):
        data_frame = data_frame.copy()
        data_frame["organization"] = data_frame.raw_affiliation
        return data_frame

    # -------------------------------------------------------------------------
    def step_05_replace_abbr_names_in_organizations(self, data_frame):

        # loads the abbreviation thesaurus
        file_path = internal__generate_system_thesaurus_file_path(
            "geography/country_to_alpha3.the.txt"
        )
        mapping = internal__load_thesaurus_as_mapping(file_path)

        # replaces the abbreviations
        for word, abbr in mapping.items():
            data_frame["organization"] = data_frame["organization"].str.replace(
                r"\b" + word + r"\b", abbr[0], regex=True
            )

        # remove leading and trailing spaces
        data_frame["organization"] = data_frame["organization"].str.strip()

        return data_frame

    # -------------------------------------------------------------------------
    def step_06_adds_a_empty_organizations_column(self, data_frame):
        """Adds empty organizations."""

        data_frame = data_frame.copy()
        data_frame["organizations"] = pd.NA
        return data_frame

    # -------------------------------------------------------------------------
    def step_07_load_known_organizations(self):
        return internal__load_text_processing_terms("known_organizations.txt")

    # -------------------------------------------------------------------------
    def step_08_assign_known_names_to_organizations(
        self, data_frame, known_organizations
    ):
        for org in known_organizations:
            data_frame.loc[
                data_frame.raw_affiliation.astype(str).str.contains(org, case=False),
                "organization",
            ] = org
        return data_frame

    # -------------------------------------------------------------------------
    def step_09_assign_names_by_priority(self, data_frame):

        def select_name(affiliation):
            for name in NAMES:
                regex = r"\b" + name + r"\b"

                if re.search(regex, affiliation, re.IGNORECASE):
                    parts = affiliation.split(",")
                    for part in parts:
                        if re.search(regex, part, re.IGNORECASE):
                            return part.strip()
            return affiliation

        #
        # Main code:
        #
        data_frame = data_frame.copy()
        for index, row in data_frame.iterrows():
            if row.organization is pd.NA:
                data_frame.loc[index, "organization"] = select_name(
                    data_frame.loc[index, "affiliation"]
                )

        data_frame["organization"] = data_frame["organization"].map(select_name)
        return data_frame

    # -------------------------------------------------------------------------
    def step_10_format_organization_names(self, data_frame):
        data_frame = data_frame.copy()
        data_frame["organization"] = (
            data_frame["organization"].astype(str) + " (" + data_frame["code"] + ")"
        )
        return data_frame

    # -------------------------------------------------------------------------
    def step_11_save_data_frame_as_thesaurus(self, data_frame):

        data_frame = data_frame.sort_values(["organization", "raw_affiliation"])
        data_frame = data_frame.groupby("organization", as_index=False).agg(
            {"raw_affiliation": list}
        )

        file_path = (
            pathlib.Path(self.params.root_dir) / "thesaurus/organizations.the.txt"
        )

        with open(file_path, "w", encoding="utf-8") as file:
            for _, row in data_frame.iterrows():
                file.write(row.organization + "\n")
                for aff in row.raw_affiliation:
                    file.write("    " + aff + "\n")

    # -------------------------------------------------------------------------
    def build(self):
        """:meta private:"""

        file_path = self.step_01_generate_file_path()

        # -------------------------------------------------------------------------
        internal__log_message(
            msgs=[
                "Reseting thesaurus to initial state.",
                f"  Thesaurus file: '{file_path}'.",
            ],
            prompt_flag=self.params.prompt_flag,
        )
        # -------------------------------------------------------------------------

        data_frame = self.step_02_generate_data_frame_from_country_thesaurus(file_path)
        data_frame = self.step_03_add_country_alpta3_code_column(data_frame)
        data_frame = self.step_04_add_candidate_organization_column(data_frame)
        data_frame = self.step_05_replace_abbr_names_in_organizations(data_frame)
        data_frame = self.step_06_adds_a_empty_organizations_column(data_frame)
        known_organizations = self.step_07_load_known_organizations()
        data_frame = self.step_08_assign_known_names_to_organizations(
            data_frame, known_organizations
        )
        data_frame = self.step_09_assign_names_by_priority(data_frame)
        data_frame = self.step_10_format_organization_names(data_frame)
        self.step_11_save_data_frame_as_thesaurus(data_frame)

        # -------------------------------------------------------------------------
        internal__log_message(
            msgs=[
                "  Done.",
            ],
            prompt_flag=-1,
        )


# =============================================================================
