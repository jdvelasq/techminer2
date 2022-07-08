"""
Create institutions thesaurus
===============================================================================

Creates a institutions thesaurus from the data in the database.

>>> from techminer2 import *
>>> directory = "data/regtech/"

>>> x = create_institutions_thesaurus(directory)
>>> x[x.institution.isna()]


# >>> apply_institutions_thesaurus(directory)
--INFO-- Applying thesaurus to institutions
--INFO-- The thesaurus was applied to institutions in all databases

"""

import glob
import os.path
import sys

import pandas as pd

from .thesaurus import load_file_as_dict

#
# The algorithm searches in order until detect a match
#
NAMES = [
    "ministry",
    "national",
    "univ ",
    "unisversidade",
    "univerza",
    "univerrsity",
    "universidad",
    "universidade",
    "universita",
    "universitas",
    "universitat",
    "universite",
    "universiteit",
    "university",
    "univesity",
    "univesrity",
    "unversitat",
    "universiti",
    "institut",
    "instituto",
    "college",
    "colegio",
    "bank",
    "banco",
    "centre",
    "center",
    "centro",
    "agency",
    "agencia",
    "council",
    "commission",
    "comision",
    "consejo",
    "politec",
    "polytechnic",
    "politecnico",
    "department",
    "direction",
    "laboratory",
    "laboratoire",
    "laboratorio",
    "school",
    "skola",
    "scuola",
    "ecole",
    "escuela",
    "hospital",
    "association",
    "asociacion",
    "company",
    "organization",
    "academy",
    "academia",
    "tecnologico",
    "empresa",
    "inc.",
    "ltd.",
    "office",
    "oficina",
    "corporation",
    "corporacion",
    "ministerio",
    "technologies",
    "unidad",
    "tecnologico",
    "consorcio",
    "autoridad",
    "compania",
    "sociedad",
    "servicio",
    "government",
    "institute",
    "sociedad",
    "society",
]

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


def create_institutions_thesaurus(directory="./"):
    """Creates an insitutions thesaurus."""

    affiliations = _load_affiliations_from_country_thesaurus(directory)
    affiliations = _convert_countries_to_codes(affiliations)
    affiliations["institution"] = affiliations["affiliation"].map(_select_institution)

    return affiliations


###
def _select_institution(affiliation):
    # affiliation es un string con cada afiliacion completa separada por comas

    affiliation = affiliation.split(",")
    affiliation = [a.strip() for a in affiliation]
    for aff in affiliation:
        if "univers" in aff.lower():
            return aff

    #
    #
    #
    return pd.NA


def _get_list_of_countries():
    pass


def _load_affiliations_from_country_thesaurus(directory):

    file_name = os.path.join(directory, "processed", "countries.txt")
    th_dict = load_file_as_dict(file_name)
    affiliations = pd.DataFrame(
        {
            "affiliation": th_dict.values(),
            "country": th_dict.keys(),
        }
    )
    affiliations["affiliation"] = affiliations["affiliation"].map(lambda x: x[0])
    return affiliations


def _convert_countries_to_codes(affiliations):

    module_path = os.path.dirname(__file__)
    filename = os.path.join(module_path, "files/country_codes.txt")
    codes_dict = load_file_as_dict(filename)
    codes_dict = {t: k for k, v in codes_dict.items() for t in v}

    affiliations["country"] = affiliations["country"].str.lower()
    affiliations["country"] = affiliations["country"].map(codes_dict)
    return affiliations
