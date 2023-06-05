# flake8: noqa
"""
Create 'organizations.txt' thesaurus file 
===============================================================================

Creates a organizations thesaurus from the data in the database.


>>> root_dir = "data/regtech/"

>>> from techminer2 import techminer
>>> techminer.data.create_organizations_thesaurus(root_dir)
--INFO-- The data/regtech/processed/organizations.txt thesaurus file was created


"""
import pathlib
import re

import pandas as pd
import requests  # type: ignore


def create_organizations_thesaurus(root_dir="./"):
    """Creates organizations.txt thesaurus file."""

    frame = load_affiliations_from_country_thesaurus(root_dir)
    frame = add_country_code_column(frame)
    frame = add_candidate_organization_column(frame)
    frame = clean_candidate_organization_column(frame)
    knwon_orgs = load_known_orgs()
    frame = assigns_from_kwown_organizations(frame, knwon_orgs)
    frame = assings_names_by_priority(frame)
    frame = format_organization_names(frame)
    save_organizations_thesaurus(frame, root_dir)
    print(
        f"--INFO-- The {pathlib.Path(root_dir) / 'processed/organizations.txt'} "
        "thesaurus file was created"
    )


def load_affiliations_from_country_thesaurus(root_dir):
    """Loads data from countries.txt file."""

    file_path = pathlib.Path(root_dir) / "processed/countries.txt"

    country = None
    countries = []
    affiliations = []

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
            "raw_affiliation": affiliations,
            "country": countries,
        }
    )
    return frame


def add_country_code_column(frame):
    """Add 'code' column to the frame."""

    owner = "jdvelasq"
    repo = "techminer2"
    path = "settings/country_codes.txt"
    url = f"https://raw.githubusercontent.com/{owner}/{repo}/main/{path}"

    response = requests.get(url, timeout=5)
    country_codes = response.text.split("\n")

    countries = []
    codes = []
    code = None
    for line in country_codes:
        if line[0] != " ":
            code = line.strip()
        else:
            countries.append(line.strip())
            codes.append(code)

    frame = frame.copy()
    frame["code"] = "unknown"
    for country, code in zip(countries, codes):
        frame.loc[frame.country.str.lower() == country.lower(), "code"] = code

    return frame


def add_candidate_organization_column(frame):
    """Adds raw candidate organizations.

    The raw candidate organizations are the two first components
    of the raw affiliations in lower case.

    """
    frame = frame.copy()
    frame["organization"] = frame.raw_affiliation
    return frame


def clean_candidate_organization_column(frame):
    """Cleans the candidate organizations column."""

    owner = "jdvelasq"
    repo = "techminer2"
    path = "settings/organizations_abbr.csv"
    url = f"https://raw.githubusercontent.com/{owner}/{repo}/main/{path}"

    repl_frame = pd.read_csv(url)
    frame = frame.copy()

    for pat, repl in [
        ('"', ""),
        (".", ""),
        ("“", ""),
        ("”", ""),
        ("’", ""),
        # ("-", " "),
    ]:
        frame["organization"] = frame["organization"].str.replace(
            pat, repl, regex=False
        )

    for _, row in repl_frame.iterrows():
        frame["organization"] = frame["organization"].str.replace(
            r"\b" + row.pat + r"\b", row.repl, regex=True
        )

    frame["organization"] = frame["organization"].str.strip()

    return frame


def add_a_empty_organization_column(frame):
    """Adds empty organizations."""

    frame = frame.copy()
    frame["organizations"] = pd.NA
    return frame


def load_known_orgs():
    """Loads known organizations from GitHub repo."""

    owner = "jdvelasq"
    repo = "techminer2"
    path = "settings/known_organizations.txt"
    url = f"https://raw.githubusercontent.com/{owner}/{repo}/main/{path}"

    response = requests.get(url, timeout=5)
    known_organizations = response.text.split("\n")
    known_organizations = [org.strip() for org in known_organizations]
    return known_organizations


def assigns_from_kwown_organizations(frame, knwon_orgs):
    """Adds organizations from known organizations."""

    frame = frame.copy()
    for org in knwon_orgs:
        frame.loc[
            frame.raw_affiliation.astype(str).str.contains(org, case=False),
            "organization",
        ] = org
    return frame


# names sorted by proirity
NAMES = [
    "Min",  # ministry, ministerio
    "Univ",  # university, universidad, univedade, ...
    "B",  # bank, banco
    "AG",  # agency, agencia
    "Counc",  # council, concilio, consejo
    "Conc",  # concilio, consejo
    "Com",  # comission, comision
    "Consortium",
    "Politec",  # polytechnic, politecnico
    "Hosp",  # hospital
    "Assn",  # association
    "Asoc",  # asociacion
    "Soc",
    "Consor",
    "Co",
    "Org",
    "Inc",
    "Ltd",
    "Off",
    "Corp",
    "Gob",
    "Gov",
    "Found",
    "Fund",
    "Inst",
    "Coll",
    "Sch",
]


def assings_names_by_priority(frame):
    """Assigns the organization name by priority."""

    def select_name(affiliation):
        for name in NAMES:
            regex = r"\b" + name + r"\b"

            if re.search(regex, affiliation, re.IGNORECASE):
                parts = affiliation.split(",")
                for part in parts:
                    if re.search(regex, part, re.IGNORECASE):
                        return part.strip()
        return affiliation

    #
    # Main code:
    #
    frame = frame.copy()
    for index, row in frame.iterrows():
        if row.organization is pd.NA:
            frame.loc[index, "organization"] = select_name(
                frame.loc[index, "affiliation"]
            )

    frame["organization"] = frame["organization"].map(select_name)
    return frame


def format_organization_names(frame):
    """Formats the organization names."""

    frame = frame.copy()
    frame["organization"] = (
        frame["organization"].astype(str) + " (" + frame["code"] + ")"
    )
    return frame

    # frame["organization"] = (
    #     frame["organization"]
    #     .str.title()
    #     .str.replace(" Of ", " of ")
    #     .str.replace(" And ", " and ")
    #     .str.replace(" For ", " for ")
    # )

    # return frame


def save_organizations_thesaurus(frame, root_dir):
    """Saves the thesaurus."""

    frame = frame.copy()

    existent_organizations = read_existent_organizations_txt_thesaurus(
        root_dir
    )

    if existent_organizations is not None:
        frame = pd.concat([existent_organizations, frame], ignore_index=True)
        frame = frame.drop_duplicates(subset=["raw_affiliation"])
        frame = frame.reset_index(drop=True)

    ##
    frame = frame.sort_values(["organization", "raw_affiliation"])
    frame = frame.groupby("organization", as_index=False).agg(
        {"raw_affiliation": list}
    )

    file_path = pathlib.Path(root_dir) / "processed/organizations.txt"

    with open(file_path, "w", encoding="utf-8") as file:
        for _, row in frame.iterrows():
            file.write(row.organization + "\n")
            for aff in row.raw_affiliation:
                file.write("    " + aff + "\n")


def read_existent_organizations_txt_thesaurus(root_dir):
    """Read the existent thesaurus if exists."""
    file_path = pathlib.Path(root_dir) / "processed/organizations.txt"

    organization = None
    organizations = []
    affiliations = []

    if not file_path.exists():
        return None

    # collects the countries and the respective affiliations
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            if not line.startswith(" "):
                organization = line.strip()
            else:
                affiliation = line.strip()
                organizations.append(organization)
                affiliations.append(affiliation)

    frame = pd.DataFrame(
        {
            "raw_affiliation": affiliations,
            "organization": organizations,
        }
    )

    return frame
