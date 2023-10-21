# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=import-outside-toplevel
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

import glob
import os

import pandas as pd


def _adds_countries_and_regions_to_stopwords(
    #
    # DATABASE PARAMS:
    root_dir,
):
    #
    # Loads stopwords
    stopwords_file_path = os.path.join(root_dir, "my_keywords/stopwords.txt")
    with open(stopwords_file_path, "r", encoding="utf-8") as file:
        stopwords = [line.strip() for line in file.readlines()]

    #
    # Adds countries and regions to stopwords
    countries_and_regions = []
    country2regions_file_path = os.path.join(
        root_dir, "thesauri/country-to-region.the.txt"
    )
    with open(country2regions_file_path, "r", encoding="utf-8") as file:
        for name in file.readlines():
            name = name.strip()
            if name != "":
                countries_and_regions.append(name)

    #
    # Adds countries and sub-regions to stopwords
    country2regions_file_path = os.path.join(
        root_dir, "thesauri/country-to-subregion.the.txt"
    )
    with open(country2regions_file_path, "r", encoding="utf-8") as file:
        for name in file.readlines():
            name = name.strip()
            if name != "":
                countries_and_regions.append(name)

    countries_and_regions = list(set(countries_and_regions))
    countries_and_regions = [w.upper() for w in countries_and_regions]

    files = list(glob.glob(os.path.join(root_dir, "databases/_*.zip")))
    for col in ["raw_index_keywords", "raw_author_keywords"]:
        for file in files:
            data = pd.read_csv(file, encoding="utf-8", compression="zip")
            if col in data.columns:
                if data[col].dropna().shape[0] > 0:
                    keywords = (
                        data[col]
                        .dropna()
                        .str.upper()
                        .str.split("; ")
                        .explode()
                        .str.strip()
                        .drop_duplicates()
                        .tolist()
                    )
                    keywords = [w for w in keywords if w not in countries_and_regions]
                    if len(keywords) > 0:
                        stopwords.extend(keywords)

    stopwords = sorted(set(stopwords))
    with open(country2regions_file_path, "w", encoding="utf-8") as file:
        for word in stopwords:
            file.write(word + "\n")
