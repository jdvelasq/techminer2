"""
Extract country
===============================================================================

Creates a country list from a column.



"""
import glob
import os
import re

import pandas as pd

from .thesaurus import load_file_as_dict


def extract_country(directory, input_col, output_col):
    """Extracts country names from the datasets"""

    #
    country_names = _get_country_names()
    country_names_as_regex = "|".join(country_names)
    country_names_as_regex = country_names_as_regex.lower()

    #
    files = list(glob.glob(os.path.join(directory, "processed/_*.csv")))
    for file in files:
        data = pd.read_csv(file, encoding="utf-8")
        #
        if input_col in data.columns:
            data[output_col] = data[input_col].copy()
            #
            data[output_col] = data[output_col].str.lower()
            for text_to_replace, new_text in [
                ("bosnia and herz.", "bosnia and herzegovina"),
                ("brasil", "brazil"),
                ("czechia", "czech republic"),
                ("espana", "spain"),
                ("macao", "china"),
                ("macau", "china"),
                ("peoples r china", "china"),
                ("rusia", "russia"),
                ("russian federation", "russia"),
                ("united states of america", "united states"),
                ("usa", "united states"),
            ]:
                data[output_col] = data[output_col].str.replace(
                    text_to_replace,
                    new_text,
                )
            #
            data[output_col] = data[output_col].str.split(";")
            data[output_col] = data[output_col].map(
                lambda x: [re.search(country_names_as_regex, y) for y in x]
                if isinstance(x, list)
                else x
            )
            data[output_col] = data[output_col].map(
                lambda x: [y.group(0) for y in x if y is not None]
                if isinstance(x, list)
                else x
            )

            data[output_col] = data[output_col].map(
                lambda x: [y for y in x if not pd.isna(y)] if isinstance(x, list) else x
            )
            data[output_col] = data[output_col].str.join("; ")
            data[output_col] = data[output_col].map(lambda x: pd.NA if x == "" else x)
            data[output_col] = data[output_col].str.title()
            data[output_col] = data[output_col].str.replace(" Of ", " of ")
            data[output_col] = data[output_col].str.replace(" And ", " and ")

        #
        data.to_csv(file, sep=",", encoding="utf-8", index=False)


def _get_country_names():

    module_path = os.path.dirname(__file__)
    file_name = os.path.join(module_path, "files", "country_codes.txt")
    country_codes = load_file_as_dict(file_name)
    country_names = list(country_codes.values())
    country_names = [name.lower() for w in country_names for name in w]
    return country_names


###################################################################################################


NAMES = [
    ("universidad del norte", "colombia"),
    ("universidad nacional de colombia", "colombia"),
    ("universidad de antioquia", "colombia"),
    ("universidad industrial de santander", "colombia"),
    ("universidad del valle", "colombia"),
    ("universidad del cauca", "colombia"),
    ("instituto tecnologico metropolitano", "colombia"),
]


def extract_country_from_string(x):
    """
    Extracts a country name from a string.
    """
    #
    if pd.isna(x) or x is None:
        return pd.NA

    # List of standardized country names
    #
    module_path = os.path.dirname(__file__)
    filename = os.path.join(module_path, "files/country_codes.txt")
    country_codes = load_file_as_dict(filename)
    country_names = list(country_codes.values())
    country_names = [name.lower() for w in country_names for name in w]

    ##
    ## Replace administrative regions by country names
    ## for the current string
    ##
    x = x.lower()
    x = x.strip()
    for a, b in [
        ("bosnia and herzegovina", "bosnia and herz."),
        ("brasil", "brazil"),
        ("czech republic", "czechia"),
        ("espana", "spain"),
        ("hong kong", "china"),
        ("macao", "china"),
        ("macau", "china"),
        ("peoples r china", "china"),
        ("rusia", "russia"),
        ("russian federation", "russia"),
        ("united states of america", "united states"),
        ("usa", "united states"),
    ]:
        x = re.sub(a, b, x)

    ##
    ## Name search in the affiliation (x)
    ##
    for z in reversed(x.split(",")):

        z = z.strip()

        ##
        ## Exact match in list of stadardized country names
        ##
        if z.lower() in country_names:
            return z.lower()

        ##
        ## Discard problems of multiple blank spaces
        ##
        z = " ".join([w.strip() for w in z.lower().split(" ")])
        if z in country_names:
            return z.lower()

    #
    # Repair country name from institution name
    #
    for institution, country in NAMES:
        if institution in x:
            return country

    for country_name in country_names:
        if country_name in x:
            return country_name

    #
    # Country not found
    #
    return None
