# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
import pathlib
import re

import pandas as pd

KEYWORDS_MAX_LENGTH = 60


def internal__clean_raw_keywords(
    source,
    dest,
    #
    # DATABASE PARAMS:
    root_dir="./",
):
    """:meta private:"""

    database_file = pathlib.Path(root_dir) / "databases/database.csv.zip"

    dataframe = pd.read_csv(
        database_file,
        encoding="utf-8",
        compression="zip",
        low_memory=False,
    )

    if source in dataframe.columns and not dataframe[source].dropna().empty:
        dataframe[dest] = clean_raw_keywords(dataframe[source])

    dataframe.to_csv(
        database_file,
        sep=",",
        encoding="utf-8",
        index=False,
        compression="zip",
    )


def remove_quotes_and_parentheses(string_list):
    """Remove quotes from text."""
    string_list = [
        z[1:-1] if z.startswith("'") and z.endswith("'") else z for z in string_list
    ]
    string_list = [
        z[1:-1] if z.startswith('"') and z.endswith('"') else z for z in string_list
    ]
    string_list = [
        z[1:-1] if z.startswith("(") and z.endswith(")") else z for z in string_list
    ]
    string_list = [
        z[1:-1] if z.startswith("[") and z.endswith("]") else z for z in string_list
    ]

    ## string_list = [z.replace('"', "**").replace('"', "**") for z in string_list]
    string_list = [z for z in string_list if not z.isdigit()]
    string_list = [z for z in string_list if z != ""]
    string_list = [z.strip() for z in string_list]

    return string_list


def clean_raw_keywords(text):
    """Clean and preprocess author keywords."""

    text = text.str.upper()

    # check bad separators
    text = text.map(
        lambda x: (
            x.replace(",", ";")
            if isinstance(x, str) and ";" not in x and len(x) > KEYWORDS_MAX_LENGTH
            else x
        )
    )

    # remove all non-ascii characters
    text = text.str.normalize("NFKD")
    text = text.str.encode("ascii", errors="ignore")
    text = text.str.decode("utf-8")

    # remove all html tags
    text = text.str.replace("<.*?>", "", regex=True)

    # remove apostrophes
    text = text.str.replace("ʿ", "'", regex=False)
    text = text.str.replace("’", "'", regex=False)
    text = text.str.replace("'", "'", regex=False)

    # remove word/word or word\word
    text = text.str.replace("/", "_", regex=False)
    text = text.str.replace("\\", "_", regex=False)

    # Remove single and double quotes
    text = text.str.split("; ")
    text = text.map(lambda x: [z.strip() for z in x], na_action="ignore")
    text = text.map(remove_quotes_and_parentheses, na_action="ignore")
    text = text.str.join("; ")

    # Replace possessives
    text = text.str.replace("'S ", " ", regex=False)
    text = text.str.replace("'", " ", regex=False)
    text = text.str.replace("^\s+", "", regex=True)

    # Replace '&' with 'AND'
    text = text.str.replace("&", " AND ", regex=False)

    # Remove terms at the beginning of the string
    text = text.str.split("; ")
    text = text.map(lambda x: [re.sub("^AND ", "", z) for z in x], na_action="ignore")
    text = text.map(lambda x: [re.sub("^AN ", "", z) for z in x], na_action="ignore")
    text = text.map(lambda x: [re.sub("^A ", "", z) for z in x], na_action="ignore")
    text = text.map(lambda x: [re.sub("^THE ", "", z) for z in x], na_action="ignore")
    text = text.str.join("; ")

    # Remove multiple spaces and unwanted characters
    text = text.str.replace(r"\s+", " ", regex=True)
    text = text.str.replace('"', "", regex=False)
    text = text.str.replace(".", "", regex=False)
    text = text.str.replace(",", "", regex=False)
    text = text.str.replace(":", "", regex=False)
    text = text.str.replace("-", "_", regex=False)

    # Remove spaces
    text = text.str.replace(" ", "_", regex=False)

    # Adjust separators
    text = text.str.replace(";_", "; ", regex=False)
    text = text.str.replace("_+", "_", regex=True)
    text = text.str.replace("_(", " (", regex=False)
    text = text.str.replace(")_", ") ", regex=False)
    text = text.str.replace("_[", " [", regex=False)
    text = text.str.replace("]_", "] ", regex=False)
    text = text.str.replace("; _", "; ", regex=False)

    return text
