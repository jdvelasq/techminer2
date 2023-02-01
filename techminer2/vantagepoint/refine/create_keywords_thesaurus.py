"""
Create keywords thesaurus
===============================================================================

>>> directory = "data/regtech/"

>>> from techminer2 import vantagepoint
>>> vantagepoint.refine.create_keywords_thesaurus(directory=directory)
--INFO-- Creating `keywords.txt` from author/index keywords, and abstract/title words

"""
import glob
import os
import os.path
import sys

import pandas as pd
from nltk.stem import PorterStemmer

from ..._load_thesaurus_as_dict import load_thesaurus_as_dict
from ..._load_thesaurus_as_dict_r import load_thesaurus_as_dict_r


def create_keywords_thesaurus(directory="./"):
    """Creates a words thesaurus from raw author/index keywords and title/abstact words."""

    sys.stdout.write(
        "--INFO-- Creating `keywords.txt` from author/index keywords, and abstract/title words\n"
    )

    keywords_list = _load_keywords_from_databases(directory=directory)
    keywords_list = _explode_keywords(keywords_list)
    keywords_list = _remove_strange_characters(keywords_list)
    keywords_list = _build_occurrences_table(keywords_list)
    keywords_list = _build_fingerprint(keywords_list)
    keywords_list = _create_keyterm(keywords_list)
    keywords_list = _merge_thesaurus(directory, keywords_list)
    _save_thesaurus(keywords_list, directory)


def _save_thesaurus(keywords_list, directory):
    thesaurus_file = os.path.join(directory, "processed", "keywords.txt")
    keywords_list = keywords_list.copy()
    keywords_list = keywords_list.groupby(["keyterm"]).agg(list)
    keywords_list = keywords_list.sort_index(axis=0)
    with open(thesaurus_file, "w", encoding="utf-8") as file:
        for key in keywords_list.index.tolist():
            file.write(key + "\n")
            for word in keywords_list.word[key]:
                file.write("    " + word + "\n")


def _merge_thesaurus(directory, keywords_list):
    thesaurus_file = os.path.join(directory, "processed", "keywords.txt")
    if not os.path.isfile(thesaurus_file):
        return keywords_list
    old_th_dict = load_thesaurus_as_dict_r(thesaurus_file)
    new_th_dict = {
        key: value for key, value in zip(keywords_list.word, keywords_list.keyterm)
    }
    new_th_dict = {**new_th_dict, **old_th_dict}
    keywords_list = pd.DataFrame(
        {
            "word": list(new_th_dict.keys()),
            "keyterm": list(new_th_dict.values()),
        }
    )
    return keywords_list


def _create_keyterm(keywords_list):
    keywords_list = keywords_list.copy()
    keywords_list = keywords_list.sort_values(
        ["fingerprint", "OCC", "word"], ascending=[True, False, True]
    )
    keywords_list = keywords_list.assign(
        rnk=keywords_list.groupby(["fingerprint"])["OCC"].rank(
            method="first", ascending=False
        )
    )
    keyterms = keywords_list.loc[keywords_list["rnk"] == 1]
    keyterms_dict = {
        key: value for key, value in zip(keyterms.fingerprint, keyterms.word)
    }
    keywords_list = keywords_list.assign(
        keyterm=keywords_list.fingerprint.map(keyterms_dict)
    )
    keywords_list = keywords_list[["word", "keyterm"]]
    return keywords_list


def _build_fingerprint(keywords_list):
    #
    def invert_parenthesis(word):
        if "(" in word:
            text_to_remove = word[word.find("(") + 1 : word.find(")")]
            meaning = word[: word.find("(")].strip()
            if len(meaning) < len(text_to_remove) and len(text_to_remove.strip()) > 1:
                word = text_to_remove + " (" + meaning + ")"
        return word

    def remove_brackets(word):
        if "[" in word:
            text_to_remove = word[word.find("[") : word.find("]") + 1]
            word = word.replace(text_to_remove, "")
            word = " ".join([w.strip() for w in word.split()])
        return word

    def remove_parenthesis(word):
        if "(" in word:
            text_to_remove = word[word.find("(") : word.find(")") + 1]
            word = word.replace(text_to_remove, "")
            word = " ".join([w.strip() for w in word.split()])
        return word

    def remove_initial_terms(keywords_list):
        keywords_list = keywords_list.copy()
        for word in ["^and ", "^the ", "^a ", "^an "]:
            keywords_list.fingerprint = keywords_list.fingerprint.str.replace(
                word, "", regex=True
            )
        return keywords_list

    def replace_sinonimous(keywords_list):
        keywords_list = keywords_list.copy()
        replacements = [
            ("&", "and"),
            (r"\bof\b", ""),
            (r"-based\b", " "),
            (r"\bbased\b", " "),
            (r"\bfor\b", " "),
            (r"\btype-i\b", "type-1 "),
            (r"\btype i\b", "type-1 "),
            (r"\btype 1\b", "type-1 "),
            (r"\btype-ii\b", "type-2 "),
            (r"\btype ii\b", "type-2 "),
            (r"\btype 2\b", "type-2 "),
            (r"\btype2\b", "type-2 "),
            (r"\binterval type\b", "type "),
            (r"\bforecasting\b", "prediction"),
            (r"\bforecast\b", "prediction"),
            (r"\btype2-fuzzy\b", "type-2 fuzzy"),
            (r"\b1-dimensional\b", "one-dimensional "),
            (r"\bneural-net\b", " neural network "),
            (r"\boptimisation\b", "optimization"),
            (r"\bartificial neural network\b", "neural network"),
            (r"\bsolar irradiance\b", "solar radiation"),
            (r"\bsolar irradiation\b", "solar radiation"),
        ]
        for to_replace, value in replacements:
            keywords_list.fingerprint = keywords_list.fingerprint.str.replace(
                to_replace, value, regex=False
            )
        return keywords_list

    def remove_hypen_from_know_keywords(keywords_list):
        keywords_list = keywords_list.copy()
        keywords_with_hypen = [
            "auto-associative",
            "auto-encoder",
            "back-propagation",
            "big-data",
            "feed-forward",
            "lithium-ion",
            "micro-grid",
            "micro-grids",
            "multi-layer",
            "multi-step",
            "non-linear",
            "photo-voltaic",
            "power-point",
            "radial-basis",
            "smart-grid",
            "smart-grids",
            "stand-alone",
        ]
        for word in keywords_with_hypen:
            keywords_list.fingerprint = keywords_list.fingerprint.str.replace(
                r"\b" + word + r"\b", word.replace("-", ""), regex=True
            )
        return keywords_list

    def remove_ending_terms(keywords_list):
        keywords_list = keywords_list.copy()
        replacements = [
            "techniques",
            "technique",
            "algorithms",
            "algorithm",
            "methods",
            "method",
            "approaches",
            "approach",
            "strategies",
            "strategy",
            "models",
            "model",
            "methodologies",
            "methodology",
        ]
        for to_replace in replacements:
            keywords_list.fingerprint = keywords_list.fingerprint.str.replace(
                " " + to_replace + "$", "", regex=True
            )
        return keywords_list

    def _british_to_american_spelling(keywords_list):
        #
        def load_br2am_dict():
            module_path = os.path.dirname(__file__)
            filename = os.path.join(module_path, "../../files/bg2am.txt")
            br2am_dict = load_thesaurus_as_dict(filename)
            br2am_dict = {key: value[0] for key, value in br2am_dict.items()}
            return br2am_dict

        def translate(phrase):
            nonlocal br2am_dict
            british = [br2am_dict.get(word, word) for word in phrase.split()]
            return " ".join(british)

        #
        br2am_dict = load_br2am_dict()
        keywords_list = keywords_list.copy()
        keywords_list.fingerprint = keywords_list.fingerprint.apply(translate)
        return keywords_list

    def _apply_porter_stemmer(keywords_list):
        keywords_list = keywords_list.copy()
        stemmer = PorterStemmer()
        keywords_list.fingerprint = keywords_list.fingerprint.apply(
            lambda x: " ".join([stemmer.stem(word) for word in x.split()])
        )
        return keywords_list

    def _create_fingerprint(keywords_list):
        keywords_list = keywords_list.copy()
        keywords_list.fingerprint = keywords_list.fingerprint.apply(
            lambda x: " ".join(sorted(set(x.split())))
        )
        return keywords_list

    keywords_list = keywords_list.copy()
    keywords_list = keywords_list.assign(fingerprint=keywords_list.word)
    keywords_list.fingerprint = keywords_list.fingerprint.map(invert_parenthesis)
    keywords_list.fingerprint = keywords_list.fingerprint.map(remove_brackets)
    keywords_list.fingerprint = keywords_list.fingerprint.map(remove_parenthesis)
    keywords_list = remove_initial_terms(keywords_list)
    keywords_list = replace_sinonimous(keywords_list)
    keywords_list = remove_hypen_from_know_keywords(keywords_list)
    keywords_list = remove_ending_terms(keywords_list)
    keywords_list = _british_to_american_spelling(keywords_list)
    keywords_list = _apply_porter_stemmer(keywords_list)
    keywords_list = _create_fingerprint(keywords_list)
    return keywords_list


def _build_occurrences_table(keywords_list):
    keywords_list = keywords_list.copy()
    keywords_list = keywords_list.value_counts()
    keywords_list = keywords_list.to_frame()
    keywords_list = keywords_list.reset_index()
    keywords_list.columns = ["word", "OCC"]

    return keywords_list


def _remove_strange_characters(keywords_list):
    keywords_list = keywords_list.copy()
    keywords_list = keywords_list.str.replace('"', "")
    keywords_list = keywords_list.str.replace(chr(8212), "")
    keywords_list = keywords_list.str.replace(chr(8220), "")
    keywords_list = keywords_list.str.replace(chr(8221), "")
    keywords_list = keywords_list.mask(
        (keywords_list.str[0] == "-") & keywords_list.str.len() > 1,
        keywords_list.str.replace("^-", "", regex=True),
    )
    return keywords_list


def _explode_keywords(keywords_list):
    keywords_list = keywords_list.copy()
    keywords_list = keywords_list.dropna()
    keywords_list = keywords_list.str.lower()
    keywords_list = keywords_list.str.split(";")
    keywords_list = keywords_list.explode()
    keywords_list = keywords_list.str.strip()
    return keywords_list


def _load_keywords_from_databases(directory="./"):

    words_list = []
    files = list(glob.glob(os.path.join(directory, "processed/_*.csv")))
    for file in files:
        data = pd.read_csv(file, encoding="utf-8")

        for column in [
            "raw_author_keywords",
            "raw_index_keywords",
            "raw_title_words",
            "raw_abstract_words",
        ]:

            if column in data.columns:
                words_list.append(data[column])
    words_list = pd.concat(words_list, ignore_index=True)
    words_list = words_list.str.strip()
    words_list = words_list[words_list.str.len() > 0]
    return words_list
