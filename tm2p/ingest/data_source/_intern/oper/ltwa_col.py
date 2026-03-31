import sys
from typing import Optional

from pandarallel import pandarallel  # type: ignore

from tm2p import Field
from tm2p._intern import stdout_to_stderr
from tm2p._intern.packag_data import load_builtin_mapping
from tm2p._intern.packag_data.word_lists import load_builtin_word_list

from ._file_dispatch import get_file_operations

SUFFIXES = load_builtin_mapping("ltwa_suffixes.json")
PREFIXES = load_builtin_mapping("ltwa_prefixes.json")
FULLWORDS = load_builtin_mapping("ltwa_fullwords.json")
STOPWORDS = load_builtin_word_list("stopwords.txt")


def _apply_ltwa_to_words(words: list[str]) -> list[str]:

    new_words = []

    for word in words:

        for suffix in sorted(SUFFIXES.keys(), reverse=True):
            abbreviation = SUFFIXES[suffix]
            if isinstance(abbreviation, list):
                abbreviation = abbreviation[0]
            if word.endswith(suffix):
                word = word[: -len(suffix)] + abbreviation
                break

        for prefix in sorted(PREFIXES.keys(), reverse=True):
            abbreviation = PREFIXES[prefix]
            if isinstance(abbreviation, list):
                abbreviation = abbreviation[0]
            if word.startswith(prefix):
                word = abbreviation
                break

        for fullword, abbreviation in FULLWORDS.items():
            if isinstance(abbreviation, list):
                abbreviation = abbreviation[0]
            if word == fullword:
                word = abbreviation
                break

        new_words.append(word)

    return new_words


def ltwa_column(
    source: Field,
    target: Field,
    root_directory: str,
    na_action: Optional[str] = None,
) -> int:

    load_data, save_data, get_path = get_file_operations()

    df = load_data(root_directory=root_directory, usecols=None)

    if source.value not in df.columns:
        if na_action == "ignore":
            return 0
        raise KeyError(
            f"Source column '{source.value}' not found in {get_path(root_directory).name}"
        )

    df[target.value] = df[source.value].copy()
    df[target.value] = df[target.value].apply(
        lambda x: f" {x} " if isinstance(x, str) else x
    )
    df[target.value] = df[target.value].str.lower()
    df[target.value] = df[target.value].str.replace("; ", " ; ", regex=False)
    for stopword in STOPWORDS:
        df[target.value] = df[target.value].str.replace(
            f" {stopword.lower()} ", " ", regex=False
        )

    df[target.value] = df[target.value].str.split()

    with stdout_to_stderr():
        progress_bar = True
        pandarallel.initialize(progress_bar=progress_bar, verbose=0)
        df[target.value] = df[target.value].parallel_apply(
            lambda x: _apply_ltwa_to_words(x) if isinstance(x, list) else x
        )
        sys.stderr.write("\n")

    df[target.value] = df[target.value].str.join(" ")
    df[target.value] = df[target.value].str.replace(" ; ", "; ", regex=False)
    df[target.value] = df[target.value].str.upper()

    save_data(df=df, root_directory=root_directory)

    return len(df)
