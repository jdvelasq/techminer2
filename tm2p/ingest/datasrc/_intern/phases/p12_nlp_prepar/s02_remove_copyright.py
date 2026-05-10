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

    for regex in [
        r"\. all rights reserved \.$",
        r"this is an open access article\b.*$",
        r"clinical trial registration :\b.*$",
        r"this article is distributed under the terms of\b.*$",
        r"los articulos publicados por el sello editorial\b.*$",
        r"\. the open access version of this book\b.*$",
        r"\. contributors include :\b.*$",
        r"\. \d{4} selection and editorial matter ,.*$",
        r"\. prospero registration number.*$",
        r"\. copyright \d{4}.*$",
        r"\. trial sponsor :.*$",
    ]:

        df[Field.ABSTR_TOK.value] = df[Field.ABSTR_TOK.value].str.replace(
            regex, "", regex=True
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
