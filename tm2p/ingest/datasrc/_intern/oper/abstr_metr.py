import sys
from typing import Callable, Optional

import pandas as pd  # type: ignore
from pandas import Series  # type: ignore

from tm2p.enum import Field

from ._file_dispatch import get_file_operations

ABSTR = Field.ABSTR_UPPER.value
WORD_RAW = "WORD_RAW"
KEY = "KEY"


def _get_df_abstr(
    root_directory: str,
):

    load_data, _, _ = get_file_operations()

    df = load_data(root_directory=root_directory, usecols=[ABSTR])

    df = df.dropna(subset=[ABSTR])
    df[ABSTR] = df[ABSTR].str.split(" ")
    df = df.explode(ABSTR)
    df = df.reset_index(drop=True)
    df = df[df[ABSTR].str.isalpha()]

    df.columns = [WORD_RAW]
    df[KEY] = df[WORD_RAW].str.lower()
    df = df.groupby(KEY, as_index=False).aggregate({WORD_RAW: set})

    return df


def _extract_mixed_cases(df: pd.DataFrame) -> pd.DataFrame:

    mixed_cases = df[df[KEY].apply(lambda x: len(x) > 1)]
    mixed_cases = df[df[WORD_RAW].apply(lambda x: len(x) > 1)]
    mixed_cases = mixed_cases[
        mixed_cases[WORD_RAW].apply(
            lambda x: any(y.isupper() for y in x) or any(y.islower() for y in x)
        )
    ]

    return mixed_cases


def _extract_one_letter_cases(df: pd.DataFrame) -> pd.DataFrame:

    one_letter = df[df[KEY].apply(lambda x: len(x) == 1)]
    one_letter = one_letter[
        one_letter[WORD_RAW].apply(lambda x: any(y == y.upper() for y in x))
    ]

    return one_letter


def _extract_mixed_letters_cases(df: pd.DataFrame) -> pd.DataFrame:

    mixed_letters = df.loc[
        df[WORD_RAW].apply(
            lambda x: any(
                any(ch.isupper() for ch in y) and any(ch.islower() for ch in y)
                for y in x
            )
        ),
        :,
    ]

    return mixed_letters


def _repair_mixed_cases(
    root_directory: str,
):

    load_data, save_data, get_path = get_file_operations()
    mixed_cases = _extract_mixed_cases(df=_get_df_abstr(root_directory=root_directory))

    if not mixed_cases.empty:
        df = load_data(root_directory=root_directory, usecols=None)
        df[ABSTR] = df[ABSTR].apply(lambda x: f" {x} " if isinstance(x, str) else x)
        for word in mixed_cases[KEY].to_list():
            if word.endswith("ing") or word in (
                "al",
                "am",
                "aim",
                "aims",
                "the",
                "in",
                "is",
            ):
                df[ABSTR] = df[ABSTR].str.replace(
                    f" {word.upper().strip()} ",
                    f" {word.lower().strip()} ",
                    regex=False,
                )
            else:
                df[ABSTR] = df[ABSTR].str.replace(
                    f" {word.lower().strip()} ",
                    f" {word.upper().strip()} ",
                    regex=False,
                )
        df[ABSTR] = df[ABSTR].str.strip()
        save_data(df=df, root_directory=root_directory)


def _repair_one_letter_cases(
    root_directory: str,
):

    load_data, save_data, get_path = get_file_operations()
    one_letter_cases = _extract_one_letter_cases(
        df=_get_df_abstr(root_directory=root_directory)
    )

    if not one_letter_cases.empty:
        df = load_data(root_directory=root_directory, usecols=None)
        df[ABSTR] = df[ABSTR].apply(lambda x: f" {x} " if isinstance(x, str) else x)
        for word in one_letter_cases[KEY].to_list():
            df[ABSTR] = df[ABSTR].str.replace(
                f" {word.upper().strip()} ", f" {word.lower().strip()} ", regex=False
            )
        df[ABSTR] = df[ABSTR].str.strip()
        save_data(df=df, root_directory=root_directory)


def _repair_mixed_letters_cases(
    root_directory: str,
):

    load_data, save_data, get_path = get_file_operations()
    mixed_letters_cases = _extract_mixed_letters_cases(
        df=_get_df_abstr(root_directory=root_directory)
    )

    if not mixed_letters_cases.empty:
        df = load_data(root_directory=root_directory, usecols=None)
        df[ABSTR] = df[ABSTR].apply(lambda x: f" {x} " if isinstance(x, str) else x)
        mixed_letters_cases = mixed_letters_cases[WORD_RAW].explode().to_list()
        for word in mixed_letters_cases:
            df[ABSTR] = df[ABSTR].str.replace(
                f" {word.strip()} ", f" {word.upper().strip()} ", regex=False
            )
        df[ABSTR] = df[ABSTR].str.strip()
        save_data(df=df, root_directory=root_directory)


def _print_header():
    sys.stderr.write("\n" + "-" * 80 + "\n")
    sys.stderr.write("DIAGNOSTIC:\n")
    sys.stderr.write("-" * 80 + "\n")


def _print_footer():
    sys.stderr.write("\n" + "-" * 80 + "\n\n")


def _review_mixed_cases(
    root_directory: str,
) -> None:

    df = _get_df_abstr(root_directory=root_directory)
    mixed_cases = _extract_mixed_cases(df=df)

    if not mixed_cases.empty:
        sys.stderr.write(f"Found {len(mixed_cases)} words with mixed cases:\n")
        mixed_cases = mixed_cases.head(100).to_string(index=False)
        sys.stderr.write(mixed_cases + "\n")
    else:
        sys.stderr.write("No words with mixed cases found.\n")


def _review_one_letter_cases(
    root_directory: str,
) -> None:

    df = _get_df_abstr(root_directory=root_directory)
    one_letter = _extract_one_letter_cases(df=df)

    if not one_letter.empty:
        sys.stderr.write(
            f"Found {len(one_letter)} one-letter words that are uppercase:\n"
        )
        one_letter = one_letter.to_string(index=False)
        sys.stderr.write(one_letter + "\n")
    else:
        sys.stderr.write("No one-letter uppercase words found.\n")


def _review_mixed_letters_cases(
    root_directory: str,
) -> None:

    df = _get_df_abstr(root_directory=root_directory)
    mixed_letters = _extract_mixed_letters_cases(df=df)

    if not mixed_letters.empty:
        sys.stderr.write(
            f"Found {len(mixed_letters)} mixed uppercase and lowercase letters in the same term:\n"
        )
        mixed_letters = mixed_letters.head(100).to_string(index=False)
        sys.stderr.write(mixed_letters + "\n")
    else:
        sys.stderr.write(
            "No mixed uppercase and lowercase letters in the same term found.\n"
        )


def abstr_metrics(
    root_directory: str,
) -> int:

    _repair_mixed_cases(root_directory)
    _repair_one_letter_cases(root_directory)
    _repair_mixed_letters_cases(root_directory)

    _print_header()

    _review_mixed_cases(root_directory)
    _review_one_letter_cases(root_directory)
    _review_mixed_letters_cases(root_directory)

    _print_footer()

    return 1
