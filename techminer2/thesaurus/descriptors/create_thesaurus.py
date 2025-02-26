# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Create Thesaurus
===============================================================================


>>> from techminer2.thesaurus.descriptors import CreateThesaurus
>>> (
...     CreateThesaurus()  
...     #
...     # DATABASE:
...     .where_root_directory_is("example/")
...     #
...     .build()
... )
<BLANKLINE>
Thesaurus creation completed successfully for file: ...urus/descriptors.the.txt

"""

import re
import sys

import pandas as pd  # type: ignore
from textblob import Word  # type: ignore
from tqdm import tqdm  # type: ignore

from ..._internals.mixins import ParamsMixin
from ...database._internals.io import internal__load_filtered_database
from ...package_data.text_processing import internal__load_text_processing_terms
from .._internals import (
    internal__apply_porter_stemmer,
    internal__generate_system_thesaurus_file_path,
    internal__generate_user_thesaurus_file_path,
    internal__load_cleanup_thesaurus_as_mapping,
    internal__load_thesaurus_as_mapping,
    internal__print_thesaurus_header,
)
from .._internals.load_reversed_thesaurus_as_mapping import (
    internal__load_reversed_thesaurus_as_mapping,
)
from .._internals.load_thesaurus_as_mapping import internal__load_thesaurus_as_mapping

THESAURUS_FILE = "thesaurus/descriptors.the.txt"
ABBREVIATIONS_FILE = "thesaurus/abbreviations.the.txt"

tqdm.pandas()
LENGTH = 43


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
    def step_03_load_records(self):
        # self.records = internal__load_records(params=self.params)
        self.records = internal__load_filtered_database(params=self.params)

    # -------------------------------------------------------------------------
    def step_04_create_data_frame(self):
        #
        sys.stderr.write("\n  Loading records")
        sys.stderr.flush()
        #
        values = self.records[self.params.field].dropna()
        values = values.str.split("; ")
        values = values.explode()
        values = values.str.strip()
        values = values.drop_duplicates()
        #
        keys = values.str.lower()
        keys = keys.str.replace("-", " ")
        keys = keys.str.replace("_", " ")
        keys = keys.str.replace('"', " ")
        keys = keys.str.replace("'", " ")
        keys = [k.strip() for k in keys]
        #
        counts = values.value_counts()
        mapping = dict(zip(counts.index.tolist(), counts.values.tolist()))
        #
        data_frame = pd.DataFrame(
            {
                "key": keys,
                "value": values,
                "occ": [mapping[k] for k in values],
            }
        )
        #
        self.data_frame = data_frame

    # -------------------------------------------------------------------------
    def step_05_removing_surrounding_parentheses(self):
        #
        def remove_parentheses(text):
            if len(text) > 0 and text[0] == "(" and text[-1] == ")":
                return text[1:-1]
            return text

        tqdm.pandas(desc="Removing surrounding parentheses".rjust(LENGTH))
        self.data_frame["key"] = self.data_frame.key.progress_apply(remove_parentheses)
        tqdm.pandas(desc=None)

    # -------------------------------------------------------------------------
    def step_06_invert_abbreviation_definitions(self):
        #
        # Case:
        # "REGTECH (REGULATORY_TECHNOLOGY)" -> "REGULATORY_TECHNOLOGY (REGTECH)"
        #
        def invert_definitions(text):
            start_idx = text.find("(")
            end_idx = text.find(")")
            if start_idx == -1 or end_idx == -1:
                text_to_remove = text[start_idx + 1 : end_idx].strip()
                meaning = text[:start_idx].strip()
                if (
                    len(meaning) < len(text_to_remove)
                    and len(text_to_remove.strip()) > 1
                ):
                    return f"{text_to_remove} ({meaning})"
            return text

        tqdm.pandas(desc="Inverting abbreviation definitions".rjust(LENGTH))
        self.data_frame["key"] = self.data_frame.key.progress_apply(invert_definitions)
        tqdm.pandas(desc=None)

    # -------------------------------------------------------------------------
    def step_07_remove_text_inside_brackets(self):
        #
        # Tansforms:
        #
        # "REGULATORY_TECHNOLOGY [REGTECH]" -> "REGULATORY_TECHNOLOGY"
        #
        def remove(text):
            start_idx = text.find("[")
            end_idx = text.find("]")
            if start_idx != -1 and end_idx != -1:
                text_to_remove = text[start_idx : end_idx + 1]
                text = text.replace(text_to_remove, "").strip()
                text = text.replace("  ", " ").replace("  ", " ")
            return text

        tqdm.pandas(desc="Removing text inside brackets".rjust(LENGTH))
        self.data_frame["key"] = self.data_frame.key.progress_apply(remove)
        tqdm.pandas(desc=None)

    # -------------------------------------------------------------------------
    def step_08_remove_text_inside_parentheses(self):
        #
        # Case:
        # "REGULATORY_TECHNOLOGY (REGTECH)" -> "REGULATORY_TECHNOLOGY"
        #
        #
        def remove(text):
            start_idx = text.find("(")
            end_idx = text.find(")")
            if start_idx != -1 and end_idx != -1:
                text_to_remove = text[start_idx : end_idx + 1]
                text = text.replace(text_to_remove, "").strip()
                text = text.replace("  ", " ").replace("  ", " ")
            return text

        for i in range(3):
            tqdm.pandas(desc=f"Removing text inside parentheses ({i+1})".rjust(LENGTH))
            self.data_frame["key"] = self.data_frame.key.progress_apply(remove)
        tqdm.pandas(desc=None)
        self.data_frame["key"] = self.data_frame.key.str.replace("(", "")
        self.data_frame["key"] = self.data_frame.key.str.replace(")", "")
        self.data_frame["key"] = self.data_frame.key.str.replace("[", "")
        self.data_frame["key"] = self.data_frame.key.str.replace("]", "")
        self.data_frame["key"] = self.data_frame.key.str.replace("   ", " ")
        self.data_frame["key"] = self.data_frame.key.str.replace("  ", " ")

    # -------------------------------------------------------------------------
    def step_09_remove_initial_particles(self):
        #
        # Transforms:
        #
        #   "and regtech" -> "regtech"
        #   "the regtech" -> "regtech"
        #   "a regtech" -> "regtech"
        #   "an regtech" -> "regtech"
        #

        PARTICLES = [
            "and ",
            "the ",
            "a ",
            "an ",
            "all ",
            "any ",
            "both ",
        ]

        pattern = r"^(" + "|".join(PARTICLES) + r")"
        self.data_frame["key"] = self.data_frame.key.str.replace(
            pattern, "", regex=True
        )

    # -------------------------------------------------------------------------
    def step_10_transform_hypened_words(self):
        #
        # Transforms:
        #   "WIFI" -> "WI_FI"
        #   "COEVOLUTION" -> "CO_EVOLUTION"
        #

        # the file contains words in uppercase and '-' replaced by '_'.
        hypened_words = internal__load_text_processing_terms("hypened_words.txt")
        hypened_words = [word.lower() for word in hypened_words]
        hypened_words = [word.replace("_", " ") for word in hypened_words]

        # create a list of (pattern, replacement) tuples
        patterns = [
            (re.compile(r"\b" + word.replace(" ", "") + r"\b"), word)
            for word in hypened_words
        ]

        def replace_patterns(text):
            for pattern, replacement in patterns:
                text = pattern.sub(replacement, text)
            return text

        tqdm.pandas(desc="Processing haypened words".rjust(LENGTH))
        self.data_frame["key"] = self.data_frame.key.progress_apply(replace_patterns)
        tqdm.pandas(desc=None)

    # -------------------------------------------------------------------------
    def step_11_correct_bad_hypened_words(self):
        #
        # Transforms:
        #   "FIN_TECH" -> "FINTECH"
        #
        hypened_words = internal__load_text_processing_terms("non_hypened_words.txt")
        hypened_words = [word.lower() for word in hypened_words]
        hypened_words = [word.replace("_", " ") for word in hypened_words]

        patterns = [
            (re.compile(r"\b" + word + r"\b"), word.replace(" ", ""))
            for word in hypened_words
        ]

        def replace_patterns(text):
            for pattern, replacement in patterns:
                text = pattern.sub(replacement, text)
            return text

        tqdm.pandas(desc="Fixing bad haypened words".rjust(LENGTH))
        self.data_frame["key"] = self.data_frame.key.progress_apply(replace_patterns)
        tqdm.pandas(desc=None)

    # -------------------------------------------------------------------------
    def step_12_remove_common_starting_words(self):

        words = internal__load_text_processing_terms("common_starting_words.txt")
        words = [word.lower().replace("_", " ") for word in words]
        patterns = [re.compile(r"^" + word + " ") for word in words]

        def replace_patterns(text):
            for pattern in patterns:
                text = pattern.sub("", text)
            return text

        PARTICLES = [
            "and ",
            "the ",
            "a ",
            "an ",
            "all ",
            "any ",
            "both ",
        ]

        for i in range(3):
            tqdm.pandas(desc=f"Removing common starting words ({i+1})".rjust(LENGTH))
            self.data_frame["key"] = self.data_frame.key.progress_apply(
                replace_patterns
            )
            pattern = r"^(" + "|".join(PARTICLES) + r")"
            self.data_frame["key"] = self.data_frame.key.str.replace(
                pattern, "", regex=True
            )
        tqdm.pandas(desc=None)

    # -------------------------------------------------------------------------
    def step_13_remove_common_ending_words(self):

        words = internal__load_text_processing_terms("common_ending_words.txt")
        words = [word.lower().replace("_", " ") for word in words]
        patterns = [re.compile(r" " + word + "$") for word in words]

        def replace_patterns(text):
            for pattern in patterns:
                text = pattern.sub("", text)
            return text

        for i in range(3):
            tqdm.pandas(desc=f"Removing common ending words ({i+1})".rjust(LENGTH))
            self.data_frame["key"] = self.data_frame.key.progress_apply(
                replace_patterns
            )
        tqdm.pandas(desc=None)

    # -------------------------------------------------------------------------
    def step_14_british_to_american_spelling(self):

        file_path = internal__generate_system_thesaurus_file_path(
            "language/british2american.the.txt"
        )
        br2am = internal__load_thesaurus_as_mapping(file_path)
        br2am = {k: v[0] for k, v in br2am.items()}

        self.data_frame["key"] = self.data_frame.key.str.split(" ")
        self.data_frame["key"] = self.data_frame.key.map(
            lambda x: [z.strip() for z in x]
        )
        tqdm.pandas(desc="Transforming British to American spelling".rjust(LENGTH))
        self.data_frame["key"] = self.data_frame.key.progress_apply(
            lambda x: [br2am.get(z, z) for z in x]
        )
        tqdm.pandas(desc=None)
        self.data_frame["key"] = self.data_frame["key"].str.join(" ")

    # -------------------------------------------------------------------------
    def step_15_prepare_fingerprint_column(self):
        #
        self.data_frame["fingerprint"] = self.data_frame["key"].copy()
        #
        tqdm.pandas(desc="Stemming fingerprint terms".rjust(LENGTH))

        self.data_frame["fingerprint"] = self.data_frame["fingerprint"].progress_apply(
            lambda x: " ".join(
                sorted(internal__apply_porter_stemmer(w) for w in x.split(" "))
            )
        )

        # self.data_frame["fingerprint"] = self.data_frame["fingerprint"].progress_apply(
        #     lambda x: " ".join(sorted(Word(w).singularize() for w in x.split(" ")))
        # )

        tqdm.pandas(desc=None)

    # -------------------------------------------------------------------------
    def step_16_prepare_key_column(self):
        self.data_frame["key"] = (
            self.data_frame["key"].str.upper().str.replace(" ", "_")
        )

    # -------------------------------------------------------------------------
    def step_17_generate_fingerprint2value_mapping(self):
        self.data_frame = self.data_frame.sort_values(
            by=["fingerprint", "occ", "key"], ascending=[True, False, True]
        )
        data_frame = self.data_frame.drop_duplicates(subset=["fingerprint"])
        mapping = data_frame.set_index("fingerprint")["key"].to_dict()
        self.mapping = mapping

    # -------------------------------------------------------------------------
    def step_18_apply_mapping(self):
        tqdm.pandas(desc="Generating new thesaurus keys".rjust(LENGTH))
        self.data_frame["key"] = self.data_frame.fingerprint.progress_apply(
            lambda x: self.mapping.get(x, x)
        )
        tqdm.pandas(desc=None)
        self.data_frame = self.data_frame[["key", "value"]]

    # -------------------------------------------------------------------------
    def step_19_apply_system_cleanup_thesaurus_files(self):

        mapping = internal__load_cleanup_thesaurus_as_mapping()
        # mapping = {
        #     k.lower().replace("_", " "): v.lower().replace("_", " ")
        #     for k, v in mapping.items()
        # }
        tqdm.pandas(desc="Applying system cleanup thesaurus files".rjust(LENGTH))
        self.data_frame["key"] = self.data_frame.key.progress_apply(
            lambda x: mapping.get(x, x)
        )
        tqdm.pandas(desc=None)

    # -------------------------------------------------------------------------
    def step_20_write_thesaurus_to_disk(self):
        self.data_frame = self.data_frame.groupby("key").agg({"value": list})
        self.data_frame["value"] = self.data_frame.value.apply(lambda x: sorted(set(x)))
        with open(self.file_path, "w", encoding="utf-8") as file:
            for _, row in self.data_frame.iterrows():
                file.write(row.name + "\n")
                for value in row["value"]:
                    file.write(f"    {value}\n")

    # -------------------------------------------------------------------------
    def step_21_print_info_tail(self):
        truncated_file_path = str(self.file_path)
        if len(truncated_file_path) > 28:
            truncated_file_path = "..." + truncated_file_path[-24:]
        sys.stdout.write(
            f"\nThesaurus creation completed successfully for file: {truncated_file_path}"
        )
        sys.stdout.flush()
        internal__print_thesaurus_header(thesaurus_path=self.file_path)

    # -------------------------------------------------------------------------
    def build(self):
        """:meta private:"""

        self.params.update(
            thesaurus_file="descriptors.the.txt",
            field="raw_descriptors",
        )

        self.step_01_get_thesaurus_file_path()
        self.step_02_print_info_header()
        self.step_03_load_records()
        self.step_04_create_data_frame()
        self.step_05_removing_surrounding_parentheses()
        self.step_06_invert_abbreviation_definitions()
        self.step_07_remove_text_inside_brackets()
        self.step_08_remove_text_inside_parentheses()
        self.step_09_remove_initial_particles()
        self.step_10_transform_hypened_words()
        self.step_11_correct_bad_hypened_words()
        self.step_12_remove_common_starting_words()
        self.step_13_remove_common_ending_words()
        self.step_14_british_to_american_spelling()
        self.step_15_prepare_fingerprint_column()
        self.step_16_prepare_key_column()
        self.step_17_generate_fingerprint2value_mapping()
        self.step_18_apply_mapping()
        self.step_19_apply_system_cleanup_thesaurus_files()
        self.step_20_write_thesaurus_to_disk()
        self.step_21_print_info_tail()


# def _load_abbreviations_th_as_dict(abbreviations_file):
#     if not os.path.isfile(abbreviations_file):
#         raise FileNotFoundError(f"The file {abbreviations_file} does not exist.")
#     abbreviations_dict = internal__load_thesaurus_as_mapping(abbreviations_file)
#     return abbreviations_dict


# def _apply_abbreviations_thesaurus(data_frame, abbreviations_dict):

#     for abbr, values in tqdm(
#         abbreviations_dict.items(), desc="Remmplacing abbreviations"
#     ):
#         #
#         # Replace abbreviations in descriptor keys
#         for value in values:
#             data_frame["key"] = data_frame["key"].str.replace(
#                 re.compile("^" + abbr + "$"), value, regex=True
#             )
#             data_frame["key"] = data_frame["key"].str.replace(
#                 re.compile("^" + abbr + "_"), value + "_", regex=True
#             )
#             data_frame["key"] = data_frame["key"].str.replace(
#                 re.compile("^" + abbr + " "), value + " ", regex=True
#             )
#             data_frame["key"] = data_frame["key"].str.replace(
#                 re.compile("_" + abbr + "$"), "_" + value, regex=True
#             )
#             data_frame["key"] = data_frame["key"].str.replace(
#                 re.compile(" " + abbr + "$"), " " + value, regex=True
#             )
#             data_frame["key"] = data_frame["key"].str.replace(
#                 re.compile("_" + abbr + "_"), "_" + value + "_", regex=True
#             )
#             data_frame["key"] = data_frame["key"].str.replace(
#                 re.compile(" " + abbr + "_"), " " + value + "_", regex=True
#             )
#             data_frame["key"] = data_frame["key"].str.replace(
#                 re.compile("_" + abbr + " "), "_" + value + " ", regex=True
#             )
#             data_frame["key"] = data_frame["key"].str.replace(
#                 re.compile(" " + abbr + " "), " " + value + " ", regex=True
#             )

#     # -------------------------------------------------------------------------------------------
#     # data_frame = data_frame.sort_values(by="key")
#     # data_frame = data_frame.groupby("key", as_index=False).agg({"value": list})
#     return data_frame


#
#
# # MAIN CODE:
# #
# #
# def reset_thesaurus(
#     #
#     # DATABASE PARAMS:
#     root_dir="./",
# ):
#     """:meta private:"""

#     start_time = time.time()

#     # Thesaurus paths
#     th_descriptors_file = os.path.join(root_dir, THESAURUS_FILE)
#     th_abbreviations_file = os.path.join(root_dir, ABBREVIATIONS_FILE)

#     abbreviations_th = _load_abbreviations_th_as_dict(th_abbreviations_file)

# loads the dataframe for nornal processing
# data_frame = _create_data_frame_from_thesaurus(th_descriptors_file)

# Replace abbreviations directly in the thesaurus file
# print(".  1/10 . Reemplacing abbreviations.")
# data_frame = _apply_abbreviations_thesaurus(data_frame, abbreviations_th)

# print(".  2/10 . Inverting terms in parenthesis.")
# data_frame = _check_terms_in_parenthesis(data_frame)
# data_frame = _invert_terms_in_parenthesis(data_frame)

# print(".  3/10 . Removing text in brackets.")
# data_frame = _remove_brackets(data_frame)

# print(".  4/10 . Removing text in parenthesis.")
# data_frame = _remove_parenthesis(data_frame)
# data_frame = _remove_initial_articles(data_frame)

# print(".  5/10 . Transforming hypened words.")
# data_frame = _transform_hypened_words(data_frame)
# data_frame = _transform_non_hypened_words(data_frame)
# data_frame = _apply_abbreviations_thesaurus(data_frame, abbreviations_th)

# print(".  6/10 . Removing common starting words.")
# data_frame = _remove_common_starting_words(data_frame)

# print(".  7/10 . Removing common ending words.")
# data_frame = _remove_common_ending_words(data_frame)

# print(".  8/10 . Applying the default.the.txt thesaurus.")
# data_frame = _apply_default_thesaurus_files(data_frame)

# print(".  9/10 . Transforming british to american spelling.")
# data_frame = _british_to_american_spelling(data_frame)

# print(". 10/10 . Applying Porter stemmer.")
# data_frame["fingerprint"] = data_frame["key"].copy()

# data_frame = _apply_porter_stemmer(data_frame)
# data_frame = _compute_terms_by_key(data_frame)
# data_frame = _replace_fingerprint(data_frame)

# _save_thesaurus(data_frame, th_descriptors_file)

# #
# new_th_file = os.path.join(root_dir, "thesaurus/_descriptors_.the.txt")
# with open(th_descriptors_file, "r", encoding="utf-8") as file:
#     with open(new_th_file, "w", encoding="utf-8") as new_file:
#         new_file.write(file.read())
# #

# end_time = time.time()
# total_time = end_time - start_time
# hours, remainder = divmod(total_time, 3600)
# minutes, seconds = divmod(remainder, 60)

# print(f"--INFO-- The thesaurus {th_descriptors_file} has been reseted.")
# print(
#     f"--INFO-- Total time consumed by the execution: {int(hours):02}:{int(minutes):02}:{seconds:04.1f}"
# )
