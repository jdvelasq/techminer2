# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""Clean abstract and title texts."""

import pathlib

import contractions  # type: ignore
import pandas as pd  # type: ignore


def internal__clean_text(
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
    )

    if source in dataframe.columns and not dataframe[source].dropna().empty:
        dataframe[dest] = clean_text(dataframe[source])

    dataframe.to_csv(
        database_file,
        sep=",",
        encoding="utf-8",
        index=False,
        compression="zip",
    )


def clean_text(text):
    """:meta private:"""

    # remove [...]
    text = text.map(
        lambda w: pd.NA if w[0] == "[" and w[-1] == "]" else w, na_action="ignore"
    )

    text = text.str.lower()

    # remove contractions
    text = text.map(contractions.fix, na_action="ignore")

    # remove all html tags
    text = text.str.replace("<.*?>", "", regex=True)

    # process puntuation
    text = text.str.replace("’", "'", regex=False)
    text = text.str.replace(";", ".", regex=False)
    text = text.str.replace(r"(", r" ( ", regex=False)  # (
    text = text.str.replace(r")", r" ) ", regex=False)  # )
    text = text.str.replace(r"$", r" $ ", regex=False)  # $
    text = text.str.replace(r"/", r" / ", regex=False)  # /
    text = text.str.replace(r"?", r" ? ", regex=False)  # ?
    text = text.str.replace(r"¿", r" ¿ ", regex=False)  # ?
    text = text.str.replace(r"!", r" ! ", regex=False)  # !
    text = text.str.replace(r"¡", r" ¡ ", regex=False)  # ¡
    text = text.str.replace(r"=", r" = ", regex=False)  # =
    text = text.str.replace(r'"', r' " ', regex=False)  # "
    text = text.str.replace(r":", r" : ", regex=False)  # :
    text = text.str.replace(r"%", r" % ", regex=False)  # %

    text = text.str.replace(r"(\w+)(,\s)", r"\1 \2", regex=True)  # ,
    text = text.str.replace(r"(\')(,\s)", r"\1 \2", regex=True)  # ,
    text = text.str.replace(r"(\w+)(\.\s)", r"\1 \2", regex=True)  # .
    text = text.str.replace(r"(\w+)\.$", r"\1 .", regex=True)  # .
    text = text.str.replace(r"(\w+)'s(\b)", r"\1\2", regex=True)
    text = text.str.replace(r"(\w+)'(\s)", r"\1\2", regex=True)  # 's  # s
    text = text.str.replace("—", "-", regex=False)
    text = text.str.replace("-", " ", regex=False)

    # remove all non-ascii characters
    text = text.str.normalize("NFKD")
    text = text.str.encode("ascii", errors="ignore")
    text = text.str.decode("utf-8")

    # rempve multiple spaces
    text = text.str.replace(r"\s+", r" ", regex=True)
    text = text.str.strip()

    return text
