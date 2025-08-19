# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Cutoff Fuzzy Merging
===============================================================================


Example:
    >>> # Reset the thesaurus to initial state
    >>> from techminer2.thesaurus.user import InitializeThesaurus
    >>> InitializeThesaurus(
    ...     thesaurus_file="demo.the.txt",
    ...     field="raw_descriptors",
    ...     root_directory="examples/fintech/",
    ...     quiet=True,
    ... ).run()

    >>> from techminer2.thesaurus.user import ReduceKeys
    >>> (
    ...     ReduceKeys(use_colorama=False)
    ...     .with_thesaurus_file("demo.the.txt")
    ...     .where_root_directory_is("examples/fintech/")
    ...     .run()
    ... )

    >>> # Redirecting stderr to avoid messages during doctests
    >>> import sys
    >>> from io import StringIO
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Cutoff Fuzzy Merging
    >>> from techminer2.thesaurus.user import CutoffFuzzyMerging
    >>> (
    ...     CutoffFuzzyMerging(use_colorama=False, tqdm_disable=True)
    ...     .with_thesaurus_file("demo.the.txt")
    ...     .with_field("raw_descriptors")
    ...     .where_root_directory_is("examples/fintech/")
    ...     .having_cutoff_threshold(85)
    ...     .having_match_threshold(95)
    ...     .run()
    ... )

    >>> # Capture and print stderr output to test the code using doctest
    >>> output = sys.stderr.getvalue()
    >>> sys.stderr = original_stderr
    >>> print(output)
    Cutoff-Fuzzy Merging thesaurus keys...
      File : examples/fintech/data/thesaurus/demo.the.txt
      Keys reduced from 1569 to 1554
      Merging process completed successfully
    <BLANKLINE>
    <BLANKLINE>

"""


import sys

from colorama import Fore
from colorama import init
from techminer2._internals.mixins import ParamsMixin
from techminer2.thesaurus._internals import internal__print_thesaurus_header
from techminer2.thesaurus._internals import ThesaurusMixin
from tqdm import tqdm  # type: ignore
from fuzzywuzzy import fuzz  # type: ignore
from techminer2.package_data.text_processing import internal__load_text_processing_terms
from techminer2.thesaurus.user.general.reduce_keys import ReduceKeys
from techminer2.database._internals.io import (
    internal__load_filtered_records_from_database,
)
from techminer2.database.metrics.performance import DataFrame

tqdm.pandas()


class CutoffFuzzyMerging(
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

        sys.stderr.write(f"Cutoff-Fuzzy Merging thesaurus keys...\n")
        sys.stderr.write(f"  File : {file_path}\n")
        sys.stderr.flush()

    # -------------------------------------------------------------------------
    def internal__notify_process_end(self):

        sys.stderr.write(
            f"  Keys reduced from {self.n_initial_keys} to {self.n_final_keys}\n"
        )
        sys.stderr.write(f"  Merging process completed successfully\n\n")
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
    def internal__mark_keywords(self):
        self.data_frame["is_keyword"] = False
        self.data_frame.loc[
            self.data_frame["key"].isin(self.keywords.index.to_list()), "is_keyword"
        ] = True

    # -------------------------------------------------------------------------
    def internal__get_raw_occurrences(self):

        records = internal__load_filtered_records_from_database(params=self.params)
        records = records[[self.params.field]]
        records = records.dropna()
        records[self.params.field] = records[self.params.field].str.split("; ")
        records = records.explode(self.params.field)
        records[self.params.field] = records[self.params.field].str.strip()
        records["OCC"] = 1
        counts = records.groupby(self.params.field, as_index=True).agg({"OCC": "sum"})

        self.raw_key2occ = dict(zip(counts.index, counts.OCC))

    # -------------------------------------------------------------------------
    def internal__compute_key_occurrences(self):

        self.key_occurrences = self.data_frame.copy()

        self.key_occurrences["value"] = self.key_occurrences["value"].str.split("; ")
        self.key_occurrences = self.key_occurrences.explode("value")
        self.key_occurrences["value"] = self.key_occurrences["value"].str.strip()

        self.key_occurrences["OCC"] = self.key_occurrences.value.map(
            # lambda x: raw_key2occ.get(x, 1)
            lambda x: self.raw_key2occ[x]
        )
        self.key_occurrences["OCC"] = self.key_occurrences["OCC"].astype(int)
        self.key_occurrences = self.key_occurrences[["key", "OCC"]]
        self.key_occurrences = self.key_occurrences.groupby("key", as_index=False).agg(
            {"OCC": "sum"}
        )

        keys2occ = dict(zip(self.key_occurrences.key, self.key_occurrences.OCC))

        self.data_frame["OCC"] = self.data_frame.key.map(keys2occ)

    # -------------------------------------------------------------------------
    def internal__sort_by_keylength(self):

        self.data_frame["key_length"] = self.data_frame["key"].str.len()

        self.data_frame = self.data_frame.sort_values(
            by=["key_length", "OCC"], ascending=[True, False]
        )

    # -------------------------------------------------------------------------
    def internal__compute_fuzzy_match(self, string1, string2):

        # obtain the shorten and lengthen strings
        string1 = string1.split(" ")
        string2 = string2.split(" ")

        if len(string1) > len(string2):
            shorten_string = string2
            lengthen_string = string1
        else:
            shorten_string = string1
            lengthen_string = string2

        scores_per_word = []
        for base_word in shorten_string:
            best_match = 0
            for candidate_word in lengthen_string:
                score = fuzz.ratio(base_word, candidate_word)
                if score > best_match:
                    best_match = score
            scores_per_word.append(best_match)

        match = all(score >= self.params.match_threshold for score in scores_per_word)

        return match

    # -------------------------------------------------------------------------
    def internal__compute_mergings(self):

        self.data_frame["selected"] = False
        self.data_frame["cutoff"] = 0.0
        self.data_frame["fuzzy"] = 0.0
        self.data_frame = self.data_frame.reset_index(drop=True)
        self.data_frame["key"] = self.data_frame["key"].str.lower()
        self.data_frame["key"] = self.data_frame["key"].str.replace("_", " ")
        self.data_frame["key_length"] = self.data_frame["key"].str.len()

        keys = self.data_frame["key"].tolist()
        mergings = {}

        for index, key in tqdm(
            enumerate(keys),
            total=len(keys),
            desc=f"  Progress",
            ncols=80,
            disable=self.params.tqdm_disable,
        ):

            if self.data_frame.loc[index, "selected"] is False:
                continue

            if self.data_frame.loc[index, "selected"] is True:
                continue

            # Select the rows not evaluated
            df = self.data_frame[self.data_frame.index > index]

            # Only evaluate noun phrases
            df = df[df.is_keyword == False]

            # Preselect
            diff_in_length = (
                int((1 - self.params.cutoff_threshold / 100.0) * len(key)) + 1
            )
            min_key_length = max(len(key) - diff_in_length, 1)
            max_key_length = len(key) + diff_in_length
            df = df[df.key_length <= max_key_length]
            df = df[df.key_length >= min_key_length]

            # Apply the cutoff rule
            df["cutoff"] = df["key"].apply(lambda x: fuzz.ratio(key, x))
            df = df[df["cutoff"] >= self.params.cutoff_threshold]

            if df.empty:
                continue

            df["fuzzy"] = df["key"].apply(
                lambda x: self.internal__compute_fuzzy_match(key, x)
            )

            df = df[df["fuzzy"] == True]

            if df.empty:
                continue

            key = key.replace(" ", "_").upper()
            df["key"] = df["key"].str.replace(" ", "_").str.upper()

            self.data_frame.loc[df.index, "selected"] = True

            mergings[key] = df["key"].tolist()

        self.mergings = mergings

        # print(mergings)

        self.data_frame["key"] = self.data_frame["key"].str.upper()
        self.data_frame["key"] = self.data_frame["key"].str.replace(" ", "_")

    # -------------------------------------------------------------------------
    def internal__make_mergings(self):

        reversed_mergings = {v: k for k, vs in self.mergings.items() for v in vs}
        self.data_frame["key"] = self.data_frame["key"].map(
            lambda x: reversed_mergings.get(x, x)
        )

    # -------------------------------------------------------------------------
    def run(self):
        """:meta private:"""

        self.internal__build_user_thesaurus_path()
        self.internal__notify_process_start()
        self.internal__load_thesaurus_as_mapping()
        self.internal__transform_mapping_to_data_frame()
        self.internal__get_keywords()
        self.internal__mark_keywords()
        #
        self.n_initial_keys = self.data_frame.shape[0]
        #
        self.internal__get_raw_occurrences()
        self.internal__compute_key_occurrences()
        self.internal__sort_by_keylength()
        #
        self.internal__compute_mergings()
        self.internal__make_mergings()
        self.internal__explode_and_group_values_by_key()
        self.internal__sort_data_frame_by_rows_and_key()
        #
        self.n_final_keys = self.data_frame.shape[0]
        #
        self.internal__write_thesaurus_data_frame_to_disk()
        self.internal__notify_process_end()
