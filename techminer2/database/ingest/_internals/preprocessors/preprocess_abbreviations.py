# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=import-outside-toplevel
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""Search for abbreviations in a thesaurus."""

import pathlib
import sys

import pandas as pd  # type: ignore
from textblob import TextBlob  # type: ignore

from ....._internals.log_message import internal__log_message
from .....thesaurus._internals import (
    internal__generate_system_thesaurus_file_path,
    internal__load_thesaurus_as_data_frame,
    internal__load_thesaurus_as_mapping,
)


# -------------------------------------------------------------------------
def step_01_load_descriptors_thesaurus(root_dir):
    file_path = pathlib.Path(root_dir) / "thesaurus" / "descriptors.the.txt"
    return internal__load_thesaurus_as_data_frame(file_path)


# -------------------------------------------------------------------------
def step_02_extracts_abbreviations_from_definitions(data_frame):

    data_frame = data_frame.copy()
    data_frame = data_frame.loc[data_frame.value.str.contains("(", regex=False), :]
    data_frame = data_frame.loc[data_frame.value.str.endswith(")"), :]
    data_frame = data_frame[["value"]].drop_duplicates()
    data_frame["value"] = data_frame["value"].str[:-1]
    data_frame["value"] = data_frame["value"].str.split(" (", regex=False)

    data_frame = data_frame[data_frame.value.map(len) == 2]
    data_frame["abbr"] = data_frame.value.map(lambda x: x[1])
    data_frame["value"] = data_frame.value.map(lambda x: x[0])
    data_frame = data_frame[data_frame.abbr.str.len() < data_frame.value.str.len()]

    return data_frame


# -------------------------------------------------------------------------
def step_03_add_abbreviations_from_abstracts(root_dir, data_frame):

    # load abstracts
    file_path = pathlib.Path(root_dir) / "databases/database.csv.zip"
    records = pd.read_csv(file_path, encoding="utf-8", compression="zip")
    records = records[["abstract"]].dropna()

    # extract phrases
    records["abstract"] = records.abstract.map(
        lambda x: [str(s) for s in TextBlob(x).sentences]
    )
    records = records.explode("abstract")
    records["abstract"] = records.abstract.str.strip()

    # select abstracts with parentheses
    records = records[records.abstract.str.contains("(", regex=False)]
    records = records[records.abstract.str.contains(")", regex=False)]

    # extract abbreviations
    records["abbr"] = records.abstract.str.extract(r"\(([^)]+)\)")
    records["abbr"] = records.abbr.str.upper().str.strip()
    records["value"] = records.abstract.str.replace(r"\([^)]+\)", "")
    records = records[["abbr", "value"]].drop_duplicates()

    # remove enumerations
    records = records[
        records.abbr.map(lambda x: x not in ["I", "II", "III", "IV", "V"])
    ]
    records = records[records.abbr.map(lambda x: x not in ["1", "2", "3", "4", "5"])]
    records = records[records.abbr.map(lambda x: "," not in x)]
    records = records[records.abbr.map(lambda x: " " not in x)]

    # remove abbreviations of length 1
    records = records[records.abbr.str.len() > 1]

    # remove enumerations already listed in the keywords
    existent_abbr = data_frame.abbr.drop_duplicates().tolist()
    records = records[records.abbr.map(lambda x: x not in existent_abbr)]

    # concat data frames
    data_frame = pd.concat([data_frame, records], ignore_index=True)
    return data_frame


# -------------------------------------------------------------------------
def step_04_remove_bad_abbreviations(data_frame):

    bad_abbreviations = [
        "CLASSIFICATION",
        "COMPUTER",
        "ECONOMICS",
        "ELECTRONICS",
        "ELECTRONIC",
        "IRRATIONAL",
        "ONLINE",
        "PERSONNEL",
    ]

    for abbr in bad_abbreviations:
        data_frame = data_frame[data_frame.abbr != abbr]

    return data_frame


# -------------------------------------------------------------------------
def step_05_add_knowns_abbreviations(mod_frame, raw_frame):

    file_path = internal__generate_system_thesaurus_file_path(
        "abbreviations/common_abbr.the.txt"
    )
    mapping = internal__load_thesaurus_as_mapping(file_path)

    for abbr, meaning in mapping.items():
        meaning = meaning[0]
        frame = raw_frame.copy()
        frame = frame[frame.value == abbr]
        if frame.shape[0] == 0:
            continue
        new_frame = pd.DataFrame({"value": [meaning], "abbr": [abbr]})
        mod_frame = pd.concat([mod_frame, new_frame], ignore_index=True)

    return mod_frame


# -------------------------------------------------------------------------
def step_06_prepare_data_frame(mod_frame):
    mod_frame = mod_frame[["abbr", "value"]].drop_duplicates()
    mod_frame = mod_frame.sort_values(["abbr", "value"]).reset_index(drop=True)
    mod_frame = mod_frame.groupby("abbr", as_index=False).agg({"value": list})
    mod_frame = mod_frame.reset_index(drop=True)
    return mod_frame


# -------------------------------------------------------------------------
def step_07_save_abbreviations_thesaurus(root_dir, mod_frame):

    file_path = pathlib.Path(root_dir) / "thesaurus/abbreviations.the.txt"

    with open(file_path, "w", encoding="utf-8") as f:
        for _, row in mod_frame.iterrows():
            f.write(row["abbr"] + "\n")
            for value in row["value"]:
                f.write("    " + value + "\n")


# -------------------------------------------------------------------------
def internal__preprocess_abbreviations(root_dir):

    sys.stdout.write("\nINFO  Extracting abbrevitions from descriptors and abstracts.")
    sys.stdout.flush()
    #
    raw_frame = step_01_load_descriptors_thesaurus(root_dir)
    mod_frame = step_02_extracts_abbreviations_from_definitions(raw_frame)
    mod_frame = step_03_add_abbreviations_from_abstracts(root_dir, mod_frame)
    mod_frame = step_04_remove_bad_abbreviations(mod_frame)
    mod_frame = step_05_add_knowns_abbreviations(mod_frame, raw_frame)
    mod_frame = step_06_prepare_data_frame(mod_frame)
    step_07_save_abbreviations_thesaurus(root_dir, mod_frame)
    #
    sys.stdout.write(f"\n      {len(mod_frame)} extracted abbreviations.")
    sys.stdout.flush()
