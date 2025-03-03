# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Replace Abbreviations
===============================================================================

>>> from techminer2.thesaurus.descriptors import CreateThesaurus
>>> CreateThesaurus(root_directory="example/", quiet=True).run()


>>> from techminer2.thesaurus.descriptors import ReplaceAbbreviations
>>> (
...     ReplaceAbbreviations()
...     #
...     # DATABASE:
...     .where_root_directory_is("example/")
...     #
...     .run()
... )
<BLANKLINE>
Abbreviations replacement completed successfully for file: ...scriptors.the.txt


"""
import re
import sys

from tqdm import tqdm  # type: ignore

from ...._internals.mixins import Params, ParamsMixin
from ..._internals import (
    internal__generate_user_thesaurus_file_path,
    internal__load_thesaurus_as_data_frame,
    internal__load_thesaurus_as_mapping,
    internal__print_thesaurus_header,
)


class ReplaceAbbreviations(
    ParamsMixin,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def step_01_get_descriptors_thesaurus_file_path(self):

        params = (
            Params()
            .update(**self.params.__dict__)
            .update(thesaurus_file="descriptors.the.txt")
        )

        self.descriptors_file_path = internal__generate_user_thesaurus_file_path(
            params=params
        )

    # -------------------------------------------------------------------------
    def step_02_get_abbrevaviations_thesaurus_file_path(self):

        params = (
            Params()
            .update(**self.params.__dict__)
            .update(thesaurus_file="abbreviations.the.txt")
        )

        self.abbreviations_file_path = internal__generate_user_thesaurus_file_path(
            params=params
        )

    # -------------------------------------------------------------------------
    def step_02_print_info_header(self):
        file_path = self.descriptors_file_path
        # field = self.params.field
        sys.stdout.write(f"Reemplacing abbreviations")
        sys.stdout.write(f"\n  File : {file_path}")
        sys.stdout.flush()

    # -------------------------------------------------------------------------
    def step_03_load_descriptor_thesaurus_as_data_frame(self):
        self.data_frame = internal__load_thesaurus_as_data_frame(
            self.descriptors_file_path
        )

    # -------------------------------------------------------------------------
    def step_04_load_abbreviations_thesaurus_as_mapping(self):
        self.abbreviations_dict = internal__load_thesaurus_as_mapping(
            self.abbreviations_file_path
        )

    # -------------------------------------------------------------------------
    def step_05_replace_abbreviations(self):

        for abbr, values in tqdm(
            self.abbreviations_dict.items(), desc="    Reemplacing abbreviations"
        ):
            #
            # Replace abbreviations in descriptor keys
            for value in values:
                self.data_frame["key"] = self.data_frame["key"].str.replace(
                    re.compile("^" + abbr + "$"), value, regex=True
                )
                self.data_frame["key"] = self.data_frame["key"].str.replace(
                    re.compile("^" + abbr + "_"), value + "_", regex=True
                )
                self.data_frame["key"] = self.data_frame["key"].str.replace(
                    re.compile("^" + abbr + " "), value + " ", regex=True
                )
                self.data_frame["key"] = self.data_frame["key"].str.replace(
                    re.compile("_" + abbr + "$"), "_" + value, regex=True
                )
                self.data_frame["key"] = self.data_frame["key"].str.replace(
                    re.compile(" " + abbr + "$"), " " + value, regex=True
                )
                self.data_frame["key"] = self.data_frame["key"].str.replace(
                    re.compile("_" + abbr + "_"), "_" + value + "_", regex=True
                )
                self.data_frame["key"] = self.data_frame["key"].str.replace(
                    re.compile(" " + abbr + "_"), " " + value + "_", regex=True
                )
                self.data_frame["key"] = self.data_frame["key"].str.replace(
                    re.compile("_" + abbr + " "), "_" + value + " ", regex=True
                )
                self.data_frame["key"] = self.data_frame["key"].str.replace(
                    re.compile(" " + abbr + " "), " " + value + " ", regex=True
                )

    # -------------------------------------------------------------------------
    def step_06_aggregate_descriptors_by_key(self):
        self.data_frame = self.data_frame.sort_values(by=["key", "value"])
        self.data_frame = self.data_frame.groupby("key", as_index=False).agg(
            {"value": list}
        )

    # -------------------------------------------------------------------------
    def step_07_save_thesaurus(self):

        with open(self.descriptors_file_path, "w", encoding="utf-8") as file:
            for _, row in self.data_frame.iterrows():
                file.write(row.key + "\n")
                for item in row.value:
                    file.write("    " + item + "\n")

    # -------------------------------------------------------------------------
    def step_print_info_tail(self):
        truncated_file_path = str(self.descriptors_file_path)
        if len(truncated_file_path) > 21:
            truncated_file_path = "..." + truncated_file_path[-17:]
        sys.stdout.write(
            f"\nAbbreviations replacement completed successfully for file: {truncated_file_path}"
        )
        sys.stdout.flush()

    # -------------------------------------------------------------------------
    def run(self):
        """:meta private:"""
        self.step_01_get_descriptors_thesaurus_file_path()
        self.step_02_get_abbrevaviations_thesaurus_file_path()
        self.step_03_load_descriptor_thesaurus_as_data_frame()
        self.step_04_load_abbreviations_thesaurus_as_mapping()
        self.step_05_replace_abbreviations()
        self.step_06_aggregate_descriptors_by_key()
        self.step_07_save_thesaurus()
        self.step_print_info_tail()
        return
