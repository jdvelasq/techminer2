"""
Create Country Thesaurus
===============================================================================

Creates a country thesaurus from 'affiliations' column in the datasets.



"""
import glob
import os.path
import re

import pandas as pd

from .thesaurus import Thesaurus, load_file_as_dict


def create_country_thesaurus(directory):
    """Creates a country thesaurus from 'affiliations' column in the datasets."""

    country_names = _get_country_names()
    country_names_as_regex = "|".join(country_names)
    country_names_as_regex = country_names_as_regex.lower()

    affiliations = _load_affiliations(directory)
    affiliations = affiliations.dropna()
    affiliations = affiliations.str.split(";")
    affiliations = affiliations.explode()
    affiliations = affiliations.str.strip()
    affiliations = affiliations.drop_duplicates()

    affiliations = pd.DataFrame({"key": affiliations.tolist()})
    affiliations = affiliations.assign(text=affiliations.key)
    affiliations = affiliations.assign(key=affiliations.key.str.lower())
    affiliations = _replace_sinonimous(affiliations)

    affiliations["key"] = affiliations["key"].map(
        lambda x: re.search(country_names_as_regex, x)
    )
    affiliations["key"] = affiliations["key"].map(
        lambda x: x.group(0) if x is not None else "unknown"
    )

    affiliations["key"] = affiliations["key"].str.title()
    affiliations["key"] = affiliations["key"].str.replace(" And ", " and ")
    affiliations["key"] = affiliations["key"].str.replace(" Of ", " of ")
    affiliations["key"] = affiliations["key"].str.replace("Unknown", "[UNKNOWN]")

    countries_dict = affiliations.groupby(by="key").agg({"text": list})
    countries_dict = {
        key: items for key, items in zip(countries_dict.index, countries_dict.text)
    }

    thesarurus = Thesaurus(
        x=countries_dict,
    )
    output_file = os.path.join("data", "processed", "countries.txt")
    thesarurus.to_textfile(output_file)


def _replace_sinonimous(affiliations):
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
        affiliations = affiliations.assign(
            key=affiliations.key.str.replace(
                text_to_replace,
                new_text,
            )
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
