# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Reset Thesaurus to Initial State
===============================================================================



## >>> from techminer2.thesaurus.user import ResetThesaurusToInitialState
## >>> (
## ...     ResetThesaurusToInitialState()  
## ...     # 
## ...     # THESAURUS:
## ...     .with_thesaurus_file("descriptors.the.txt")
## ...     #
## ...     # DATABASE:
## ...     .where_directory_is("example/")
## ...     #
## ...     .build()
## ... )


"""
import glob
import os
import re
import time

import pandas as pd  # type: ignore
import pkg_resources  # type: ignore
from tqdm import tqdm  # type: ignore

from .._internals.load_reversed_thesaurus_as_mapping import (
    internal__load_reversed_thesaurus_as_mapping,
)
from .._internals.load_thesaurus_as_mapping import internal__load_thesaurus_as_mapping
from .cleanup_thesaurus import (
    _apply_porter_stemmer,
    _compute_terms_by_key,
    _replace_fingerprint,
    _save_thesaurus,
)

THESAURUS_FILE = "thesaurus/descriptors.the.txt"
ABBREVIATIONS_FILE = "thesaurus/abbreviations.the.txt"

tqdm.pandas()


def _create_data_frame_from_thesaurus(th_file):
    #
    # Creates a dataframe with the thesaurus with the following columns:
    #
    # - key: current key in the original thesaurus. This key is transformed into the fingerprint.
    # - fingerprint: new key for the cleaned thesaurus
    # - text: raw descriptor text
    #
    with open(th_file, "r", encoding="utf-8") as file:
        terms = [line.strip() for line in file if line.startswith(" ")]

    data = pd.DataFrame(
        {
            "key": terms,
            "text": terms,
        }
    )

    return data


def _load_abbreviations_th_as_dict(abbreviations_file):
    if not os.path.isfile(abbreviations_file):
        raise FileNotFoundError(f"The file {abbreviations_file} does not exist.")
    abbreviations_dict = internal__load_thesaurus_as_mapping(abbreviations_file)
    return abbreviations_dict


def _apply_abbreviations_thesaurus(data_frame, abbreviations_dict):

    for abbr, values in tqdm(
        abbreviations_dict.items(), desc="Remmplacing abbreviations"
    ):
        #
        # Replace abbreviations in descriptor keys
        for value in values:
            data_frame["key"] = data_frame["key"].str.replace(
                re.compile("^" + abbr + "$"), value, regex=True
            )
            data_frame["key"] = data_frame["key"].str.replace(
                re.compile("^" + abbr + "_"), value + "_", regex=True
            )
            data_frame["key"] = data_frame["key"].str.replace(
                re.compile("^" + abbr + " "), value + " ", regex=True
            )
            data_frame["key"] = data_frame["key"].str.replace(
                re.compile("_" + abbr + "$"), "_" + value, regex=True
            )
            data_frame["key"] = data_frame["key"].str.replace(
                re.compile(" " + abbr + "$"), " " + value, regex=True
            )
            data_frame["key"] = data_frame["key"].str.replace(
                re.compile("_" + abbr + "_"), "_" + value + "_", regex=True
            )
            data_frame["key"] = data_frame["key"].str.replace(
                re.compile(" " + abbr + "_"), " " + value + "_", regex=True
            )
            data_frame["key"] = data_frame["key"].str.replace(
                re.compile("_" + abbr + " "), "_" + value + " ", regex=True
            )
            data_frame["key"] = data_frame["key"].str.replace(
                re.compile(" " + abbr + " "), " " + value + " ", regex=True
            )

    # -------------------------------------------------------------------------------------------
    # data_frame = data_frame.sort_values(by="key")
    # data_frame = data_frame.groupby("key", as_index=False).agg({"value": list})
    return data_frame


def _check_terms_in_parenthesis(data_frame):
    #
    # Transforms:
    #
    # "REGTECH (REGULATORY_TECHNOLOGY)" -> "REGULATORY_TECHNOLOGY (REGTECH)"
    #
    def check_parenthesis_in_text(text):

        if len(text) > 0 and text[0] == "(" and text[-1] == ")":
            return text[1:-1]

        return text

    data_frame["key"] = data_frame["key"].progress_apply(check_parenthesis_in_text)

    return data_frame


def _invert_terms_in_parenthesis(data_frame):
    #
    # Transforms:
    #
    # "REGTECH (REGULATORY_TECHNOLOGY)" -> "REGULATORY_TECHNOLOGY (REGTECH)"
    #
    def invert_parenthesis_in_text(text):

        start_idx = text.find("(")
        end_idx = text.find(")")

        if start_idx == -1 or end_idx == -1:

            text_to_remove = text[start_idx + 1 : end_idx].strip()
            meaning = text[:start_idx].strip()

            if len(meaning) < len(text_to_remove) and len(text_to_remove.strip()) > 1:
                return f"{text_to_remove} ({meaning})"

        return text

    data_frame["key"] = data_frame["key"].progress_apply(invert_parenthesis_in_text)

    return data_frame


def _remove_brackets(data_frame):
    #
    # Tansforms:
    #
    # "REGULATORY_TECHNOLOGY [REGTECH]" -> "REGULATORY_TECHNOLOGY"
    #
    def remove_brackets_from_text(text):

        start_idx = text.find("[")
        end_idx = text.find("]")

        if start_idx != -1 and end_idx != -1:
            text_to_remove = text[start_idx : end_idx + 1]
            text = text.replace(text_to_remove, "").strip()
            text = " ".join(text.split())

        return text

    data_frame["key"] = data_frame["key"].progress_apply(remove_brackets_from_text)

    return data_frame


def _remove_parenthesis(data_frame):
    #
    # Tansforms:
    #
    # "REGULATORY_TECHNOLOGY (REGTECH)" -> "REGULATORY_TECHNOLOGY"
    #
    def remove_parenthesis_from_text(text):

        if "(" in text and ")" in text:

            start_idx = text.find("(")
            end_idx = text.find(")")
            text_to_remove = text[start_idx : end_idx + 1]

            text = text.replace(text_to_remove, "").strip()

            text = " ".join(text.split())

        return text

    data_frame["key"] = data_frame["key"].progress_apply(remove_parenthesis_from_text)
    data_frame["key"] = data_frame["key"].progress_apply(remove_parenthesis_from_text)
    return data_frame


def _remove_initial_articles(data_frame):
    #
    # Transforms:
    #
    #   "AND_REGTECH" -> "REGTECH"
    #   "THE_REGTECH" -> "REGTECH"
    #   "A_REGTECH" -> "REGTECH"
    #   "AN_REGTECH" -> "REGTECH"
    #
    ARTICLES = [
        "AND_",
        "THE_",
        "A_",
        "AN_",
    ]

    articles_pattern = r"^(" + "|".join(ARTICLES) + r")_"
    data_frame["key"] = data_frame["key"].str.replace(articles_pattern, "", regex=True)
    return data_frame


def _transform_hypened_words(data_frame):
    #
    # Transforms:
    #
    #   "WI_FI" -> "WIFI"
    #   "CO_EVOLUTION" -> "COEVOLUTION"
    #
    def load_words():
        file_path = pkg_resources.resource_filename(
            "techminer2",
            "thesaurus/_data/hypened_words.txt",
        )
        with open(file_path, "r", encoding="utf-8") as file:
            return [line.strip() for line in file.readlines()]

    regex = load_words()

    data_frame["key"] = data_frame["key"].str.replace("_", " ", regex=False)

    patterns = [
        (re.compile(r"\b" + word.replace("_", "") + r"\b"), word.replace("_", " "))
        for word in regex
    ]

    def replace_patterns(text):
        for pattern, replacement in patterns:
            text = pattern.sub(replacement, text)
        return text

    data_frame["key"] = data_frame["key"].progress_apply(replace_patterns)

    data_frame["key"] = data_frame["key"].str.replace(" ", "_", regex=False)

    return data_frame


def _transform_non_hypened_words(data_frame):
    #
    # Transforms:
    #
    #   "FIN_TECH" -> "FINTECH"
    #
    def load_words():
        #
        file_path = pkg_resources.resource_filename(
            "techminer2",
            "thesaurus/_data/non_hypened_words.txt",
        )
        with open(file_path, "r", encoding="utf-8") as file:
            return [line.strip() for line in file.readlines()]

    data_frame["key"] = data_frame["key"].str.replace("_", " ", regex=False)

    patterns = load_words()
    patterns = [
        (re.compile(r"\b" + word.replace("_", " ") + r"\b"), word.replace("_", ""))
        for word in patterns
    ]

    def replace_patterns(text):
        for pattern, replacement in patterns:
            text = pattern.sub(replacement, text)
        return text

    data_frame["key"] = data_frame["key"].progress_apply(replace_patterns)

    data_frame["key"] = data_frame["key"].str.replace(" ", "_", regex=False)

    return data_frame


def _remove_common_starting_words(data_frame):
    #
    # Remove common starting words.
    #
    def load_words():
        #
        file_path = pkg_resources.resource_filename(
            "techminer2",
            "thesaurus/_data/common_starting_words.txt",
        )
        with open(file_path, "r", encoding="utf-8") as file:
            return [line.strip() for line in file.readlines()]

    words = load_words()
    patterns = [re.compile(r"^" + word + "_") for word in words]

    def replace_patterns(text):
        for pattern in patterns:
            text = pattern.sub("", text)
        return text

    data_frame["key"] = data_frame["key"].progress_apply(replace_patterns)
    data_frame["key"] = data_frame["key"].progress_apply(replace_patterns)
    data_frame["key"] = data_frame["key"].progress_apply(replace_patterns)

    return data_frame


def _remove_common_ending_words(data_frame):
    #
    # Remove common ending words.
    #
    def load_words():
        #
        file_path = pkg_resources.resource_filename(
            "techminer2",
            "thesaurus/_data/common_ending_words.txt",
        )
        with open(file_path, "r", encoding="utf-8") as file:
            return [line.strip() for line in file.readlines()]

    words = load_words()
    patterns = [re.compile(r"_" + word + "$") for word in words]

    def replace_patterns(text):
        for pattern in patterns:
            text = pattern.sub("", text)
        return text

    data_frame["key"] = data_frame["key"].progress_apply(replace_patterns)
    data_frame["key"] = data_frame["key"].progress_apply(replace_patterns)
    data_frame["key"] = data_frame["key"].progress_apply(replace_patterns)

    return data_frame


def _apply_default_thesaurus_files(data_frame):
    #
    # Apply _*.the.txt thesaurus files
    #
    file_paths = pkg_resources.resource_filename(
        "techminer2",
        "thesaurus/_data/_*.the.txt",
    )

    th_dict = {}
    for file_path in glob.glob(file_paths):
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"The file {file_path} does not exist.")
        th_dict = internal__load_reversed_thesaurus_as_mapping(file_path)
        data_frame["key"] = data_frame["key"].apply(lambda x: th_dict.get(x, x))

    return data_frame


def _british_to_american_spelling(data_frame):
    #
    # Loads the thesaurus
    def load_br2am_dict():
        #
        br2am = {}

        file_path = pkg_resources.resource_filename(
            "techminer2",
            "thesaurus/_data/british2american.the.txt",
        )
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file.readlines():
                if not line.startswith(" "):
                    british = line.strip().upper()
                else:
                    american = line.strip().upper()
                    br2am[british] = american

        return br2am

    br2am = load_br2am_dict()

    #
    # Replaces british by american spelling
    data_frame = data_frame.copy()

    #
    # Replaces "_" by " "
    data_frame["key"] = data_frame["key"].str.replace("_", " ", regex=False)
    data_frame["key"] = data_frame["key"].str.split(" ")
    data_frame["key"] = data_frame["key"].map(lambda x: [z.strip() for z in x])
    data_frame["key"] = data_frame["key"].map(lambda x: [br2am.get(z, z) for z in x])
    data_frame["key"] = data_frame["key"].str.join("_")

    return data_frame


#
#
# MAIN CODE:
#
#
def reset_thesaurus(
    #
    # DATABASE PARAMS:
    root_dir="./",
):
    """:meta private:"""

    start_time = time.time()

    # Thesaurus paths
    th_descriptors_file = os.path.join(root_dir, THESAURUS_FILE)
    th_abbreviations_file = os.path.join(root_dir, ABBREVIATIONS_FILE)

    abbreviations_th = _load_abbreviations_th_as_dict(th_abbreviations_file)

    # loads the dataframe for nornal processing
    data_frame = _create_data_frame_from_thesaurus(th_descriptors_file)

    # Replace abbreviations directly in the thesaurus file
    print(".  1/10 . Reemplacing abbreviations.")
    data_frame = _apply_abbreviations_thesaurus(data_frame, abbreviations_th)

    print(".  2/10 . Inverting terms in parenthesis.")
    data_frame = _check_terms_in_parenthesis(data_frame)
    data_frame = _invert_terms_in_parenthesis(data_frame)

    print(".  3/10 . Removing text in brackets.")
    data_frame = _remove_brackets(data_frame)

    print(".  4/10 . Removing text in parenthesis.")
    data_frame = _remove_parenthesis(data_frame)
    data_frame = _remove_initial_articles(data_frame)

    print(".  5/10 . Transforming hypened words.")
    data_frame = _transform_hypened_words(data_frame)
    data_frame = _transform_non_hypened_words(data_frame)
    data_frame = _apply_abbreviations_thesaurus(data_frame, abbreviations_th)

    print(".  6/10 . Removing common starting words.")
    data_frame = _remove_common_starting_words(data_frame)

    print(".  7/10 . Removing common ending words.")
    data_frame = _remove_common_ending_words(data_frame)

    print(".  8/10 . Applying the default.the.txt thesaurus.")
    data_frame = _apply_default_thesaurus_files(data_frame)

    print(".  9/10 . Transforming british to american spelling.")
    data_frame = _british_to_american_spelling(data_frame)

    print(". 10/10 . Applying Porter stemmer.")
    data_frame["fingerprint"] = data_frame["key"].copy()

    data_frame = _apply_porter_stemmer(data_frame)
    data_frame = _compute_terms_by_key(data_frame)
    data_frame = _replace_fingerprint(data_frame)

    _save_thesaurus(data_frame, th_descriptors_file)

    #
    new_th_file = os.path.join(root_dir, "thesaurus/_descriptors_.the.txt")
    with open(th_descriptors_file, "r", encoding="utf-8") as file:
        with open(new_th_file, "w", encoding="utf-8") as new_file:
            new_file.write(file.read())
    #

    end_time = time.time()
    total_time = end_time - start_time
    hours, remainder = divmod(total_time, 3600)
    minutes, seconds = divmod(remainder, 60)

    print(f"--INFO-- The thesaurus {th_descriptors_file} has been reseted.")
    print(
        f"--INFO-- Total time consumed by the execution: {int(hours):02}:{int(minutes):02}:{seconds:04.1f}"
    )
