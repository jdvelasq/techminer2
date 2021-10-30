import re
from os.path import dirname, join

import pandas as pd
from techminer.utils.thesaurus import load_file_as_dict

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


def extract_institution(text):
    #
    if pd.isna(x) or x is None:
        return pd.NA

    module_path = dirname(__file__)
    filename = join(module_path, "../config/institutions.data")
    with open(filename, "r", encoding="utf-8") as file:
        known_institution_names = file.read().splitlines()

    #
    # List of standardized country names
    #
    module_path = dirname(__file__)
    filename = join(module_path, "../config/country_codes.data")
    country_codes = load_file_as_dict(filename)
    country_names = list(country_codes.values())
    country_names = [w[0].lower() for w in country_names]
    country_names_to_codes = {
        item: code for code in country_codes.keys() for item in country_codes[code]
    }

    #
    #
    #
    text = text.lower().strip()

    # known_names = [w.replace("\n", "").lower() for w in known_names]
    # known_names = [w for w in known_names if len(w) > 0]

    return
