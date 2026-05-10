import re
import sys
from typing import Optional

import pandas as pd  # type: ignore
from pandarallel import pandarallel  # type: ignore

from tm2p._intern import stdout_to_stderr
from tm2p._intern.data_access import load_main_csv_zip, save_main_csv_zip
from tm2p._intern.packag_data.word_lists import load_builtin_word_list
from tm2p.enum import Field

editorial_suffixes = sorted(
    load_builtin_word_list("editorial_suffixes.txt"),
    key=len,
    reverse=True,
)


def s02_remove_copyright(root_directory: str) -> int:

    df = load_main_csv_zip(root_directory=root_directory)

    df = df.drop_duplicates(subset=[Field.ABSTR_RAW.value])

    df[Field.ABSTR_TOK.value] = df[Field.ABSTR_TOK.value].str.replace(
        r"\. all rights reserved \.$", "", regex=True
    )

    df[Field.ABSTR_TOK.value] = df[Field.ABSTR_TOK.value].str.replace(
        r"this is an open access article\b.*$", "", regex=True
    )

    df[Field.ABSTR_TOK.value] = df[Field.ABSTR_TOK.value].str.replace(
        r"clinical trial registration :\b.*$", "", regex=True
    )

    df[Field.ABSTR_TOK.value] = df[Field.ABSTR_TOK.value].str.replace(
        r"this article is distributed under the terms of\b.*$",
        "",
        regex=True,
    )

    df[Field.ABSTR_TOK.value] = df[Field.ABSTR_TOK.value].str.replace(
        r"los articulos publicados por el sello editorial\b.*$",
        "",
        regex=True,
    )

    df[Field.ABSTR_TOK.value] = df[Field.ABSTR_TOK.value].str.replace(
        r"\. the open access version of this book\b.*$",
        "",
        regex=True,
    )

    df[Field.ABSTR_TOK.value] = df[Field.ABSTR_TOK.value].str.replace(
        r"\. contributors include :\b.*$",
        "",
        regex=True,
    )

    df[Field.ABSTR_TOK.value] = df[Field.ABSTR_TOK.value].str.replace(
        r"\. \d{4} selection and editorial matter ,.*$",
        "",
        regex=True,
    )

    df[Field.ABSTR_TOK.value] = df[Field.ABSTR_TOK.value].str.replace(
        r"\. prospero registration number.*$",
        "",
        regex=True,
    )

    df[Field.ABSTR_TOK.value] = df[Field.ABSTR_TOK.value].str.replace(
        r"\. copyright \d{4}.*$",
        "",
        regex=True,
    )

    df[Field.ABSTR_TOK.value] = df[Field.ABSTR_TOK.value].str.replace(
        r"\. trial sponsor :.*$",
        "",
        regex=True,
    )

    with stdout_to_stderr():
        progress_bar = True
        pandarallel.initialize(progress_bar=progress_bar, verbose=0)
        df[Field.ABSTR_TOK.value] = df.parallel_apply(  # type: ignore
            _process_row,
            axis=1,
        )
        sys.stderr.write("\n")

    save_main_csv_zip(df=df, root_directory=root_directory)

    return 1


def _process_row(row: pd.Series) -> Optional[str]:

    abstr = Field.ABSTR_TOK.value
    text = row[abstr]
    if pd.isna(text):
        return text

    for suffix in editorial_suffixes:
        text = re.sub(rf"{suffix}$", "", text, flags=re.IGNORECASE).strip()

    return text
