import sys
from pathlib import Path

# import pandas as pd  # type: ignore
from pandarallel import pandarallel  # type: ignore

from tm2p._intern import stdout_to_stderr
from tm2p._intern.data_access import load_main_csv_zip, save_main_csv_zip
from tm2p._intern.packag_data import load_builtin_mapping
from tm2p._intern.packag_data.word_lists import load_builtin_word_list
from tm2p.enum import Field
from tm2p.ingest.data_source._intern.phases.get_datab_marker import get_datab_marker

from ._intern.extract_org_name import extract_org_name_from_string

SUFFIXES = load_builtin_mapping("ltwa_suffixes.json")
PREFIXES = load_builtin_mapping("ltwa_prefixes.json")
FULLWORDS = load_builtin_mapping("ltwa_fullwords.json")
STOPWORDS = load_builtin_word_list("stopwords.txt")


AFFIL = Field.AFFIL.value
ORG = "ORG"

_ABBREVIATIONS = (
    "ab",
    "acad",
    "admin",
    "ag",
    "as",
    "asa",
    "assoc",
    "auth",
    "bv",
    "co",
    "commn",
    "corp",
    "ctr",
    "dept",
    "dept",
    "dev",
    "div",
    "eng",
    "fed",
    "glob",
    "gmbh",
    "govt",
    "grp",
    "hldg",
    "hldgs",
    "inc",
    "inst",
    "intl",
    "intl",
    "lab",
    "labs",
    "llc",
    "llp",
    "lp",
    "ltd",
    "med",
    "mfg",
    "mfr",
    "mgmt",
    "min",
    "mun",
    "na",
    "natl",
    "natl",
    "nv",
    "oy",
    "pa",
    "pc",
    "plc",
    "pte",
    "pty",
    "sa",
    "sci",
    "se",
    "sec",
    "soln",
    "solns",
    "svc",
    "svcs",
    "sys",
    "tech",
    "univ",
    "new",
)


def s01_org_thesaurus(root_directory: str) -> int:

    marker = get_datab_marker(root_directory)
    function = {
        "OpenAlex": _openalex,
        "PubMed": _scopus,
        "Scopus": _scopus,
        "WoS": _scopus,
    }[marker]

    return function(root_directory)


def _openalex(root_directory: str) -> int:

    df = load_main_csv_zip(root_directory)

    df[ORG] = df[ORG].str.replace(".", "")
    df[ORG] = df[ORG].str.replace('"', "")
    df[ORG] = df[ORG].str.replace(",", "")
    df[ORG] = df[ORG].str.replace("; ", " ; ")

    df[ORG] = df[ORG].apply(lambda x: f" {x.lower()} " if isinstance(x, str) else x)

    for stopword in STOPWORDS:
        if stopword not in [
            "new",
        ]:
            df[ORG] = df[ORG].str.replace(f" {stopword.lower()} ", " ", regex=False)

    df[ORG] = df[ORG].str.split()
    df[ORG] = df[ORG].apply(
        lambda x: [y.strip() for y in x] if isinstance(x, list) else x
    )

    with stdout_to_stderr():

        progress_bar = True
        pandarallel.initialize(progress_bar=progress_bar, verbose=0)

        df[ORG] = df[ORG].parallel_apply(
            lambda x: _apply_ltwa_to_words(x) if isinstance(x, list) else x
        )

        sys.stderr.write("\n")

    df[ORG] = df[ORG].apply(lambda x: [y for y in x if y] if isinstance(x, list) else x)
    df[ORG] = df[ORG].str.join(" ").str.upper()
    df[ORG] = df[ORG].str.strip()
    df[ORG] = df[ORG].str.replace(" ; ", "; ", regex=False)
    df[ORG] = df[ORG].str.strip()
    df[ORG] = df[ORG].str.replace("^[; ]+ ", "", regex=True)
    df[ORG] = df[ORG].str.replace("[ ;]+$", "", regex=True)

    save_main_csv_zip(df=df, root_directory=root_directory)

    return 1


def _scopus(root_directory: str) -> int:

    df = load_main_csv_zip(root_directory)
    df = df[[AFFIL]]
    df = df.dropna()
    df[AFFIL] = df[AFFIL].str.split("; ")
    df = df.explode(AFFIL)  # type: ignore
    df = df.drop_duplicates()

    with stdout_to_stderr():

        progress_bar = True
        pandarallel.initialize(progress_bar=progress_bar, verbose=0)

        df[ORG] = df[AFFIL].parallel_apply(extract_org_name_from_string)  ####
        sys.stderr.write("\n")

        df[ORG] = df[ORG].str.replace(".", "")
        df[ORG] = df[ORG].str.replace('"', "")

        df[ORG] = df[ORG].apply(lambda x: f" {x.lower()} " if isinstance(x, str) else x)

        for stopword in STOPWORDS:
            if stopword not in _ABBREVIATIONS:
                df[ORG] = df[ORG].str.replace(f" {stopword.lower()} ", " ", regex=False)

        df[ORG] = df[ORG].str.split()
        df[ORG] = df[ORG].parallel_apply(  #####
            lambda x: _apply_ltwa_to_words(x) if isinstance(x, list) else x
        )
        df[ORG] = df[ORG].str.join(" ").str.upper()
        df[ORG] = df[ORG].str.strip()
        df[ORG] = df[ORG].replace("", "[UNKNOWN]")  # type: ignore

        sys.stderr.write("\n")

    mapping = dict(zip(df[AFFIL], df[ORG]))

    grouped_df = df.groupby(ORG, as_index=False)[AFFIL].apply(list)  # type: ignore

    filepath = Path(root_directory) / "refine" / "thesaurus" / "org.the.txt"

    with open(filepath, "w", encoding="utf-8") as file:

        for _, row in grouped_df.iterrows():
            org = row[ORG]
            file.write(f"{org}\n")
            for affil in sorted(row[AFFIL]):
                file.write(f"    {affil}\n")

    filepath_bak = filepath.with_suffix(".bak")
    filepath_bak.write_text(filepath.read_text(encoding="utf-8"), encoding="utf-8")

    df = load_main_csv_zip(root_directory)
    df[ORG] = df[AFFIL].str.split("; ")
    df[ORG] = df[ORG].apply(
        lambda affils: (
            [mapping[affil] for affil in affils] if isinstance(affils, list) else affils
        )
    )

    df[ORG] = df[ORG].str.join("; ")

    save_main_csv_zip(df=df, root_directory=root_directory)

    return 1


def _apply_ltwa_to_words(words: list[str]) -> list[str]:

    new_words = []

    for word in words:

        # word = word.replace(".", "")
        # if word.lower() in _ABBREVIATIONS:
        #     new_words.append(word)
        #     continue

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
