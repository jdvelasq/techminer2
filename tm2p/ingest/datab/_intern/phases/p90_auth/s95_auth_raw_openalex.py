import pandas as pd  # type: ignore

from tm2p.enum import Field
from tm2p.ingest.datab._intern.oper.copy_col import copy_column
from tm2p.ingest.datab._intern.oper.transform_col import transform_column


def s03_auth_raw_openalex(root_directory: str) -> int:

    transform_column(
        source=Field.AUTH_FULL_NAME,
        target=Field.AUTH_RAW,
        function=_normalize,
        root_directory=root_directory,
    )

    return copy_column(
        source=Field.AUTH_RAW,
        target=Field.AUTH_NORM,
        root_directory=root_directory,
    )


def _normalize(series):

    def _normalize_item(text):

        if text == "":
            return pd.NA

        text = text.replace(".", "")
        words = text.split()

        if len(words) == 1:
            return text.title()

        letters = "".join(word[0].upper() for word in words[:-1])
        last_name = words[-1].title()

        return f"{last_name} {letters}"

    series = series.copy()
    series = series.str.split("; ")
    series = series.apply(
        lambda x: [_normalize_item(y) for y in x] if isinstance(x, list) else x
    )
    series = series.apply(
        lambda x: pd.NA if isinstance(x, list) and any(pd.isna(y) for y in x) else x
    )
    series = series.str.join("; ")

    return series
