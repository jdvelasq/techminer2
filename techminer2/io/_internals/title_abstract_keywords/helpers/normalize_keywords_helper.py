import re
from pathlib import Path

import pandas as pd  # type: ignore

KEYWORDS_MAX_LENGTH = 60


def normalize_keywords_helper(source: str, target: str, root_directory: str) -> int:

    database_file = Path(root_directory) / "data" / "processed" / "main.csv.zip"

    dataframe = pd.read_csv(
        database_file,
        encoding="utf-8",
        compression="zip",
        low_memory=False,
    )

    if source not in dataframe.columns:
        return 0

    text = dataframe[source]
    text = _normalize_empty_strings(text)
    text = _uppercase_keywords(text)
    text = _fix_separators(text)
    text = _normalize_unicode(text)
    text = _normalize_quotes_and_slashes(text)
    text = _remove_wrapper_characters(text)
    text = _remove_possessives_and_ampersands(text)
    text = _remove_leading_articles(text)
    text = _normalize_spacing_and_punctuation(text)
    text = _replace_spaces_with_underscores(text)
    text = _fix_separator_formatting(text)
    text = _remove_empty_terms(text)

    dataframe[target] = text

    dataframe.to_csv(
        database_file,
        sep=",",
        encoding="utf-8",
        index=False,
        compression="zip",
    )

    return len(dataframe[target].dropna())


def _normalize_empty_strings(text: pd.Series) -> pd.Series:
    return text.map(lambda x: pd.NA if isinstance(x, str) and x.strip() == "" else x)


def _uppercase_keywords(text: pd.Series) -> pd.Series:
    return text.str.upper()


def _fix_separators(text: pd.Series) -> pd.Series:
    return text.map(
        lambda x: (
            x.replace(",", ";")
            if isinstance(x, str) and ";" not in x and len(x) > KEYWORDS_MAX_LENGTH
            else x
        )
    )


def _normalize_unicode(text: pd.Series) -> pd.Series:
    text = text.str.normalize("NFKD")
    text = text.str.encode("ascii", errors="ignore")
    text = text.str.decode("utf-8")
    text = text.str.replace("<.*?>", "", regex=True)
    return text


def _normalize_quotes_and_slashes(text: pd.Series) -> pd.Series:
    text = text.str.replace("ʿ", "'", regex=False)
    text = text.str.replace("'", "'", regex=False)
    text = text.str.replace("'", "'", regex=False)
    text = text.str.replace("/", "_", regex=False)
    text = text.str.replace("\\", "_", regex=False)
    return text


def _remove_wrapper_characters(text: pd.Series) -> pd.Series:
    text = text.str.split("; ")
    text = text.map(lambda x: [z.strip() for z in x], na_action="ignore")
    text = text.map(_strip_surrounding_chars, na_action="ignore")
    text = text.str.join("; ")
    return text


def _strip_surrounding_chars(string_list: list[str]) -> list[str]:
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
    string_list = [z for z in string_list if not z.isdigit()]
    string_list = [z for z in string_list if z != ""]
    string_list = [z.strip() for z in string_list]
    return string_list


def _remove_possessives_and_ampersands(text: pd.Series) -> pd.Series:
    text = text.str.replace("'S ", " ", regex=False)
    text = text.str.replace("'", " ", regex=False)
    text = text.str.replace(r"^\s+", "", regex=True)
    text = text.str.replace("&", " AND ", regex=False)
    return text


def _remove_leading_articles(text: pd.Series) -> pd.Series:
    text = text.str.split("; ")
    text = text.map(lambda x: [re.sub("^AND ", "", z) for z in x], na_action="ignore")
    text = text.map(lambda x: [re.sub("^AN ", "", z) for z in x], na_action="ignore")
    text = text.map(lambda x: [re.sub("^A ", "", z) for z in x], na_action="ignore")
    text = text.map(lambda x: [re.sub("^THE ", "", z) for z in x], na_action="ignore")
    text = text.str.join("; ")
    return text


def _normalize_spacing_and_punctuation(text: pd.Series) -> pd.Series:
    text = text.str.replace(r"\s+", " ", regex=True)
    text = text.str.replace('"', "", regex=False)
    text = text.str.replace(".", "", regex=False)
    text = text.str.replace(",", "", regex=False)
    text = text.str.replace(":", "", regex=False)
    text = text.str.replace("-", "_", regex=False)
    text = text.str.replace("\u2013", "_", regex=False)
    return text


def _replace_spaces_with_underscores(text: pd.Series) -> pd.Series:
    return text.str.replace(" ", "_", regex=False)


def _fix_separator_formatting(text: pd.Series) -> pd.Series:
    text = text.str.replace(";_", "; ", regex=False)
    text = text.str.replace("_+", "_", regex=True)
    text = text.str.replace("_(", " (", regex=False)
    text = text.str.replace(")_", ") ", regex=False)
    text = text.str.replace("_[", " [", regex=False)
    text = text.str.replace("]_", "] ", regex=False)
    text = text.str.replace("; _", "; ", regex=False)
    return text


def _remove_empty_terms(text: pd.Series) -> pd.Series:
    text = text.str.split("; ")
    text = text.map(lambda x: [z for z in x if z.strip() != ""], na_action="ignore")
    text = text.str.join("; ")
    return text
