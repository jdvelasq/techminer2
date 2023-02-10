"""
Create 'organizations.txt' thesaurus file
===============================================================================

Creates a organizations thesaurus from the data in the database.


>>> directory = "data/regtech/"

>>> from techminer2 import vantagepoint
>>> vantagepoint.refine.create_organizations_thesaurus(directory)
--INFO-- The data/regtech/processed/organizations.txt thesaurus file was created


"""
import os.path
import sys

import pandas as pd

from ..._thesaurus import Thesaurus, load_file_as_dict

SPANISH = [
    "ARG",
    "CHL",
    "COL",
    "CUB",
    "ECU",
    "ESP",
    "GTM",
    "HND",
    "MEX",
    "NIC",
    "PAN",
    "PER",
    "VEN",
]

PORTUGUES = [
    "BRA",
    "PRT",
]

NAMES = [
    "ministry",
    "ministerio",
    #
    "universidad",
    "universidade",
    "universita",
    "universite",
    "universiti",
    "universiteit",
    "university",
    "univerza",
    "unversitat",
    #
    "bank",
    "banco",
    #
    "agency",
    "agencia",
    #
    "council",
    "commission",
    "comision",
    "consejo",
    "consortium",
    #
    "politec",
    "polytechnic",
    "politecnico",
    #
    "hospital",
    #
    "association",
    "asociacion",
    #
    "sociedad",
    "society",
    #
    "consorcio",
    #
    "company",
    "organization",
    #
    "inc.",
    "ltd.",
    "office",
    "oficina",
    "corporation",
    "corporacion",
    #
    "government",
    #
    "fundacion",
    "foundation",
]


def create_organizations_thesaurus(directory="./"):
    """Creates organizations.txt thesaurus file."""

    affiliations = _load_affiliations_from_country_thesaurus(directory)
    affiliations = _convert_countries_to_codes(affiliations)
    affiliations["affiliation"] = affiliations["raw_affiliation"]
    affiliations = _clean_organization_names(affiliations)
    affiliations["organization"] = affiliations["affiliation"]
    affiliations["organization"] = affiliations["organization"].map(
        _select_organization
    )

    _group_and_save(affiliations, directory)


def _select_organization(affiliation):
    """Selects the organization from the affiliation."""

    affiliation = affiliation.split(",")
    affiliation = [a.strip() for a in affiliation]

    # --------------------------------------------------------------------------------
    valid_names = _load_valid_names()
    for name in valid_names:
        for aff in affiliation:
            if name in aff.lower():
                return aff

    # --------------------------------------------------------------------------------
    for aff in affiliation:
        for name in NAMES:
            if name in aff.lower():
                if aff[:4].lower() == "the ":
                    aff = aff.replace("The ", "", 1)
                    return aff
                return aff

    # Regla por defecto: la primera componente de la afiliación
    return "---" + affiliation[0]


def _load_valid_names():
    module_path = os.path.dirname(__file__)
    with open(
        os.path.join(module_path, "../../_files/organizations.txt"),
        "rt",
        encoding="utf-8",
    ) as file:
        valid_names = file.readlines()
    valid_names = [w.replace("\n", "").lower() for w in valid_names]
    return valid_names


def _group_and_save(affiliations, directory):

    affiliations = affiliations[["raw_affiliation", "organization"]]

    grp = affiliations.groupby(by="organization", as_index=False).agg(
        {"raw_affiliation": list}
    )
    th_dict = {k: v for k, v in zip(grp.organization, grp.raw_affiliation)}

    thesaurus_file = os.path.join(directory, "processed", "organizations.txt")

    Thesaurus(
        th_dict,
        ignore_case=False,
        full_match=True,
        use_re=False,
    ).to_textfile(thesaurus_file)

    sys.stdout.write(f"--INFO-- The {thesaurus_file} thesaurus file was created\n")


def _clean_organization_names(affiliations):

    affiliations = affiliations.copy()

    repl = [
        (".", ""),
        ("&", " and "),
        (" aandm ", " a and m "),
        ("The University of ", "University of "),
        (" Univ. Nacional de ", " Universidad Nacional de "),
        (" Univ. de la ", " Universidad de la "),
        (" Univ. del ", " Universidad del "),
        (" Univ. do ", " Universidade do "),
        (" Univ. of ", " University of "),
        (" Univ,", " University,"),
        (" U. de ", " Universidad de "),
        ("'", ""),
        ('"', ""),
        ("“", ""),
        ("”", ""),
        ("’", ""),
        ("-", " "),
        (" UNAM,", " Universidad Nacional Autonoma de Mexico,"),
    ]
    for pattern, text in repl:
        affiliations["affiliation"] = affiliations["affiliation"].str.replace(
            pattern, text, regex=False
        )

    affiliations["affiliation"] = affiliations["affiliation"].str.replace(
        r"\([A-Za-z\-]+\)", "", regex=True
    )
    affiliations["affiliation"] = affiliations["affiliation"].str.strip()

    return affiliations


def _load_affiliations_from_country_thesaurus(directory):

    file_name = os.path.join(directory, "processed", "countries.txt")
    th_dict = load_file_as_dict(file_name)
    country = [k for k, v in th_dict.items() for t in v]
    aff = [t for k, v in th_dict.items() for t in v]

    affiliations = pd.DataFrame(
        {
            "raw_affiliation": aff,
            "country": country,
        }
    )
    return affiliations


def _convert_countries_to_codes(affiliations):

    module_path = os.path.dirname(__file__)
    filename = os.path.join(module_path, "../../_files/country_codes.txt")
    codes_dict = load_file_as_dict(filename)
    codes_dict = {t: k for k, v in codes_dict.items() for t in v}

    affiliations["country"] = affiliations["country"].str.lower()
    affiliations["country"] = affiliations["country"].map(codes_dict)
    return affiliations
