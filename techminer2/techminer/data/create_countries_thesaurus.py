"""
Create Country Thesaurus
===============================================================================

Creates a country thesaurus from 'affiliations' column in the datasets.

>>> from techminer2 import techminer
>>> root_dir = "data/regtech/"

>>> techminer.data.create_countries_thesaurus(root_dir)
--INFO-- The data/regtech/processed/countries.txt thesaurus file was created


"""
import glob
import os.path
import pathlib
import re

import pandas as pd
import requests  # type: ignore


def create_countries_thesaurus(root_dir):
    """Creates a countries thesaurus."""

    affiliations = load_affiliations_frame(root_dir)
    affiliations = copy_affiliations_to_contry_column(affiliations)
    affiliations = extract_country_component(affiliations)
    affiliations = fix_country_names(affiliations)
    country_codes = get_country_codes()
    country_names = get_country_names(country_codes)
    regex = country_names_to_regex(country_names)
    affiliations = extract_country_name_from_regex(
        affiliations, regex, country_names
    )
    affiliations = format_country_names(affiliations)
    save_countries_thesaurus(affiliations, root_dir)
    print(
        f"--INFO-- The {pathlib.Path(root_dir) / 'processed/countries.txt'} "
        "thesaurus file was created"
    )


def load_affiliations_frame(directory):
    """Loads the 'affiliations' column from the datasets."""

    affiliations = []

    files = list(glob.glob(os.path.join(directory, "processed/_*.csv")))
    for file in files:
        data = pd.read_csv(file, encoding="utf-8")
        if "affiliations" in data.columns:
            affiliations.append(
                data.affiliations.dropna()
                .drop_duplicates()
                .str.split(";")
                .explode()
                .str.strip()
                .drop_duplicates()
            )
    affiliations = pd.concat(affiliations).drop_duplicates()

    if len(affiliations) == 0:
        raise ValueError(
            "Column 'affiliations' do not exists in any databases "
            "or it is empty."
        )

    frame = pd.DataFrame({"affiliations": affiliations})

    return frame


def copy_affiliations_to_contry_column(affiliations):
    """Copies the 'affiliations' column to the 'country' column."""

    affiliations = affiliations.copy()
    affiliations = affiliations.assign(country=affiliations.affiliations)
    return affiliations


def extract_country_component(affiliations):
    """Extracts the country component from the 'country' column."""

    affiliations = affiliations.copy()
    affiliations["country"] = (
        affiliations["country"].str.lower().str.split(",").str[-1].str.strip()
    )
    return affiliations


def fix_country_names(affiliations):
    """Fix variations in country names."""

    affiliations = affiliations.copy()

    owner = "jdvelasq"
    repo = "techminer2"
    path = "settings/country_replace.csv"
    url = f"https://raw.githubusercontent.com/{owner}/{repo}/main/{path}"

    repl = pd.read_csv(url)
    for _, row in repl.iterrows():
        affiliations["country"] = affiliations["country"].str.replace(
            row.pat, row.repl, regex=False
        )

    return affiliations


def get_country_codes():
    """Gets the regex from the settings file."""

    owner = "jdvelasq"
    repo = "techminer2"
    path = "settings/country_codes.txt"
    url = f"https://raw.githubusercontent.com/{owner}/{repo}/main/{path}"

    response = requests.get(url, timeout=5)
    return response.text


def get_country_names(country_codes):
    """Gets the regex from the text."""

    country_codes = country_codes.split("\n")

    countries = []
    for line in country_codes:
        if line[0] == " ":
            countries.append(line.strip())

    return countries


def country_names_to_regex(country_names):
    """Converts country names to regex."""

    return r"(" + "|".join(country_names[1:]).lower() + r")"


def extract_country_name_from_regex(affiliations, regex, country_names):
    """Extract the country based on a regex."""

    affiliations = affiliations.copy()
    affiliations["country"] = affiliations["country"].map(
        lambda x: re.search(regex, x)
    )
    affiliations["country"] = affiliations["country"].map(
        lambda x: x.group(0) if x is not None else "unknown"
    )
    affiliations["country"] = affiliations["country"].map(
        lambda x: x if x in country_names else "[UKNOW]"
    )
    return affiliations


def format_country_names(affiliations):
    """Formats the country names."""

    affiliations = affiliations.copy()
    affiliations["country"] = (
        affiliations["country"]
        .str.title()
        .str.replace(" And ", " and ")
        .str.replace(" Of ", " of ")
    )
    return affiliations


def save_countries_thesaurus(affiliations, root_dir):
    """Saves the thesaurus."""

    affiliations = affiliations.copy()

    existent_affiliations = read_existent_coutries_txt_thesaurus(root_dir)

    if existent_affiliations is not None:
        affiliations = pd.concat(
            [existent_affiliations, affiliations], ignore_index=True
        )
        affiliations = affiliations.drop_duplicates(subset=["affiliations"])
        affiliations = affiliations.reset_index(drop=True)

    affiliations = affiliations.sort_values(["country", "affiliations"])
    affiliations = affiliations.groupby("country", as_index=False).agg(
        {"affiliations": list}
    )

    file_path = pathlib.Path(root_dir) / "processed/countries.txt"

    with open(file_path, "w", encoding="utf-8") as file:
        for _, row in affiliations.iterrows():
            file.write(row.country + "\n")
            for aff in row.affiliations:
                file.write("    " + aff + "\n")


def read_existent_coutries_txt_thesaurus(root_dir):
    """Read the existent thesaurus if exists."""
    file_path = pathlib.Path(root_dir) / "processed/countries.txt"

    country = None
    countries = []
    affiliations = []

    if not file_path.exists():
        return None

    # collects the countries and the respective affiliations
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            if not line.startswith(" "):
                country = line.strip()
            else:
                affiliation = line.strip()
                countries.append(country)
                affiliations.append(affiliation)

    frame = pd.DataFrame(
        {
            "affiliations": affiliations,
            "country": countries,
        }
    )

    return frame
