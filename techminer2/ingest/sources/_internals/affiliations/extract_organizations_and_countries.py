import re
from pathlib import Path
from typing import List

import pandas as pd  # type: ignore

from techminer2 import CorpusField
from techminer2._internals.data_access import load_main_data, save_main_data
from techminer2._internals.package_data import (
    load_builtin_mapping,
    load_builtin_word_list,
)

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
    "universitāte",
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


AFFIL_RAW = CorpusField.AFFIL_RAW.value
COUNTRY_AND_AFFIL = CorpusField.COUNTRY_AND_AFFIL.value
COUNTRY = CorpusField.COUNTRY.value
ORG_AUTH_FIRST = CorpusField.ORG_AUTH_FIRST.value
ORG_AND_AFFIL = CorpusField.ORG_AND_AFFIL.value
ORG = CorpusField.ORG.value


# ----------------------------------------------------------------------------
# Country extraction
# ----------------------------------------------------------------------------


def _extract_country_from_string(affiliation: str) -> str:

    country = affiliation.split(",")[-1].strip()

    for pat, repl in _COUNTRY_REPLACEMENTS:
        country = country.replace(pat, repl)

    country_names = load_builtin_word_list("country_names.txt")
    if country not in country_names:
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

    organizations = load_builtin_word_list("organizations.txt")
    for org in organizations:
        if org.lower() in affiliation.lower():
            return org

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

    affil_df = dataframe[[AFFIL_RAW]].copy()
    affil_df = affil_df.dropna()
    affil_df[AFFIL_RAW] = affil_df[AFFIL_RAW].str.split("; ")
    affil_df = affil_df.explode(AFFIL_RAW)
    affil_df[AFFIL_RAW] = affil_df[AFFIL_RAW].str.strip()
    affil_df = affil_df.drop_duplicates()

    return affil_df


def _get_country_mapping(df: pd.DataFrame) -> dict[str, str]:

    df = df[[AFFIL_RAW, COUNTRY]].dropna()
    df = df.drop_duplicates()
    mapping: dict[str, str] = pd.Series(
        df[COUNTRY].values, index=df[AFFIL_RAW]
    ).to_dict()
    return mapping


def _get_organization_mapping(df: pd.DataFrame) -> dict[str, str]:

    df = df[[AFFIL_RAW, ORG]].dropna()
    df = df.drop_duplicates()
    mapping: dict[str, str] = pd.Series(df[ORG].values, index=df[AFFIL_RAW]).to_dict()
    return mapping


def _create_country_column(
    df: pd.DataFrame, country_mapping: dict[str, str]
) -> pd.DataFrame:

    df = df.copy()

    df[COUNTRY] = df[AFFIL_RAW].copy()
    df[COUNTRY] = df[COUNTRY].fillna("[N/A]")
    df[COUNTRY] = df[COUNTRY].str.split("; ")
    df[COUNTRY] = df[COUNTRY].apply(
        lambda affils: [country_mapping.get(affil, "[N/A]") for affil in affils],
    )
    df[CorpusField.COUNTRY_AUTH_FIRST.value] = df[COUNTRY].map(
        lambda countries: countries[0] if countries else "[N/A]",
    )
    df[COUNTRY] = df[COUNTRY].apply(set)
    df[COUNTRY] = df[COUNTRY].str.join("; ")

    return df


def _create_organization_column(
    df: pd.DataFrame, organization_mapping: dict[str, str]
) -> pd.DataFrame:
    df = df.copy()

    df[ORG] = df[AFFIL_RAW].copy()
    df[ORG] = df[ORG].fillna("[N/A]")
    df[ORG] = df[ORG].str.split("; ")
    df[ORG] = df[ORG].apply(
        lambda affils: [organization_mapping.get(affil, "[N/A]") for affil in affils]
    )
    df[ORG_AUTH_FIRST] = df[ORG].map(lambda orgs: orgs[0] if orgs else "[N/A]")
    df[ORG] = df[ORG].str.join("; ")

    return df


def _create_thesaurus(
    root_directory: str,
    dataframe: pd.DataFrame,
    mapping: dict[str, str],
    filename: str,
) -> None:

    dataframe = pd.DataFrame(
        {
            "key": list(mapping.values()),
            "label": list(mapping.keys()),
        }
    )
    groupby_df = dataframe.groupby("key", as_index=False)["label"].apply(list)

    filepath = Path(root_directory) / "refine" / "thesaurus" / filename
    with open(filepath, "w", encoding="utf-8") as file:
        for _, row in groupby_df.iterrows():
            key = row["key"]
            file.write(f"{key}\n")
            for value in sorted(row["label"]):
                file.write(f"    {value}\n")


def _assign_country_code(df: pd.DataFrame) -> pd.Series:

    df = df.copy()

    country_to_alpha3 = load_builtin_mapping("country_to_alpha3.json")
    df[ORG] += df[COUNTRY].map(
        lambda country: f" [{country_to_alpha3.get(country, 'N/A')}]"
    )
    return df[ORG]


def _create_thesaurus_columns(
    df: pd.DataFrame,
    country_mapping: dict[str, str],
    organization_mapping: dict[str, str],
) -> pd.DataFrame:

    df = df.copy()

    df[COUNTRY_AND_AFFIL] = df.apply(
        lambda row: (
            "; ".join(
                f"{country_mapping.get(affil, '[N/A]')} @ {affil}"
                for affil in row[AFFIL_RAW].split("; ")
            )
            if pd.notna(row[AFFIL_RAW])
            else "[N/A]"
        ),
        axis=1,
    )

    df[ORG_AND_AFFIL] = df.apply(
        lambda row: (
            "; ".join(
                f"{organization_mapping.get(affil, '[N/A]')} @ {affil}"
                for affil in row[AFFIL_RAW].split("; ")
            )
            if pd.notna(row[AFFIL_RAW])
            else "[N/A]"
        ),
        axis=1,
    )

    return df


def _create_country_thesaurus_file(
    root_directory: str, dataframe: pd.DataFrame
) -> None:

    dataframe = dataframe[[COUNTRY_AND_AFFIL]].copy().dropna()
    dataframe[COUNTRY_AND_AFFIL] = dataframe[COUNTRY_AND_AFFIL].str.split("; ")
    dataframe = dataframe.explode(COUNTRY_AND_AFFIL)
    dataframe[COUNTRY_AND_AFFIL] = dataframe[COUNTRY_AND_AFFIL].str.strip()
    dataframe["country"] = dataframe[COUNTRY_AND_AFFIL].apply(
        lambda x: x.split(" @ ")[0].strip() if " @ " in x else "[N/A]"
    )
    dataframe["affil"] = dataframe[COUNTRY_AND_AFFIL].apply(
        lambda x: x.split(" @ ")[1].strip() if " @ " in x else "[N/A]"
    )
    # counting = dataframe["affil"].value_counts()

    # dataframe["affil"] = dataframe["affil"].apply(
    #     lambda x: f"{x} # occ: {counting.get(x, 0)}"
    # )

    dataframe = dataframe[["country", "affil"]]
    groupby_df = dataframe.groupby("country", as_index=False).agg({"affil": list})
    groupby_df["affil"] = groupby_df["affil"].apply(sorted)
    groupby_df = groupby_df.sort_values(by=["country"], ascending=True)

    filepath = Path(root_directory) / "refine" / "thesaurus" / "countries.the.txt"

    with open(filepath, "w", encoding="utf-8") as file:
        for _, row in groupby_df.iterrows():
            country = row["country"]
            if country == "[N/A]":
                continue
            file.write(f"{country}\n")
            for affil in row["affil"]:
                file.write(f"    {affil}\n")


def _create_organizations_thesaurus_file(
    root_directory: str, dataframe: pd.DataFrame
) -> None:

    dataframe = dataframe[[ORG_AND_AFFIL]].copy().dropna()
    dataframe[ORG_AND_AFFIL] = dataframe[ORG_AND_AFFIL].str.split("; ")
    dataframe = dataframe.explode(ORG_AND_AFFIL)
    dataframe[ORG_AND_AFFIL] = dataframe[ORG_AND_AFFIL].str.strip()
    dataframe["organization"] = dataframe[ORG_AND_AFFIL].apply(
        lambda x: x.split(" @ ")[0].strip() if " @ " in x else "[N/A]"
    )
    dataframe["affil"] = dataframe[ORG_AND_AFFIL].apply(
        lambda x: x.split(" @ ")[1].strip() if " @ " in x else "[N/A]"
    )
    # counting = dataframe["affil"].value_counts()

    # dataframe["affil"] = dataframe["affil"].apply(
    #     lambda x: f"{x} # occ: {counting.get(x, 0)}"
    # )

    dataframe = dataframe[["organization", "affil"]]
    groupby_df = dataframe.groupby("organization", as_index=False).agg({"affil": list})
    groupby_df["affil"] = groupby_df["affil"].apply(sorted)
    groupby_df = groupby_df.sort_values(by=["organization"], ascending=True)

    filepath = Path(root_directory) / "refine" / "thesaurus" / "organizations.the.txt"

    with open(filepath, "w", encoding="utf-8") as file:
        for _, row in groupby_df.iterrows():
            organization = row["organization"]
            if organization == "[N/A]":
                continue
            file.write(f"{organization}\n")
            for affil in row["affil"]:
                file.write(f"    {affil}\n")


def extract_organizations_and_countries(root_directory: str) -> int:

    dataframe = load_main_data(root_directory=root_directory)

    affil_df = _get_affiliations_df(dataframe)
    affil_df[COUNTRY] = affil_df[AFFIL_RAW].apply(_extract_country_from_string)
    affil_df[ORG] = affil_df[AFFIL_RAW].apply(_extract_organization_from_string)

    affil_df[ORG] = _assign_country_code(affil_df)

    country_mapping = _get_country_mapping(affil_df)
    organization_mapping = _get_organization_mapping(affil_df)

    dataframe = _create_country_column(dataframe, country_mapping)
    dataframe = _create_organization_column(dataframe, organization_mapping)
    dataframe = _create_thesaurus_columns(
        dataframe, country_mapping, organization_mapping
    )

    _create_country_thesaurus_file(root_directory, dataframe)
    _create_organizations_thesaurus_file(root_directory, dataframe)

    save_main_data(df=dataframe, root_directory=root_directory)

    return int(dataframe[CorpusField.AFFIL_RAW.value].notna().sum())
