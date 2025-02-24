# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Create thesaurus
===============================================================================


>>> from techminer2.thesaurus.references import CreateThesaurus
>>> (
...     CreateThesaurus()
...     #
...     # DATABASE:
...     .where_directory_is("example/")
...     #
...     .build()
... )
<BLANKLINE>
Thesaurus creation completed successfully for file: ...lobal_references.the.txt


"""
import pathlib
import re
import sys

import pandas as pd  # type: ignore
from textblob import Word  # type: ignore
from tqdm import tqdm  # type: ignore

from ..._internals.mixins import ParamsMixin
from ...database._internals.io import (
    internal__load_filtered_database,
    internal__load_records,
)
from ...package_data.text_processing import internal__load_text_processing_terms
from .._internals import (
    internal__generate_system_thesaurus_file_path,
    internal__generate_user_thesaurus_file_path,
    internal__load_thesaurus_as_mapping,
    internal__print_thesaurus_header,
)

tqdm.pandas()


def clean_text(text):
    text = (
        text.str.lower()
        .str.replace(".", "", regex=False)
        .str.replace(",", "", regex=False)
        .str.replace(":", "", regex=False)
        .str.replace("-", " ", regex=False)
        .str.replace("_", " ", regex=False)
        .str.replace("'", "", regex=False)
        .str.replace("(", "", regex=False)
        .str.replace(")", "", regex=False)
        .str.replace("  ", " ", regex=False)
    )
    return text


class CreateThesaurus(
    ParamsMixin,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def step_01_get_thesaurus_file_path(self):
        self.file_path = internal__generate_user_thesaurus_file_path(params=self.params)

    # -------------------------------------------------------------------------
    def step_02_print_info_header(self):
        file_path = self.file_path
        field = self.params.field
        sys.stderr.write(f"\nCreating thesaurus from '{field}' field: {file_path}")
        sys.stderr.flush()

    # -------------------------------------------------------------------------
    def step_03_create_main_documents_data_frame(self):

        sys.stderr.write(f"\n  Creating main_documents data frame")
        sys.stderr.flush()

        # loads the dataframe
        main_documents = internal__load_filtered_database(self.params)
        main_documents = main_documents[main_documents.global_citations > 0]
        main_documents = main_documents[
            ["record_id", "document_title", "authors", "year"]
        ]
        main_documents = main_documents.dropna()

        # extracts the first author surname
        main_documents["first_author"] = (
            main_documents["authors"]
            .astype(str)
            .str.split(" ")
            .map(lambda x: x[0].lower())
        )

        # formats the document title field
        main_documents["document_title"] = (
            main_documents["document_title"].astype(str).str.lower()
        )
        main_documents["document_title"] = clean_text(main_documents["document_title"])

        # formats the authors field
        main_documents["authors"] = clean_text(main_documents["authors"])

        # formats the year field
        main_documents["year"] = main_documents["year"].astype(str)

        # sorts the dataframe
        main_documents = main_documents.sort_values(by=["record_id"])

        self.main_documents = main_documents

    # -------------------------------------------------------------------------
    def step_04_create_references_data_frame(self):

        sys.stderr.write(f"\n  Creating references data frame")
        sys.stderr.flush()

        # loads the dataframe
        references = internal__load_records(self.params)
        references = references[["raw_global_references"]].dropna()
        references = references.rename({"raw_global_references": "text"}, axis=1)

        references["text"] = references["text"].str.split(";")
        references = references.explode("text")
        references["text"] = references["text"].str.strip()
        references = references.drop_duplicates()
        references = references.reset_index(drop=True)

        references["key"] = clean_text(references["text"])

        self.references = references

    # -------------------------------------------------------------------------
    def step_05_create_thesaurus(self):

        sys.stderr.write("\n")

        thesaurus = {}
        for _, row in tqdm(
            self.main_documents.iterrows(),
            total=self.main_documents.shape[0],
            desc="  Homogenizing global references",
        ):

            refs = self.references.copy()

            # filters by first author
            refs = refs.loc[
                refs.key.str.lower().str.contains(row.first_author.lower()), :
            ]

            # filters by year
            refs = refs.loc[refs.key.str.lower().str.contains(row.year), :]

            # filters by document title
            refs = refs.loc[
                refs.key.str.lower().str.contains(
                    re.escape(row.document_title[:50].lower())
                ),
                :,
            ]

            if len(refs) > 0:
                thesaurus[row.record_id] = sorted(refs.text.tolist())
                self.references = self.references.drop(refs.index)

        self.thesaurus = thesaurus

    # -------------------------------------------------------------------------
    def step_06_write_thesaurus_to_disk(self):

        with open(self.file_path, "w", encoding="utf-8") as file:
            for key in sorted(self.thesaurus.keys()):
                values = self.thesaurus[key]
                file.write(key + "\n")
                for value in sorted(values):
                    file.write("    " + value + "\n")

    # -------------------------------------------------------------------------
    def step_07_print_info_tail(self):
        internal__print_thesaurus_header(file_path=self.file_path)
        ##
        truncated_file_path = str(self.file_path)
        if len(truncated_file_path) > 28:
            truncated_file_path = "..." + truncated_file_path[-24:]
        sys.stdout.write(
            f"\nThesaurus creation completed successfully for file: {truncated_file_path}"
        )
        sys.stdout.flush()

    # -------------------------------------------------------------------------
    def build(self):
        """:meta private:"""

        self.params.update(
            thesaurus_file="global_references.the.txt",
            field="global_references",
        )

        self.step_01_get_thesaurus_file_path()
        self.step_02_print_info_header()
        self.step_03_create_main_documents_data_frame()
        self.step_04_create_references_data_frame()
        self.step_05_create_thesaurus()
        self.step_06_write_thesaurus_to_disk()
        self.step_07_print_info_tail()


# def _apply_thesaurus(root_dir):
#     # Apply the thesaurus to raw_global_references

#     file_path = pathlib.Path(root_dir) / "thesaurus/global_references.the.txt"
#     th = internal__load_reversed_thesaurus_as_mapping(file_path=file_path)

#     dataframe = pd.read_csv(
#         pathlib.Path(root_dir) / "databases/database.csv.zip",
#         encoding="utf-8",
#         compression="zip",
#     )

#     # creates a list of references
#     dataframe["global_references"] = dataframe["raw_global_references"].str.split("; ")

#     # replace the oriignal references by the record_id
#     dataframe["global_references"] = dataframe["global_references"].map(
#         lambda x: [th[t] for t in x if t in th.keys()], na_action="ignore"
#     )
#     dataframe["global_references"] = dataframe["global_references"].map(
#         lambda x: pd.NA if x == [] else x, na_action="ignore"
#     )
#     dataframe["global_references"] = dataframe["global_references"].map(
#         lambda x: "; ".join(sorted(x)) if isinstance(x, list) else x
#     )

#     dataframe.to_csv(
#         pathlib.Path(root_dir) / "databases/database.csv.zip",
#         sep=",",
#         encoding="utf-8",
#         index=False,
#         compression="zip",
#     )
