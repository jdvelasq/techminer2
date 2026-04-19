import re
import unicodedata
from pathlib import Path

import Levenshtein  # type: ignore
import pandas as pd  # type: ignore
from tqdm import tqdm  # type: ignore

from tm2p._intern.data_access import load_main_csv_zip, save_main_csv_zip
from tm2p.enum import Field
from tm2p.ingest.datasrc._intern.phases.get_datab_marker import get_datab_marker

AUTH_FIRST = Field.AUTH_FIRST.value
AUTH_RAW = Field.AUTH_RAW.value
GCR_WOS_FORMAT = Field.GCR_WOS_FORMAT.value
GCR_FREE_TEXT = Field.GCR_FREE_TEXT.value
REC_ID = Field.REC_ID.value
SRC = Field.SRC.value

TITLE = Field.TITLE_RAW.value
YEAR = Field.YEAR.value

SELECTED_FIELDS = [
    REC_ID,
    TITLE,
    AUTH_RAW,
    YEAR,
    SRC,
]


def s01_gcr_wos_format(root_directory: str) -> int:

    marker = get_datab_marker(root_directory)
    function = {
        "OpenAlex": None,
        "PubMed": None,
        "Scopus": _scopus,
        "WoS": None,
    }[marker]

    if function:
        return function(root_directory=root_directory)

    return 0


def _scopus(root_directory: str) -> int:

    df = load_main_csv_zip(root_directory=root_directory)

    if Field.GCR_FREE_TEXT.value not in df.columns:
        df[Field.GCR_WOS_FORMAT.value] = pd.NA
        save_main_csv_zip(df=df, root_directory=root_directory)
        return 0

    mapping = _generate_gcr_thesaurus_file(root_directory=root_directory)
    result = _process_references(mapping=mapping, root_directory=root_directory)

    return result


def _generate_gcr_thesaurus_file(root_directory: str) -> dict[str, list[str]]:

    df = load_main_csv_zip(root_directory=root_directory)
    df = df[SELECTED_FIELDS].dropna()
    df[AUTH_FIRST] = df[AUTH_RAW].apply(_extract_first_author_surname)
    df[TITLE] = df[TITLE].apply(_format_text)
    df[YEAR] = df[YEAR].astype(str)
    df = df.sort_values(by=[Field.REC_ID.value])  # type: ignore

    references = _get_cited_references(root_directory=root_directory)
    mapping = _create_mapping(formated=df, references=references)

    _save_thesaurus_file(mapping=mapping, root_directory=root_directory)

    return mapping


def _extract_first_author_surname(authors: str) -> str:
    surname = authors.split(" ")[0]
    surname = surname.lower()
    surname = surname.replace(",", "")
    surname = unicodedata.normalize("NFD", surname)
    surname = surname.encode("ascii", "ignore").decode("utf-8")
    return surname


def _format_text(text: str) -> str:
    text = unicodedata.normalize("NFD", text)
    text = text.encode("ascii", "ignore").decode("utf-8")
    text = text.lower()
    text = re.sub(r"[.,:;()\-]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def _get_cited_references(root_directory: str) -> pd.DataFrame:

    references = load_main_csv_zip(root_directory=root_directory)
    references = references[[GCR_FREE_TEXT]].copy()
    references = references.dropna()
    references = references.rename(columns={GCR_FREE_TEXT: "text"})  # type: ignore

    references["text"] = references["text"].str.split(";")
    references = references.explode("text")
    references["text"] = references["text"].str.strip()
    references = references.drop_duplicates()
    references = references.reset_index(drop=True).copy()

    references["key"] = references["text"].apply(_format_text)

    return references


def _create_mapping(
    formated: pd.DataFrame,
    references: pd.DataFrame,
) -> dict[str, list[str]]:

    mapping = {}
    remaining_references = references.copy()

    for i in tqdm(
        range(formated.shape[0]),
        total=formated.shape[0],
        bar_format="  {percentage:3.2f}% {bar} | {n_fmt}/{total_fmt} [{rate_fmt}] |",
        ascii=" :",
        ncols=73,
    ):
        row = formated.iloc[i]
        refs = remaining_references.copy()
        refs = _keep_refs_with_approx_year_match(refs, row[YEAR])
        refs = _keep_refs_with_approx_author_match(refs, row[AUTH_FIRST])
        refs = _keep_refs_with_approx_title_match(refs, row[TITLE])

        if len(refs) > 0:
            mapping[row[REC_ID]] = sorted(refs.text.tolist())
            remaining_references = remaining_references.drop(refs.index)

    return mapping


def _keep_refs_with_approx_year_match(refs, year):
    year_before = str(int(year) - 1)
    year_after = str(int(year) + 1)
    refs = refs.copy()
    refs = refs.loc[
        refs.key.str.lower().str.contains(year)
        | refs.key.str.lower().str.contains(year_before)
        | refs.key.str.lower().str.contains(year_after),
        :,
    ]
    return refs


def _keep_refs_with_approx_author_match(refs, surname):

    def jaro_winkler(text):
        words = text.split()
        words = words[:3]
        metric = max(Levenshtein.jaro_winkler(surname, word) for word in words)
        return metric >= 0.95

    refs = refs.copy()
    refs = refs.loc[refs.key.apply(jaro_winkler), :]
    return refs


def _keep_refs_with_approx_title_match(refs, title):

    def compute_token_recall(text):
        counter = 0
        for word in title_words:
            if word in text:
                counter += 1
        return counter / len(title_words) >= 0.85

    title_words = title.split()
    refs = refs.copy()
    refs = refs.loc[refs.key.apply(compute_token_recall), :]
    return refs


def _get_reverse_mapping(mapping: dict[str, list[str]]) -> dict[str, str]:
    reverse_mapping = {}
    for key, values in mapping.items():
        for value in values:
            reverse_mapping[value] = key
    return reverse_mapping


def _save_thesaurus_file(mapping: dict[str, list[str]], root_directory: str) -> None:

    filepath1 = Path(root_directory) / "refine" / "thesaurus" / "gcr.the.txt"
    filepath2 = Path(root_directory) / "ingest" / "process" / "_gcr.the.txt"

    for filepath in [filepath1, filepath2]:

        with open(filepath, "w", encoding="utf-8") as file:
            for key, values in mapping.items():
                file.write(f"{key}\n")
                for value in values:
                    file.write(f"    {value}\n")


def _process_references(
    mapping: dict[str, list[str]],
    root_directory: str,
) -> int:

    df = load_main_csv_zip(root_directory=root_directory)
    df[GCR_WOS_FORMAT] = df[GCR_FREE_TEXT].copy()
    df[GCR_WOS_FORMAT] = df[GCR_WOS_FORMAT].str.split(";")
    df[GCR_WOS_FORMAT] = df[GCR_WOS_FORMAT].apply(
        lambda refs: (
            [y.strip() for y in refs]
            if isinstance(refs, list)
            else refs if isinstance(refs, list) else refs
        ),
    )

    #

    df[GCR_WOS_FORMAT] = df[GCR_WOS_FORMAT].apply(
        lambda refs: (
            [mapping[ref] for ref in refs if ref in mapping]
            if isinstance(refs, list)
            else refs
        ),
    )
    df[GCR_WOS_FORMAT] = df[GCR_WOS_FORMAT].str.join("; ")

    save_main_csv_zip(df=df, root_directory=root_directory)

    non_null_count = int(df[GCR_WOS_FORMAT].notna().sum())

    return non_null_count
