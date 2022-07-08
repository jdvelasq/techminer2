"""
Create Country Thesaurus
===============================================================================

Creates a country thesaurus from 'affiliations' column in the datasets.

>>> from techminer2.create_country_thesaurus import create_country_thesaurus
>>> directory = "data/regtech/"

# >>> directory = "data/dyna-colombia/"

>>> create_country_thesaurus(directory)

"""
import glob
import os.path
import re

import pandas as pd

from .thesaurus import Thesaurus, load_file_as_dict


def create_country_thesaurus(directory):
    """Creates a country thesaurus from 'affiliations' column in the datasets."""

    country_names = _get_country_names()
    country_names = [r"\b" + name + r"\b" for name in country_names]
    country_names_as_regex = "|".join(country_names)
    country_names_as_regex = country_names_as_regex.lower()

    affiliations = _load_affiliations(directory)
    affiliations = affiliations.dropna()
    affiliations = affiliations.str.split(";")
    affiliations = affiliations.explode()
    affiliations = affiliations.str.strip()
    affiliations = affiliations.drop_duplicates()

    affiliations = pd.DataFrame({"affiliation": affiliations.tolist()})
    affiliations = affiliations.assign(country=affiliations.affiliation)
    affiliations = affiliations.assign(country=affiliations.country.str.split(","))
    affiliations = affiliations.assign(
        country=affiliations.country.map(lambda x: x[-1])
    )

    affiliations = affiliations.assign(country=affiliations.country.str.lower())

    affiliations = _replace_sinonimous(affiliations, "country")

    affiliations["country"] = affiliations["country"].map(
        lambda x: re.search(country_names_as_regex, x)
    )
    affiliations["country"] = affiliations["country"].map(
        lambda x: x.group(0) if x is not None else "unknown"
    )

    affiliations["country"] = affiliations["country"].str.title()
    affiliations["country"] = affiliations["country"].str.replace(" And ", " and ")
    affiliations["country"] = affiliations["country"].str.replace(" Of ", " of ")
    affiliations["country"] = affiliations["country"].str.replace("Unknown", "[UKN]")

    countries_dict = affiliations.groupby(by="country").agg({"affiliation": list})
    countries_dict = {
        key: sorted(items)
        for key, items in zip(countries_dict.index, countries_dict.affiliation)
    }

    thesarurus = Thesaurus(
        x=countries_dict,
    )
    output_file = os.path.join(directory, "processed", "countries.txt")
    thesarurus.to_textfile(output_file)


def _replace_sinonimous(affiliations, column):
    affiliations = affiliations.copy()
    for text_to_replace, new_text in [
        ("bosnia and herz.", "bosnia and herzegovina"),
        ("brasil", "brazil"),
        ("czech republic", "czechia"),
        ("espana", "spain"),
        ("macao", "china"),
        ("macau", "china"),
        ("n. cyprus", "cyprus"),
        ("peoples r china", "china"),
        ("rusia", "russia"),
        ("russian federation", "russia"),
        ("syrian arab republic", "syria"),
        ("united states of america", "united states"),
        ("usa", "united states"),
        ("viet-nam", "vietnam"),
        ("viet nam", "vietnam"),
    ]:
        affiliations[column] = affiliations[column].str.replace(
            text_to_replace,
            new_text,
        )

    return affiliations


def _load_affiliations(directory):

    affiliations = []
    files = list(glob.glob(os.path.join(directory, "processed/_*.csv")))
    for file in files:
        data = pd.read_csv(file, encoding="utf-8")
        if "affiliations" in data.columns:
            affiliations += data.affiliations.tolist()
    if len(affiliations) == 0:
        raise ValueError(
            "Column 'affiliations' do not exists in any database or it is empty."
        )
    return pd.Series(affiliations)


def _get_country_names():

    module_path = os.path.dirname(__file__)
    file_name = os.path.join(module_path, "files", "country_codes.txt")
    country_codes = load_file_as_dict(file_name)
    country_names = list(country_codes.values())
    country_names = [name.lower() for w in country_names for name in w]
    return country_names
