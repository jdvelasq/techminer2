# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Compress Thesaurus
===============================================================================


Example:
    >>> # TEST PREPARATION
    >>> import sys
    >>> from io import StringIO
    >>> from techminer2.thesaurus.user import InitializeThesaurus, CompressThesaurus

    >>> # Redirecting stderr to avoid messages during doctests
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()


    >>> # Reset the thesaurus to initial state
    >>> InitializeThesaurus(thesaurus_file="demo.the.txt", field="raw_descriptors",
    ...     root_directory="example/", quiet=True).run()

    >>> # Creates, configures, an run the compressor
    >>> compressor = (
    ...     CompressThesaurus(tqdm_disable=True, use_colorama=False)
    ...     .with_thesaurus_file("demo.the.txt")
    ...     .where_root_directory_is("example/")
    ... )
    >>> compressor.run()

    >>> # Capture and print stderr output to test the code using doctest
    >>> output = sys.stderr.getvalue()
    >>> sys.stderr = original_stderr
    >>> print(output) # doctest: +ELLIPSIS
    Compressing thesaurus keys...
                      File : example/data/thesaurus/demo.the.txt
      Keys reduced from 1723 to 1723
      Compression process completed successfully
    <BLANKLINE>
    <BLANKLINE>


"""

import re
import sys

import pandas as pd
from colorama import Fore, init
from tqdm import tqdm  # type: ignore

from ...._internals.mixins import ParamsMixin
from ....database.metrics.performance import DataFrame
from ....package_data.text_processing import internal__load_text_processing_terms
from ..._internals import ThesaurusMixin, internal__print_thesaurus_header


class CompressThesaurus(
    ParamsMixin,
    ThesaurusMixin,
):
    """:meta private:"""

    #
    # NOTIFICATIONS:
    # -------------------------------------------------------------------------
    def internal__notify_process_start(self):

        file_path = str(self.thesaurus_path)
        if len(file_path) > 72:
            file_path = "..." + file_path[-68:]

        if self.params.use_colorama:
            filename = str(file_path).split("/")[-1]
            file_path = file_path.replace(filename, f"{Fore.RESET}{filename}")
            file_path = Fore.LIGHTBLACK_EX + file_path

        sys.stderr.write(f"Compressing thesaurus keys...\n")
        sys.stderr.write(f"                  File : {file_path}\n")
        sys.stderr.flush()

    # -------------------------------------------------------------------------
    def internal__notify_process_end(self):

        sys.stderr.write(
            f"  Keys reduced from {self.n_initial_keys} to {self.n_final_keys}\n"
        )
        sys.stderr.write(f"  Compression process completed successfully\n\n")
        sys.stderr.flush()

    #
    # ALGORITHM:
    # -------------------------------------------------------------------------
    def internal__get_keywords(self):

        self.keywords = (
            DataFrame()
            .with_field("raw_keywords")
            .having_terms_ordered_by("OCC")
            .where_root_directory_is(self.params.root_directory)
            .where_database_is("main")
        ).run()

        known_keywords = internal__load_text_processing_terms("known_noun_phrases.txt")

        self.keywords = self.keywords[self.keywords.index.isin(known_keywords)]

        self.keywords["length"] = self.keywords.index.str.split("_").str.len()
        self.keywords = self.keywords.sort_values(
            by=["length", "rank_occ"], ascending=[False, True]
        )

    # -------------------------------------------------------------------------
    # def internal__get_nlp_terms(self):
    #     self.nlp_terms = (
    #         DataFrame()
    #         .with_field("raw_nouns_and_phrases")
    #         .having_terms_ordered_by("OCC")
    #         .where_root_directory_is(self.params.root_directory)
    #         .where_database_is("main")
    #     ).run()
    #     self.nlp_terms["length"] = self.nlp_terms.index.str.split("_").str.len()
    #     self.nlp_terms = self.nlp_terms.sort_values(
    #         by=["length", "rank_occ"], ascending=[True, True]
    #     )

    # -------------------------------------------------------------------------
    def internal__mark_keywords(self):
        self.data_frame["is_keyword"] = False
        self.data_frame.loc[
            self.data_frame["key"].isin(self.keywords.index.to_list()), "is_keyword"
        ] = True

    # -------------------------------------------------------------------------
    def internal__compress_keywords(self):

        for keyword, _ in tqdm(
            self.keywords.iterrows(),
            total=self.keywords.shape[0],
            desc="      Compressing keywords ",
            disable=self.params.tqdm_disable,
            ncols=80,
        ):

            regex = keyword.replace("_", " ")
            regex = re.escape(regex)
            regex = r"\b" + regex + r"\b"

            candidates = self.data_frame.copy()
            candidates = candidates[candidates.is_keyword == False].copy()
            candidates = candidates[
                candidates["phrase"].str.contains(regex, regex=True)
            ]
            if len(candidates) == 0:
                continue
            self.data_frame.loc[candidates.index, "key"] = keyword
            self.data_frame.loc[candidates.index, "is_keyword"] = True

    # -------------------------------------------------------------------------
    def internal__compress_by_words(self):

        self.data_frame["phrase"] = self.data_frame["phrase"].str.split()
        self.data_frame["phrase"] = self.data_frame["phrase"].map(sorted)
        self.data_frame["phrase"] = self.data_frame["phrase"].str.join(" ")

        for keyword, _ in tqdm(
            self.keywords.iterrows(),
            total=self.keywords.shape[0],
            desc="         Compressing words ",
            disable=self.params.tqdm_disable,
        ):

            regex = keyword.replace("_", " ")
            regex = regex.split()
            regex = sorted(regex)
            regex = " ".join(regex)
            regex = re.escape(regex)
            regex = r"\b" + regex + r"\b"

            candidates = self.data_frame.copy()
            candidates = candidates[candidates.is_keyword == False].copy()
            candidates = candidates[
                candidates["phrase"].str.contains(regex, regex=True)
            ]
            if len(candidates) == 0:
                continue
            self.data_frame.loc[candidates.index, "key"] = keyword
            self.data_frame.loc[candidates.index, "is_keyword"] = True

    # -------------------------------------------------------------------------
    def internal__compress_keys(self):

        self.n_initial_keys = len(self.data_frame.key.drop_duplicates())
        self.data_frame["phrase"] = self.data_frame["key"].str.replace("_", " ")
        self.internal__compress_keywords()
        self.internal__compress_by_words()
        self.data_frame.pop("phrase")
        self.data_frame.pop("is_keyword")
        self.n_final_keys = len(self.data_frame.key.drop_duplicates())

    # -------------------------------------------------------------------------
    def internal__group_values_by_key(self):
        self.data_frame = self.data_frame.groupby("key", as_index=False).agg(
            {"value": lambda x: "; ".join(x)}
        )
        self.data_frame = self.data_frame.sort_values("key")
        self.data_frame = self.data_frame.reset_index(drop=True)

    # -------------------------------------------------------------------------
    def run(self):
        """:meta private:"""

        self.internal__build_user_thesaurus_path()
        self.internal__notify_process_start()
        self.internal__load_thesaurus_as_mapping()
        self.internal__transform_mapping_to_data_frame()
        self.internal__get_keywords()
        # self.internal__get_nlp_terms()
        self.internal__mark_keywords()
        self.internal__compress_keys()

        ## self.internal__group_values_by_key()
        self.internal__reduce_keys()
        self.internal__explode_and_group_values_by_key()
        self.internal__sort_data_frame_by_rows_and_key()
        self.internal__write_thesaurus_data_frame_to_disk()
        self.internal__notify_process_end()
