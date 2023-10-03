# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=import-outside-toplevel
"""

>>> from techminer2.ingest.create_words_thesaurus import create_words_thesaurus
>>> create_words_thesaurus(root_dir="data/regtech/")
--INFO-- Creating `words.txt` from author/index keywords, and abstract/title nlp phrases

"""
import os
import os.path
import pathlib
import re
from os.path import dirname

import pandas as pd
from nltk.stem import PorterStemmer

from .._common.thesaurus_lib import load_system_thesaurus_as_frame


def concept_clumping(data_frame):
    """
    :meta private:
    """

    data_frame = data_frame.copy()

    data_frame["len_fingerprint"] = data_frame["fingerprint"].str.split(" ").map(len)
    data_frame = data_frame.sort_values(["len_fingerprint", "fingerprint"], ascending=[False, True])

    #
    # Terms with 4 words
    terms4 = data_frame.loc[data_frame.len_fingerprint == 4, :].copy()
    for _, row in terms4.iterrows():
        #
        # Splits the term in words
        term = row.fingerprint
        word0, word1, word2, word3 = term.split(" ")

        if len(word0) < 3 or len(word1) < 2 or len(word2) < 2 and len(word3) < 2:
            continue

        #
        # Terms with 4 words that conatins the current term of 4 words
        terms5 = data_frame.loc[data_frame.len_fingerprint == 5, :].copy()
        terms5 = terms5.loc[terms5.fingerprint.str.contains(word0, regex=False), :]
        terms5 = terms5.loc[terms5.fingerprint.str.contains(word1, regex=False), :]
        terms5 = terms5.loc[terms5.fingerprint.str.contains(word2, regex=False), :]
        terms5 = terms5.loc[terms5.fingerprint.str.contains(word3, regex=False), :]
        data_frame.loc[terms5.index, "fingerprint"] = term
        data_frame.loc[terms5.index, "len_fingerprint"] = 4

        # if terms5.shape[0] > 0:
        #     print(term)
        #     print(data_frame.loc[terms5.index, :].to_markdown())
        #     print()
        #     print()
    #
    # Terms with 3 words
    terms3 = data_frame.loc[data_frame.len_fingerprint == 3, :].copy()
    for _, row in terms3.iterrows():
        #
        # Splits the term in words
        term = row.fingerprint
        word0, word1, word2 = term.split(" ")

        if len(word0) < 3 or len(word1) < 2 or len(word2) < 2:
            continue

        #
        # Terms with 4 words that conatins the current term of 3 words
        terms4 = data_frame.loc[data_frame.len_fingerprint == 4, :].copy()
        terms4 = terms4.loc[terms4.fingerprint.str.contains(word0, regex=False), :]
        terms4 = terms4.loc[terms4.fingerprint.str.contains(word1, regex=False), :]
        terms4 = terms4.loc[terms4.fingerprint.str.contains(word2, regex=False), :]
        data_frame.loc[terms4.index, "fingerprint"] = term
        data_frame.loc[terms4.index, "len_fingerprint"] = 3

        # if terms4.shape[0] > 0:
        #     print(term)
        #     print(data_frame.loc[terms4.index, :].to_markdown())
        #     print()
        #     print()

    #
    # Terms with 2 words
    terms2 = data_frame.loc[data_frame.len_fingerprint == 2, :].copy()
    for _, row in terms2.iterrows():
        #
        # Splits the term in words
        term = row.fingerprint
        word0, word1 = term.split(" ")

        if len(word0) < 3 or len(word1) < 2:
            continue

        #
        # Terms with 3 words that conatins the current term of 2 words
        terms3 = data_frame.loc[data_frame.len_fingerprint == 3, :].copy()
        terms3 = terms3.loc[terms3.fingerprint.str.contains(word0, regex=False), :]
        terms3 = terms3.loc[terms3.fingerprint.str.contains(word1, regex=False), :]
        data_frame.loc[terms3.index, "fingerprint"] = term
        data_frame.loc[terms3.index, "len_fingerprint"] = 2

        # if terms3.shape[0] > 0:
        #     print(term)
        #     print(data_frame.loc[terms3.index, :].to_markdown())
        #     print()
        #     print()

    return data_frame


def create_words_thesaurus(
    #
    # DATABASE PARAMS:
    root_dir="./",
):
    """
    :meta private:
    """
    print(
        "--INFO-- Creating `words.txt` from author/index keywords, and abstract/title nlp phrases"
    )

    #
    # Creates a dataframe with the raw keywords of the database and the raw
    # nlp phrases (removing generic stopwords).
    #
    data_frame = create_data_frame(root_dir=root_dir)
    data_frame = update_stopwords(data_frame, root_dir=root_dir)
    data_frame = process_fingerprint_key(data_frame)
    thesaurus = create_thesuarus(data_frame)

    file_path = pathlib.Path(root_dir) / "words.txt"
    with open(file_path, "w", encoding="utf-8") as file:
        for key in sorted(thesaurus.keys()):
            file.write(key + "\n")

            for term in sorted(set(thesaurus[key])):
                file.write("    " + term + "\n")


def create_column_data_frame(root_dir, column):
    """
    :meta private:
    """

    #
    # The thesaurus is created only from the main databaase.
    file = os.path.join(root_dir, "databases/_main.csv.zip")
    data_frame = pd.read_csv(file, encoding="utf-8", compression="zip")
    data_frame = data_frame[[column]]
    data_frame.columns = ["raw_term"]
    data_frame = data_frame.dropna()

    #
    # Basic preprocessing
    data_frame["raw_term"] = data_frame["raw_term"].str.replace("_", " ")
    data_frame["raw_term"] = data_frame["raw_term"].str.strip()
    data_frame["raw_term"] = data_frame["raw_term"].str.upper()

    #
    # Only non-empty descriptors
    data_frame = data_frame.loc[data_frame["raw_term"].str.len() > 0, :]

    #
    # Explodes the terms list
    data_frame["raw_term"] = data_frame["raw_term"].str.split(";")
    data_frame = data_frame.explode("raw_term")
    data_frame["raw_term"] = data_frame["raw_term"].str.strip()

    #
    # Replace strange characters
    data_frame["raw_term"] = data_frame["raw_term"].str.replace('"', "")
    data_frame["raw_term"] = data_frame["raw_term"].str.replace(chr(8212), "")
    data_frame["raw_term"] = data_frame["raw_term"].str.replace(chr(8220), "")
    data_frame["raw_term"] = data_frame["raw_term"].str.replace(chr(8221), "")
    data_frame["raw_term"] = data_frame["raw_term"].mask(
        (data_frame["raw_term"].str[0] == "-") & data_frame["raw_term"].str.len() > 1,
        data_frame["raw_term"].str.replace("^-", "", regex=True),
    )

    #
    # Counts term frequency
    data_frame["OCC"] = 1
    data_frame = data_frame.groupby("raw_term", as_index=False).agg({"OCC": "sum"})

    #
    # Creates 'fingerprint' column
    data_frame["fingerprint"] = data_frame["raw_term"]

    return data_frame


def load_stopwords():
    """
    :meta private:
    """
    module_path = dirname(__file__)
    file_path = os.path.join(module_path, "../word_lists/stopwords.txt")
    with open(file_path, "r", encoding="utf-8") as file:
        stopwords = file.read().split("\n")
    stopwords = [w.strip() for w in stopwords]
    stopwords = [w for w in stopwords if w != ""]
    return stopwords


def create_data_frame(root_dir):
    """
    :meta private:
    """

    #
    # Loads raw keywords
    keywords_data_frame = create_column_data_frame(root_dir=root_dir, column="raw_keywords")

    #
    # Loads raw nlp phrases discarding existent keywords
    nlp_data_frame = create_column_data_frame(root_dir=root_dir, column="raw_nlp_phrases")
    nlp_data_frame = nlp_data_frame.loc[
        ~nlp_data_frame["fingerprint"].isin(keywords_data_frame["fingerprint"]), :
    ]

    #
    # Remove stopwords from nlp phrases
    stopwords = load_stopwords()
    regex = re.compile(r"\b(" + "|".join(stopwords) + r")\b")
    nlp_data_frame["fingerprint"] = nlp_data_frame["fingerprint"].str.replace(regex, "", regex=True)
    nlp_data_frame["fingerprint"] = nlp_data_frame["fingerprint"].str.strip()

    #
    # Concats the dataframes
    data_frame = pd.concat([keywords_data_frame, nlp_data_frame], ignore_index=True)
    data_frame = data_frame.reset_index(drop=True)

    return data_frame


def process_fingerprint_key(data_frame):
    """
    :meta private:
    """
    data_frame = data_frame.copy()

    data_frame["fingerprint"] = process_error_terms(data_frame["fingerprint"])
    data_frame["fingerprint"] = process_hypened_words(data_frame["fingerprint"])
    data_frame["fingerprint"] = invert_parenthesis(data_frame["fingerprint"])
    data_frame["fingerprint"] = remove_brackets(data_frame["fingerprint"])
    data_frame["fingerprint"] = remove_parenthesis(data_frame["fingerprint"])
    data_frame["fingerprint"] = remove_parenthesis(data_frame["fingerprint"])
    data_frame["fingerprint"] = remove_parenthesis(data_frame["fingerprint"])
    data_frame["fingerprint"] = remove_initial_articles(data_frame["fingerprint"])
    data_frame["fingerprint"] = replace_sinonimous(data_frame["fingerprint"])
    data_frame["fingerprint"] = remove_starting_terms(data_frame["fingerprint"])
    data_frame["fingerprint"] = remove_ending_terms(data_frame["fingerprint"])
    data_frame["fingerprint"] = remove_starting_terms(data_frame["fingerprint"])
    data_frame["fingerprint"] = remove_ending_terms(data_frame["fingerprint"])
    data_frame["fingerprint"] = british_to_american_spelling(data_frame["fingerprint"])
    #
    data_frame = concept_clumping(data_frame)
    #
    data_frame["fingerprint"] = apply_porter_stemmer(data_frame["fingerprint"])

    return data_frame


def process_error_terms(column):
    """
    :meta private:
    """
    terms = [
        "ABSOLUTE-PERCENTAGE-ERROR",
        "ABSOLUTE-RELATIVE-ERROR",
        "ABSOLUTE-AVERAGE-DEVIATION",
        "AVERAGE-ABSOLUTE-PERCENTAGE-ERROR",
        "AVERAGE-MAXIMUM-RELATIVE-ERROR",
        "AVERAGE-PERCENT-ERROR",
        "AVERAGE-QUADRATIC-ERROR",
        "AVERAGE-RELATIVE-ERROR",
        "MAXIMUM-ABSOLUTE-ERROR",
        "MAXIMUM-ABSOLUTE-PERCENTAGE-ERROR",
        "MAXIMUM-ERROR-PERCENTAGE",
        "MAXIMUM-PERCENTAGE-ERROR",
        "MEAN-ABSOLUTE-ERROR",
        "MEAN-ABSOLUTE-DEVIATION",
        "MEAN-RELATIVE-ERROR",
        "MEAN-SQUARE-ERROR",
        "MEAN-SQUARED-ERROR",
        "RELATIVE-ABSOLUTE-ERROR",
        "RELATIVE-PERCENTAGE-ERROR",
        "ROOT-MEAN-SQUARE-ERROR",
        "ROOT-MEAN-SQUARED-ERROR",
        "RMSE-ERROR-VALUE",
        "RMSE-ERROR",
        "STANDARD-DEVIATION-ERROR",
        "SUM-OF-SQUARE-ERROR",
        "SUM-OF-SQUARED-ERROR",
        "SUM-SQUARE-ERROR",
    ]
    terms = [term.replace("-", " ") for term in terms]

    for term in terms:
        column = column.map(lambda x: "ERROR METRICS" if term in x else x)

    return column


def create_thesuarus(data_frame):
    """
    :meta private:
    """

    data_frame = data_frame.copy()

    #
    # Creates key column
    data_frame = data_frame.sort_values(
        ["fingerprint", "OCC", "raw_term"], ascending=[True, False, True]
    )

    #
    # Process raw terms
    data_frame["raw_term"] = data_frame["raw_term"].str.replace("    ", "   ", regex=False)
    data_frame["raw_term"] = data_frame["raw_term"].str.replace("   ", "  ", regex=False)
    data_frame["raw_term"] = data_frame["raw_term"].str.replace("  ", " ", regex=False)
    data_frame["raw_term"] = data_frame["raw_term"].str.replace(" ", "_", regex=False)
    data_frame["raw_term"] = data_frame["raw_term"].str.replace("_(", " (", regex=False)
    data_frame["raw_term"] = data_frame["raw_term"].str.replace(")_", ") ", regex=False)

    thesaurus = (
        data_frame[["fingerprint", "raw_term"]]
        .groupby("fingerprint", as_index=True)
        .agg({"raw_term": list})
    )
    thesaurus["key"] = thesaurus["raw_term"].map(lambda x: x[0])

    #
    # Remove parenthesis from dictionary keys
    thesaurus["key"] = remove_parenthesis(thesaurus["key"])
    thesaurus["key"] = remove_parenthesis(thesaurus["key"])
    thesaurus["key"] = remove_parenthesis(thesaurus["key"])

    # ---------------------------------------------------------------------------------------------------
    # Replace hypened words

    module_path = dirname(__file__)
    file_path = os.path.join(module_path, "../word_lists/hypened_words.txt")
    with open(file_path, "r", encoding="utf-8") as file:
        hypened_words = file.read().split("\n")

    regex = [word.replace("-", " ") for word in hypened_words]
    regex = "|".join(regex)
    regex = re.compile(r"\b(" + re.escape(regex) + r")\b")

    thesaurus["key"] = thesaurus["key"].str.replace("_", " ")
    thesaurus["key"] = (
        thesaurus["key"]
        .astype(str)
        .str.replace(regex, lambda z: z.group().replace(" ", ""), regex=True)
    )

    thesaurus["key"] = (
        thesaurus["key"]
        .str.replace(" ", "_")
        .str.replace("_(", " (", regex=False)
        .str.replace(")_", ") ", regex=False)
    )

    # ---------------------------------------------------------------------------------------------------

    thesaurus["key"] = thesaurus["key"].str.strip()
    thesaurus["key"] = thesaurus["key"].str.replace("    ", "   ", regex=False)
    thesaurus["key"] = thesaurus["key"].str.replace("   ", "  ", regex=False)
    thesaurus["key"] = thesaurus["key"].str.replace("  ", " ", regex=False)
    thesaurus["key"] = thesaurus["key"].str.replace(" ", "_", regex=False)

    #
    # Replace hypened words
    thesaurus = {row.key: row.raw_term for _, row in thesaurus.iterrows()}

    return thesaurus


def update_stopwords(data_frame, root_dir):
    """
    :meta private:
    """

    data_frame = data_frame.copy()

    #
    # Terms with an empty fingerprint
    phrases = data_frame.loc[data_frame.fingerprint.str.strip() == "", :].copy()
    data_frame.loc[data_frame.fingerprint.str.strip() == "", "fingerprint"] = data_frame.loc[
        data_frame.fingerprint.str.strip() == "", "raw_term"
    ]

    #
    # Process stopwords
    phrases["raw_term"] = phrases["raw_term"].str.replace(" ", "_")
    phrases["raw_term"] = phrases["raw_term"].str.replace("_(", " (", regex=False)
    phrases["raw_term"] = phrases["raw_term"].str.replace(")_", ") ", regex=False)
    phrases["raw_term"] = phrases["raw_term"].str.strip()

    #
    # Lodas the exitent stopwords file
    file_path = pathlib.Path(root_dir) / "stopwords.txt"
    with open(file_path, "r", encoding="utf-8") as in_file:
        stopwords = in_file.read().split("\n")

    stopwords = sorted(set(stopwords + phrases.raw_term.to_list()))
    stopwords = [w.strip() for w in stopwords]
    stopwords = [w for w in stopwords if w != ""]

    with open(file_path, "w", encoding="utf-8") as out_file:
        out_file.write("\n".join(stopwords))

    return data_frame


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


def process_hypened_words(column):
    """
    Converts "CO-EVOLUTION" ---> "COEVOLUTION"
    """

    module_path = dirname(__file__)
    file_path = os.path.join(module_path, "../word_lists/hypened_words.txt")
    with open(file_path, "r", encoding="utf-8") as file:
        hypened_words = file.read().split("\n")

    regex = [word.replace("-", "_") for word in hypened_words]
    regex = "|".join(regex)
    regex = re.compile(r"\b(" + re.escape(regex) + r")\b")

    column = column.astype(str).str.replace(regex, lambda z: z.group().replace("_", ""), regex=True)

    return column


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

    module_path = dirname(__file__)
    file_path = os.path.join(module_path, "../word_lists/keywords_replacements.csv")

    replacements = pd.read_csv(file_path, encoding="utf-8")

    series = series.copy()
    for _, row in replacements.iterrows():
        series = series.str.replace(r"\b" + row.to_replace + r"\b", row.value, regex=True)

    for _ in range(3):
        series = series.str.replace("  ", " ", regex=False)

    return series


def remove_ending_terms(series):
    """Removes ending terms from the keywords list."""
    series = series.copy()
    replacements = [
        "ALGORITHM",
        "ALGORITHMS",
        "APPROACH",
        "APPROACHES",
        "FRAMEWORK",
        "METAHEURISTIC",
        "METHOD",
        "METHODOLOGIES",
        "METHODOLOGY",
        "METHODS",
        "MODEL",
        "MODELS",
        "STRATEGIES",
        "STRATEGY",
        "TECHNIQUE",
        "TECHNIQUES",
    ]
    for to_replace in replacements:
        series = series.str.replace(" " + to_replace + "$", "", regex=True)
    return series


def remove_starting_terms(series):
    """Removes ending terms from the keywords list."""
    series = series.copy()
    replacements = [
        "ADAPTIVE",
        "ADDITIONAL",
        "AUGMENTED",
        "ADVANCED",
        "CLASSICAL",
        "DISCRETE",
        "INDIVIDUAL",
        "CONVENTIONAL",
        "ENHANCED",
        "HYBRID",
        "IMPROVED",
        "NEW",
        "NOVEL",
        "STANDARD",
        "TRADITIONAL",
        "POPULAR",
        "VARIOUS",
        "SIMPLE",
    ]
    for to_replace in replacements:
        series = series.str.replace("^" + to_replace + " ", "", regex=True)
    return series


def british_to_american_spelling(series):
    """Translates British to American spelling."""

    def load_br2am_dict():
        """Gets the regex from the settings file."""

        # owner = "jdvelasq"
        # repo = "techminer2"
        # path = "settings/bg2am.txt"
        # url = f"https://raw.githubusercontent.com/{owner}/{repo}/main/{path}"

        # response = requests.get(url, timeout=5)
        # text = response.text.split("\n")

        module_path = dirname(__file__)
        file_path = os.path.join(module_path, "../word_lists/hypened_words.txt")
        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read().split("\n")

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
