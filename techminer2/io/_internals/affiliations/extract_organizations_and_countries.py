import re
from pathlib import Path
from typing import List

import pandas as pd  # type: ignore

from techminer2 import Field
from techminer2._constants import COUNTRY_NAMES, COUNTRY_TO_ALPHA3
from techminer2._internals.data_access import load_main_data, save_main_data

_AMBIGUOUS_INDICATOR = [
    "institute of",
    "institut de",
    "instituto de",
    "institutt for",
    "center for",
    "centre for",
    "centro de",
    "centro para",
    "laboratory of",
    "lab of",
    "laboratoire de",
    "laboratorio de",
    "school of",
    "école de",
    "escuela de",
    "escola de",
    "graduate school",
    "doctoral school",
]

_CORPORATE_SUFFIX = [
    "ltd",
    "limited",
    "inc",
    "incorporated",
    "corp",
    "corporation",
    "gmbh",
    "s.a.",
    "s.l.",
    "srl",
    "s.r.l.",
    "spa",
    "s.p.a.",
    "bv",
    "b.v.",
    "llc",
    "l.l.c.",
    "ag",
    "plc",
    "co.",
    "company",
]


_COUNTRY_REPLACEMENTS = [
    ("Bosnia and Herz.", "Bosnia and Herzegovina"),
    ("Brasil", "Brazil"),
    ("Central African Rep.", "Central African Republic"),
    ("Congo, Democratic Republic of The", "Democratic Republic of The Congo"),
    ("Côte D'Ivoire", "Cote D'Ivoire"),
    ("Czech Republic", "Czechia"),
    ("Dem. Rep. Congo", "Democratic Republic of The Congo"),
    ("Dominican Rep.", "Dominican Republic"),
    ("Eq. Guinea", "Equatorial Guinea"),
    ("Espana", "Spain"),
    ("Falkland Is.", "Falkland Islands"),
    ("Macao", "China"),
    ("Macau", "China"),
    ("N. Cyprus", "Cyprus"),
    ("Palestine, State Of", "Palestine"),
    ("Peoples R China", "China"),
    ("Perú", "Peru"),
    ("Rusia", "Russia"),
    ("Russian Federation", "Russia"),
    ("Saint Helena, Ascension and Tristan Da Cunha", "Saint Helena"),
    ("Solomon Is.", "Solomon Islands"),
    ("St. Kitts and Nevis", "Saint Kitts and Nevis"),
    ("St. Lucia", "Saint Lucia"),
    ("St. Vincent and The Grenadines", "Saint Vincent and The Grenadines"),
    ("Syrian Arab Republic", "Syria"),
    ("Trinidad & Tobago", "Trinidad and Tobago"),
    ("Türkiye", "Turkey"),
    ("United States of America", "United States"),
    ("USA", "United States"),
    ("Viet Nam", "Vietnam"),
    ("Viet-Nam", "Vietnam"),
    ("W. Sahara", "Western Sahara"),
]

_DEPARTMENT_INDICATOR = [
    "department of",
    "dept of",
    "dept.",
    "faculty of",
    "school of",
    "college of",
    "division of",
    "unit of",
    "section of",
    "chair of",
    "professorship",
    "lehrstuhl",
    "departamento de",
    "département de",
    "facoltà di",
    "facultad de",
    "dipartimento di",
    "departement",
    "división de",
]

_GOVERNMENT_KEYWORD = [
    "ministry",
    "government",
    "agency",
    "council",
    "commission",
    "authority",
    "department of",
    "bureau",
    "office of",
]


_ORGANIZATION_KEYWORD = [
    "university",
    "universidad",
    "université",
    "universität",
    "università",
    "universiteit",
    "yliopisto",
    "univerza",
    "univerzita",
    "universitas",
    "universiti",
    "universitet",
    "rijksuniversiteit",
    "polytechnic",
    "politecnico",
    "politechnika",
    "polytechnique",
    "institute",
    "instituto",
    "institut",
    "institutt",
    "college",
    "school",
    "academy",
    "academia",
    "hospital",
    "clinic",
    "klinik",
    "medical center",
    "medical centre",
    "research center",
    "research centre",
    "national laboratory",
    "foundation",
    "fundación",
    "fondation",
    "stiftung",
]


# ----------------------------------------------------------------------------
# Country extraction
# ----------------------------------------------------------------------------


def _extract_country_from_string(affiliation: str) -> str:

    country = affiliation.split(",")[-1].strip()

    for pat, repl in _COUNTRY_REPLACEMENTS:
        country = country.replace(pat, repl)

    if country not in COUNTRY_NAMES:
        country = "[N/A]"

    return country


# ----------------------------------------------------------------------------
# Organization extraction
# ----------------------------------------------------------------------------


def _clean_part(part: str) -> str:
    part = part.strip()
    part = re.sub(r"\s*\([^)]*\)\s*$", "", part)
    return part.strip()


def _contains_corporate_suffix(text: str) -> bool:
    if not text or not text.strip():
        return False
    text_lower = text.lower()
    return any(
        re.search(r"\b" + re.escape(suffix) + r"\b", text_lower)
        for suffix in _CORPORATE_SUFFIX
    )


def _contains_government_keyword(text: str) -> bool:
    if not text or not text.strip():
        return False
    text_lower = text.lower()
    return any(keyword in text_lower for keyword in _GOVERNMENT_KEYWORD)


def _contains_org_keyword(text: str) -> bool:
    if not text or not text.strip():
        return False
    text_lower = text.lower()
    return any(keyword in text_lower for keyword in _ORGANIZATION_KEYWORD)


def _has_multiple_words(text: str) -> bool:
    return len(text.split()) >= 2


def _is_acronym(text: str) -> bool:
    return text.isupper() and len(text) >= 2 and text.isalpha()


def _is_organization(text: str) -> bool:
    if not text or not text.strip():
        return False
    return (
        _contains_org_keyword(text)
        or _contains_corporate_suffix(text)
        or _contains_government_keyword(text)
        or _has_multiple_words(text)
        or _is_acronym(text)
    )


def _remove_duplicate_segments(parts: List[str]) -> List[str]:
    if len(parts) < 2:
        return parts
    result = []
    for i, part in enumerate(parts):
        if i == 0 or part.lower() != parts[i - 1].lower():
            result.append(part)
    return result


def _starts_with_ambiguous_indicator(text: str) -> bool:
    if not text or not text.strip():
        return False
    text_lower = text.lower().strip()
    return any(text_lower.startswith(indicator) for indicator in _AMBIGUOUS_INDICATOR)


def _starts_with_department(text: str) -> bool:
    if not text or not text.strip():
        return False
    text_lower = text.lower().strip()
    return any(text_lower.startswith(indicator) for indicator in _DEPARTMENT_INDICATOR)


def _extract_organization_from_string(affiliation: str) -> str:

    parts = [_clean_part(p) for p in affiliation.split(",")]
    parts = [p for p in parts if p]

    if not parts:
        return "[N/A]"

    parts = _remove_duplicate_segments(parts)

    if len(parts) >= 2:
        first = parts[0]
        second = parts[1]

        if _starts_with_ambiguous_indicator(first) and _is_organization(second):
            return second

        if _starts_with_department(first) and _is_organization(second):
            return second

    if len(parts) >= 1:
        first = parts[0]
        if not _starts_with_department(first) and _is_organization(first):
            return first

    if len(parts) >= 2 and _is_organization(parts[1]):
        return parts[1]

    if len(parts) >= 1 and _is_organization(parts[0]):
        return parts[0]

    return "[N/A]"


# ----------------------------------------------------------------------------


def _get_affiliations_df(dataframe: pd.DataFrame) -> pd.DataFrame:

    affil_df = dataframe[[Field.AFFIL_RAW.value]].copy()
    affil_df = affil_df.dropna()
    affil_df[Field.AFFIL_RAW.value] = affil_df[Field.AFFIL_RAW.value].str.split("; ")
    affil_df = affil_df.explode(Field.AFFIL_RAW.value)
    affil_df[Field.AFFIL_RAW.value] = affil_df[Field.AFFIL_RAW.value].str.strip()
    affil_df = affil_df.drop_duplicates()

    return affil_df


def _get_country_mapping(df: pd.DataFrame) -> dict[str, str]:
    df = df[[Field.AFFIL_RAW.value, Field.COUNTRY.value]].dropna()
    df = df.drop_duplicates()
    mapping: dict[str, str] = pd.Series(
        df[Field.COUNTRY.value].values, index=df[Field.AFFIL_RAW.value]
    ).to_dict()
    return mapping


def _get_organization_mapping(df: pd.DataFrame) -> dict[str, str]:
    df = df[[Field.AFFIL_RAW.value, Field.ORGANIZATION.value]].dropna()
    df = df.drop_duplicates()
    mapping: dict[str, str] = pd.Series(
        df[Field.ORGANIZATION.value].values, index=df[Field.AFFIL_RAW.value]
    ).to_dict()
    return mapping


def _create_country_column(
    df: pd.DataFrame, country_mapping: dict[str, str]
) -> pd.DataFrame:

    df = df.copy()

    df[Field.COUNTRY.value] = df[Field.AFFIL_RAW.value].copy()
    df[Field.COUNTRY.value] = df[Field.COUNTRY.value].fillna("[N/A]")
    df[Field.COUNTRY.value] = df[Field.COUNTRY.value].str.split("; ")
    df[Field.COUNTRY.value] = df[Field.COUNTRY.value].map(
        lambda affils: [country_mapping.get(affil, "[N/A]") for affil in affils],
    )
    df[Field.FIRSTAUTH_COUNTRY.value] = df[Field.COUNTRY.value].map(
        lambda countries: countries[0] if countries else "[N/A]",
    )
    df[Field.COUNTRY.value] = df[Field.COUNTRY.value].map(set)
    df[Field.COUNTRY.value] = df[Field.COUNTRY.value].str.join("; ")

    return df


def _create_organization_column(
    df: pd.DataFrame, organization_mapping: dict[str, str]
) -> pd.DataFrame:
    df = df.copy()

    df[Field.ORGANIZATION.value] = df[Field.AFFIL_RAW.value].copy()
    df[Field.ORGANIZATION.value] = df[Field.ORGANIZATION.value].fillna("[N/A]")
    df[Field.ORGANIZATION.value] = df[Field.ORGANIZATION.value].str.split("; ")
    df[Field.ORGANIZATION.value] = df[Field.ORGANIZATION.value].map(
        lambda affils: [organization_mapping.get(affil, "[N/A]") for affil in affils]
    )
    df[Field.FIRSTAUTH_ORGANIZATION.value] = df[Field.ORGANIZATION.value].map(
        lambda orgs: orgs[0] if orgs else "[N/A]"
    )
    df[Field.ORGANIZATION.value] = df[Field.ORGANIZATION.value].str.join("; ")

    return df


def _create_thesaurus(
    root_directory: str, mapping: dict[str, str], filename: str
) -> None:

    dataframe = pd.DataFrame(
        {
            "key": list(mapping.values()),
            "label": list(mapping.keys()),
        }
    )
    groupby_df = dataframe.groupby("key", as_index=False)["label"].apply(list)

    filepath = Path(root_directory) / "data" / "thesaurus" / filename
    with open(filepath, "w", encoding="utf-8") as file:
        for _, row in groupby_df.iterrows():
            key = row["key"]
            file.write(f"{key}\n")
            for value in row["label"]:
                file.write(f"    {value}\n")


def _assign_country_code(df: pd.DataFrame) -> pd.Series:

    df = df.copy()
    df[Field.ORGANIZATION.value] += df[Field.COUNTRY.value].map(
        lambda country: " [" + COUNTRY_TO_ALPHA3.get(country, "N/A") + "]"
    )
    return df[Field.ORGANIZATION.value]


def extract_organizations_and_countries(root_directory: str) -> int:

    dataframe = load_main_data(root_directory=root_directory)

    affil_df = _get_affiliations_df(dataframe)
    affil_df[Field.COUNTRY.value] = affil_df[Field.AFFIL_RAW.value].apply(
        _extract_country_from_string
    )
    affil_df[Field.ORGANIZATION.value] = affil_df[Field.AFFIL_RAW.value].apply(
        _extract_organization_from_string
    )

    affil_df[Field.ORGANIZATION.value] = _assign_country_code(affil_df)

    country_mapping = _get_country_mapping(affil_df)
    organization_mapping = _get_organization_mapping(affil_df)

    dataframe = _create_country_column(dataframe, country_mapping)
    dataframe = _create_organization_column(dataframe, organization_mapping)

    save_main_data(df=dataframe, root_directory=root_directory)

    _create_thesaurus(
        root_directory=root_directory,
        mapping=country_mapping,
        filename="countries.the.txt",
    )

    _create_thesaurus(
        root_directory=root_directory,
        mapping=organization_mapping,
        filename="organizations.the.txt",
    )

    return int(dataframe[Field.AFFIL_RAW.value].notna().sum())
