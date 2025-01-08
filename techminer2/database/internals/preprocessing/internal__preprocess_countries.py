# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Create countries thesaurus from affiliations.

# >>> from techminer2.ingest._list_cleanup_countries import list_cleanup_countries
# >>> list_cleanup_countries(  # doctest: +SKIP
# ...     #
# ...     # DATABASE PARAMS:
# ...     root_dir="example/",
# ... )
# --INFO-- The example/thesauri/countries.the.txt thesaurus file was created

"""

import pathlib

import pandas as pd  # type: ignore
import pkg_resources  # type: ignore

from ....prepare.thesaurus.countries.apply_thesaurus import (
    apply_thesaurus as apply_countries_thesaurus,
)


def internal__preprocess_countries(root_dir):
    """:meta private:"""

    affiliations = load_affiliations_frame(root_dir)
    affiliations = copy_affiliations_to_contry_column(affiliations)
    affiliations = extract_country_component(affiliations)
    affiliations = homogenize_country_names(affiliations)
    affiliations = check_country_names(affiliations)

    save_countries_thesaurus(affiliations, root_dir)
    apply_countries_thesaurus(root_dir)

    print(
        f"--INFO-- The {pathlib.Path(root_dir) / 'thesauri/countries.the.txt'} thesaurus file was created"
    )


def load_affiliations_frame(root_dir):
    """Loads the 'affiliations' column from the datasets."""

    dataframe = pd.read_csv(
        pathlib.Path(root_dir) / "databases/database.csv.zip",
        encoding="utf-8",
        compression="zip",
    )

    if "affiliations" not in dataframe.columns:
        raise ValueError(
            "Column 'affiliations' do not exists in any databases or it is empty."
        )

    affiliations = dataframe.affiliations
    affiliations = affiliations.dropna()
    affiliations = affiliations.str.split(";")
    affiliations = affiliations.explode()
    affiliations = affiliations.str.strip()
    affiliations = affiliations.drop_duplicates()

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
    affiliations["country"] = affiliations["country"].str.split(",").str[-1].str.strip()
    return affiliations


def homogenize_country_names(affiliations):
    """Fix variations in country names."""

    replacements = [
        ("Bosnia and Herz.", "Bosnia and Herzegovina"),
        ("Brasil", "Brazil"),
        ("Czech Republic", "Czechia"),
        ("Espana", "Spain"),
        ("Macao", "China"),
        ("Macau", "China"),
        ("N. Cyprus", "Cyprus"),
        ("Peoples R China", "China"),
        ("Rusia", "Russia"),
        ("Russian Federation", "Russia"),
        ("Syrian Arab Republic", "Syria"),
        ("United States of America", "United States"),
        ("USA", "United States"),
        ("Viet-Nam", "Vietnam"),
        ("Viet Nam", "Vietnam"),
    ]

    #
    # Replaces the names in affiliations
    affiliations = affiliations.copy()
    for pat, repl in replacements:
        affiliations["country"] = affiliations["country"].str.replace(
            pat, repl, regex=False
        )

    #
    # Returns the affiliations with the fixed country names
    return affiliations


def check_country_names(affiliations):
    """Extract the country based on a regex."""

    #
    # Loads country names from thesaurus
    file_path = pkg_resources.resource_filename(
        "techminer2",
        "package_data/thesaurus/geography/alpha3-to-country.the.txt",
    )
    countries = []
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            if line.startswith(" "):
                countries.append(line.strip())

    #
    # Checks country names
    affiliations = affiliations.copy()
    affiliations["country"] = affiliations["country"].map(
        lambda x: x if x in countries else "[UNKNWON]"
    )
    return affiliations


def save_countries_thesaurus(affiliations, root_dir):
    """Saves the thesaurus."""

    #
    # Groups affiliations by country
    affiliations = affiliations.copy()
    affiliations = affiliations.sort_values(["country", "affiliations"])
    affiliations = affiliations.groupby("country", as_index=False).agg(
        {"affiliations": list}
    )

    #
    # Creates the thesaurus
    file_path = pathlib.Path(root_dir) / "thesauri/countries.the.txt"
    with open(file_path, "w", encoding="utf-8") as file:
        for _, row in affiliations.iterrows():
            file.write(row.country + "\n")
            for aff in row.affiliations:
                file.write("    " + aff + "\n")
