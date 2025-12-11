# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

"""
Zotero
===============================================================================

Example:

    >>> from techminer2.manuscript import Zotero
    >>> (
    ...     Zotero()
    ...     .where_root_directory_is("examples/fintech/")
    ...     .where_root_directory_is("../tm2_economics_of_wind_energy/")
    ...     .run()
    ... )



"""

import glob
import os
import re

from tqdm import tqdm  # type: ignore

from techminer2._internals.mixins import ParamsMixin
from techminer2.database._internals.io import (
    internal__load_filtered_records_from_database,
)


class Zotero(
    ParamsMixin,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def internal__load_zotero_ris_records(self):

        filepath = os.path.join(
            self.params.root_directory,
            "zotero.ris",
        )

        records = []
        stack = []
        with open(filepath, "r", encoding="utf-8") as f:
            for line in f:

                if line.strip() == "":
                    # Begins a new record
                    text = "".join(stack)
                    records.append(text)
                    stack = []
                else:
                    stack.append(line)

        self.zotero_ris_records = records

    # -------------------------------------------------------------------------
    def internal__load_first_paragraph(self):

        filepath = os.path.join(
            self.params.root_directory,
            "outputs",
            "section_1_introduction",
            "first_paragraph.txt",
        )

        with open(filepath, "r", encoding="utf-8") as f:
            self.first_paragraph = f.read()

    # -------------------------------------------------------------------------
    def internal__load_second_paragraph(self):

        filepath = os.path.join(
            self.params.root_directory,
            "outputs",
            "section_1_introduction",
            "second_paragraph.txt",
        )

        with open(filepath, "r", encoding="utf-8") as f:
            self.second_paragraph = f.read()

    # -------------------------------------------------------------------------
    def internal__load_cluster_full_summaries(self):

        files = glob.glob(
            os.path.join(
                self.params.root_directory,
                "outputs",
                "section_5_discussion",
                "*full_summary.txt",
            )
        )

        cluster_descriptions = []
        for file in sorted(files):
            with open(file, encoding="utf-8") as f:
                text = f.read().strip()
                text += "\n\n"
                cluster_descriptions.append(text)

        self.cluster_full_summaries = "\n\n".join(cluster_descriptions)

    # -------------------------------------------------------------------------
    def internal__aggregate_texts(self):

        texts = [
            self.first_paragraph,
            self.second_paragraph,
            self.cluster_full_summaries,
        ]

        self.text = "\n\n".join(texts)

    # -------------------------------------------------------------------------
    def internal__extract_ut_from_text(self):

        pattern = r"\[([^\]]+)\]"

        matches = re.findall(pattern, self.text)
        uts = []
        for match in matches:
            parts = re.split(r"[;,]\s*", match)
            uts.extend(parts)

        self.uts = sorted(set(ut.strip() for ut in uts if ut.strip().startswith("UT ")))

    # -------------------------------------------------------------------------
    def internal__load_titles(self):

        records = internal__load_filtered_records_from_database(params=self.params)
        records = records[records["record_no"].isin([int(ut[3:]) for ut in self.uts])]
        self.titles = records.raw_document_title.to_list()

    # -------------------------------------------------------------------------
    def internal__select_relevant_ris_records(self):

        zotero_records = {record: False for record in self.zotero_ris_records}

        for title in tqdm(
            self.titles,
            total=len(self.titles),
            desc="  Titles ",
            ncols=80,
        ):
            for record in zotero_records.keys():
                if title in record:
                    zotero_records[record] = True

        self.selected_ris_records = [
            record for record, selected in zotero_records.items() if selected
        ]

    # -------------------------------------------------------------------------
    def internal__save_selected_ris_records(self):

        filepath = os.path.join(
            self.params.root_directory,
            "zotero_selected.ris",
        )

        with open(filepath, "w", encoding="utf-8") as f:
            for record in self.selected_ris_records:
                f.write(record)
                f.write("\n\n")

    # -------------------------------------------------------------------------
    def run(self):

        self.internal__load_zotero_ris_records()
        self.internal__load_first_paragraph()
        self.internal__load_second_paragraph()
        self.internal__load_cluster_full_summaries()
        self.internal__aggregate_texts()
        self.internal__extract_ut_from_text()
        self.internal__load_titles()
        self.internal__select_relevant_ris_records()
        self.internal__save_selected_ris_records()
