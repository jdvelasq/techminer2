# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=import-outside-toplevel
"""
Create key-concepts thesaurus
===============================================================================

>>> root_dir = "data/regtech/"

>>> import techminer2plus
>>> techminer2plus.ingest.create_descriptors_thesaurus(root_dir=root_dir)
--INFO-- Creating `words.txt` from author/index keywords, and abstract/title nlp phrases

# pylint: disable=line-too-long
"""
import os
import os.path
import pathlib

import pandas as pd
import requests
from nltk.stem import PorterStemmer

from ..thesaurus_lib import load_system_thesaurus_as_frame


def create_descriptors_thesaurus(
    #
    # DATABASE PARAMS:
    root_dir="./",
):
    """Creates a thesaurus from raw keywords and title/abstact words."""

    print(
        "--INFO-- Creating `words.txt` from author/index keywords, and abstract/title nlp phrases"
    )

    series = load_value_phrases_from_databases(root_dir=root_dir)
    series = explode_raw_nlp_phrases(series)
    series = remove_strange_characters(series)
    frame = build_occurrences_table(series)
    #
    frame = process_frame(frame)
    #
    frame = create_key_phrase(frame)

    existent_frame = load_existent_thesaurus(root_dir)
    if existent_frame is not None:
        existent_frame = process_frame(existent_frame)
        key2value = dict(zip(existent_frame.value_fingerprint, existent_frame.key_phrase))
        frame["key_phrase"] = frame["value_fingerprint"].map(lambda x: key2value.get(x, x))
        frame = frame[["key_phrase", "value_phrase"]]
        existent_frame = existent_frame[["key_phrase", "value_phrase"]]
        frame = pd.concat([existent_frame, frame])
        # frame["key_phrase"] = frame["key_phrase"].str.lower()
        frame = frame.drop_duplicates(subset=["value_phrase"])

        #
        # Intelligent merging
        #
    else:
        frame = frame[["key_phrase", "value_phrase"]]

    frame["key_phrase"] = (
        frame["key_phrase"].str.replace(" ", "_").str.replace("_(", " (", regex=False).str.upper()
    )
    frame["value_phrase"] = (
        frame["value_phrase"].str.replace(" ", "_").str.replace("_(", " (", regex=False).str.upper()
    )

    frame = frame.groupby("key_phrase", as_index=False).agg({"value_phrase": list})
    frame["value_phrase"] = frame["value_phrase"].map(set).map(sorted)
    file_path = pathlib.Path(root_dir) / "words.txt"

    with open(file_path, "w", encoding="utf-8") as file:
        for _, row in frame.iterrows():
            file.write(row.key_phrase + "\n")
            for aff in row.value_phrase:
                file.write("    " + aff + "\n")


def process_frame(frame):
    """Group techniques for preprocessing"""

    frame = frame.copy()
    frame = create_fingerprint_column(frame)
    frame["value_fingerprint"] = invert_parenthesis(frame["value_fingerprint"])
    frame["value_fingerprint"] = remove_brackets(frame["value_fingerprint"])
    frame["value_fingerprint"] = remove_parenthesis(frame["value_fingerprint"])
    frame["value_fingerprint"] = remove_initial_articles(frame["value_fingerprint"])
    frame["value_fingerprint"] = replace_sinonimous(frame["value_fingerprint"])
    # frame["value_fingerprint"] = remove_hypen_from_know_keywords(
    #     frame["value_fingerprint"]
    # )
    frame["value_fingerprint"] = remove_ending_terms(frame["value_fingerprint"])
    frame["value_fingerprint"] = british_to_american_spelling(frame["value_fingerprint"])
    frame["value_fingerprint"] = apply_porter_stemmer(frame["value_fingerprint"])

    return frame


def load_existent_thesaurus(root_dir):
    """Load existence thesaurus."""

    file_path = pathlib.Path(root_dir) / "words.txt"

    if not file_path.exists():
        return None

    existent_thesaurus = load_system_thesaurus_as_frame(file_path)
    existent_thesaurus = existent_thesaurus.rename(
        columns={"key": "key_phrase", "value": "value_phrase"}
    )

    existent_thesaurus["key_phrase"] = (
        existent_thesaurus["key_phrase"].str.replace("_", " ").str.upper()
    )
    existent_thesaurus["value_phrase"] = (
        existent_thesaurus["value_phrase"].str.replace("_", " ").str.upper()
    )

    return existent_thesaurus


def load_value_phrases_from_databases(root_dir="./"):
    """Loads keywords from author/index keywords, and abstract/title words."""

    words_list = []

    # files = list(glob.glob(os.path.join(root_dir, "databases/_*.csv")))
    # for file in files:
    #     data = pd.read_csv(file, encoding="utf-8")
    #     if "raw_nlp_phrases" in data.columns:
    #         words_list.append(data["raw_nlp_phrases"])

    file = os.path.join(root_dir, "databases/_main.zip")
    data = pd.read_csv(file, encoding="utf-8", compression="zip")
    if "raw_descriptors" in data.columns:
        words_list.append(data["raw_descriptors"])

    words_list = pd.concat(words_list, ignore_index=True)
    words_list = words_list.str.strip()
    words_list = words_list[words_list.str.len() > 0]
    words_list = words_list.rename("value_phrase")
    words_list = words_list.str.replace("_", " ").str.upper()
    return words_list


def explode_raw_nlp_phrases(frame):
    """Explodes the raw noun phrases column."""

    frame = frame.copy()
    frame = frame.dropna()
    frame = frame.str.upper()
    frame = frame.str.split(";")
    frame = frame.explode()
    frame = frame.str.strip()
    return frame


def remove_strange_characters(series):
    """Removes strange characters from the series."""

    series = series.copy()
    series = series.str.replace('"', "")
    series = series.str.replace(chr(8212), "")
    series = series.str.replace(chr(8220), "")
    series = series.str.replace(chr(8221), "")
    series = series.mask(
        (series.str[0] == "-") & series.str.len() > 1,
        series.str.replace("^-", "", regex=True),
    )
    return series


def build_occurrences_table(series):
    """Builds the occurrences table."""

    series = series.copy()
    series = series.value_counts()
    frame = series.to_frame()
    frame = frame.reset_index()
    frame.columns = ["value_phrase", "OCC"]

    return frame


def create_fingerprint_column(frame):
    """Creates the fingerprint column."""

    frame = frame.copy()
    frame = frame.assign(value_fingerprint=frame.value_phrase)
    return frame


def invert_parenthesis(column):
    """Transforms `word (meaning)` into `meaning (word)`.

    "regtech (regulatory technology)" -> "regulatory technology (regtech)"

    """

    def invert_parenthesis_in_text(text):
        if "(" in text:
            text_to_remove = text[text.find("(") + 1 : text.find(")")]
            meaning = text[: text.find("(")].strip()
            if len(meaning) < len(text_to_remove) and len(text_to_remove.strip()) > 1:
                text = text_to_remove + " (" + meaning + ")"
        return text

    column = column.astype(str).map(invert_parenthesis_in_text)
    return column


def remove_brackets(column):
    """Removes brackets from the word.

    "regtech [regulatory technology]" -> "regtech"

    """

    def remove_brackets_from_text(text):
        if "[" in text:
            text_to_remove = text[text.find("[") : text.find("]") + 1]
            text = text.replace(text_to_remove, "")
            text = " ".join([w.strip() for w in text.split()])
        return text

    column = column.astype(str).map(remove_brackets_from_text)
    return column


def remove_parenthesis(column):
    """Removes parenthesis from the column.

    "regtech (regulatory technology)" -> "regtech"

    """

    def remove_parenthesis_from_text(text):
        if "(" in text:
            text_to_remove = text[text.find("(") : text.find(")") + 1]
            text = text.replace(text_to_remove, "")
            text = " ".join([w.strip() for w in text.split()])
        return text

    column = column.astype(str).map(remove_parenthesis_from_text)
    return column


def remove_initial_articles(series):
    """Removes initial terms from the keywords list.

    "and regtech" -> "regtech"
    "the regtech" -> "regtech"
    "a regtech" -> "regtech"
    "an regtech" -> "regtech"

    """
    series = series.copy()
    for word in ["^AND ", "^THE ", "^A ", "^AN "]:
        series = series.str.replace(word, "", regex=True)
    return series


def replace_sinonimous(series):
    """Replaces sinonimous terms."""

    owner = "jdvelasq"
    repo = "techminer2"
    path = "settings/keywords_replacements.csv"
    url = f"https://raw.githubusercontent.com/{owner}/{repo}/main/{path}"

    replacements = pd.read_csv(url, encoding="utf-8")

    series = series.copy()
    for _, row in replacements.iterrows():
        series = series.str.replace(r"\b" + row.to_replace + r"\b", row.value, regex=True)

    for _ in range(3):
        series = series.str.replace("  ", " ", regex=False)

    return series


# def remove_hypen_from_know_keywords(series):
#     """Removes hypen from known keywords."""

#     series = series.copy()
#     keywords_with_hypen = [
#         "auto-associative",
#         "auto-encoder",
#         "back-propagation",
#         "big-data",
#         "feed-forward",
#         "lithium-ion",
#         "micro-grid",
#         "micro-grids",
#         "multi-layer",
#         "multi-step",
#         "non-linear",
#         "photo-voltaic",
#         "power-point",
#         "radial-basis",
#         "smart-grid",
#         "smart-grids",
#         "stand-alone",
#     ]
#     for word in keywords_with_hypen:
#         series = series.str.replace(
#             r"\b" + word + r"\b", word.replace("-", ""), regex=True
#         )
#     return series


def remove_ending_terms(series):
    """Removes ending terms from the keywords list."""
    series = series.copy()
    replacements = [
        "TECHNIQUES",
        "TECHNIQUE",
        "ALGORITHMS",
        "ALGORITHM",
        "METHODS",
        "METHOD",
        "APPROACHES",
        "APPROACH",
        "STRATEGIES",
        "STRATEGY",
        "MODELS",
        "MODEL",
        "METHODOLOGIES",
        "METHODOLOGY",
    ]
    for to_replace in replacements:
        series = series.str.replace(" " + to_replace + "$", "", regex=True)
    return series


def british_to_american_spelling(series):
    """Translates British to American spelling."""

    def load_br2am_dict():
        """Gets the regex from the settings file."""

        owner = "jdvelasq"
        repo = "techminer2"
        path = "settings/bg2am.txt.txt"
        url = f"https://raw.githubusercontent.com/{owner}/{repo}/main/{path}"

        response = requests.get(url, timeout=5)
        text = response.text.split("\n")

        values = []
        keys = []
        current_key = None
        for line in text:
            if not line.startswith(" "):
                current_key = line.strip()
            else:
                value_phrase = line.strip()
                values.append(value_phrase)
                keys.append(current_key)

        br2am = dict(zip(keys, values))

        return br2am

    # def load_br2am_dict():
    #     module_path = os.path.dirname(__file__)
    #     file_path = os.path.join(module_path, "../../_files/bg2am.txt")
    #     frame = load_system_thesaurus_as_frame(file_path)
    #     br2am = dict(zip(frame.key.to_list(), frame.value.to_list()))
    #     return br2am

    #
    # Main code:
    #
    br2am = load_br2am_dict()
    series = series.copy()
    series = (
        series.astype(str).str.split(" ").map(lambda x: [br2am.get(z, z) for z in x]).str.join(" ")
    )
    return series


def apply_porter_stemmer(series):
    """Applies Porter Stemmer to the keywords list."""

    series = series.copy()
    stemmer = PorterStemmer()
    series = series.apply(lambda x: " ".join(sorted(set(stemmer.stem(word) for word in x.split()))))
    return series


def create_key_phrase(frame):
    """Creates a keyterm column."""

    frame = frame.copy()
    frame = frame.sort_values(
        ["value_fingerprint", "OCC", "value_phrase"],
        ascending=[True, False, True],
    )
    frame = frame.assign(
        rnk=frame.groupby(["value_fingerprint"])["OCC"].rank(method="first", ascending=False)
    )
    #
    key_frame = frame.loc[frame["rnk"] == 1]
    frame = pd.merge(
        frame,
        key_frame[["value_fingerprint", "value_phrase"]],
        on="value_fingerprint",
        how="left",
    )

    frame = frame.rename(
        columns={
            "value_phrase_x": "value_phrase",
            "value_phrase_y": "key_phrase",
        }
    )

    return frame
