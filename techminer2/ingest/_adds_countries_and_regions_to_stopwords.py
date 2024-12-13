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

import pandas as pd  # type: ignore
import pkg_resources  # type: ignore

from ..prepare.thesaurus._core.load_thesaurus_as_dict import load_thesaurus_as_dict


def _adds_countries_and_regions_to_stopwords(
    #
    # DATABASE PARAMS:
    root_dir,
):
    def build_list_of_countries_regions_and_subregions():

        files = [
            "thesaurus/_data/country-to-region.the.txt",
            "thesaurus/_data/country-to-subregion.the.txt",
        ]

        candidates = []
        for file in files:
            thesaurus = load_thesaurus_as_dict(
                pkg_resources.resource_filename("techminer2", file)
            )
            for key, values in thesaurus.items():
                candidates.append(key.upper())
                values = [w.upper() for w in values]
                candidates += values

        return list(set(candidates))

    def load_stopwords(stopwords_file_path):
        with open(stopwords_file_path, "r", encoding="utf-8") as file:
            stopwords = [line.strip() for line in file.readlines()]
        return stopwords

    def save_stopwords(stopwords_file_path, stopwords):
        with open(stopwords_file_path, "w", encoding="utf-8") as file:
            print("\n".join(stopwords), file=file)

    def load_descriptors():
        files = list(glob.glob(os.path.join(root_dir, "databases/_*.zip")))
        complete_descriptors = []
        for file in files:
            df = pd.read_csv(file, encoding="utf-8", compression="zip")
            descriptors = df.descriptors.copy()
            descriptors = descriptors.dropna()
            descriptors = descriptors.str.split("; ").explode()
            descriptors = descriptors.str.strip()
            descriptors = descriptors.drop_duplicates()
            complete_descriptors += descriptors.tolist()
        return complete_descriptors

    #
    #
    # Main code
    #
    #
    candidates = build_list_of_countries_regions_and_subregions()
    stopwords_file_path = os.path.join(root_dir, "my_keywords/stopwords.txt")
    stopwords = load_stopwords(stopwords_file_path)
    descriptors = load_descriptors()
    selected_candiates = [
        w for w in candidates if w not in stopwords and w in descriptors
    ]
    stopwords += selected_candiates
    stopwords = sorted(set(stopwords))
    save_stopwords(stopwords_file_path, stopwords)
