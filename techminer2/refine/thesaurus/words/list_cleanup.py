# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
List Cleanup
===============================================================================


>>> from techminer2.refine.thesaurus.words import list_cleanup
>>> list_cleanup(
...     #
...     # DATABASE PARAMS:
...     root_dir="example/", 
... )
--INFO-- The file example/thesauri/words.the.txt has been grouped.

"""
import os.path
import re

import pandas as pd
from nltk.stem import PorterStemmer

from ...._common.thesaurus_lib import load_system_thesaurus_as_dict
from .._sort_thesaurus import _sort_thesaurus
from .replace_string import _replace_string
from .reset_thesaurus import reset_thesaurus

THESAURUS_FILE = "thesauri/words.the.txt"


def list_cleanup(
    #
    # DATABASE PARAMS:
    root_dir="./",
):
    """:meta private:"""

    # -------------------------------------------------------------------------------------------
    # Here begins the processing
    th_file = os.path.join(root_dir, THESAURUS_FILE)

    # -------------------------------------------------------------------------------------------
    def load_thesaurus_as_data_frame(th_file):
        #
        records = []
        with open(th_file, "r", encoding="utf-8") as file:
            for line in file.readlines():
                text = line.strip()
                if not line.startswith(" "):
                    key = text
                else:
                    records.append({"key": key, "fingerprint": key, "text": text})

        return pd.DataFrame(records)

    data_frame = load_thesaurus_as_data_frame(th_file)

    # -------------------------------------------------------------------------------------------
    def process_hypened_words(data_frame):
        #
        # Remove hypens from the words.
        #

        data_frame = data_frame.copy()
        #
        # Loads a generic list of hypened words
        module_path = os.path.dirname(__file__)
        file_path = os.path.join(module_path, "../../../word_lists/hypened_words.txt")
        with open(file_path, "r", encoding="utf-8") as file:
            hypened_words = file.read().split("\n")
        hypened_words = [word.strip() for word in hypened_words]

        #
        # Creates a regular expression for hypened words
        regex = [word.replace("-", "_") for word in hypened_words]
        regex = "|".join(regex)
        regex = re.compile(r"\b(" + re.escape(regex) + r")\b")

        #
        # Replace hypened words

        data_frame["fingerprint"] = data_frame["fingerprint"].str.replace(
            regex, lambda z: z.group().replace("_", ""), regex=True
        )

        return data_frame

    data_frame = process_hypened_words(data_frame)

    # -------------------------------------------------------------------------------------------
    def invert_terms_in_parenthesis(data_frame):
        #
        # Transforms `word (meaning)` into `meaning (word)`.
        #
        # "regtech (regulatory technology)" -> "regulatory technology (regtech)"
        #

        data_frame = data_frame.copy()

        def invert_parenthesis_in_text(text):
            if "(" in text:
                text_to_remove = text[text.find("(") + 1 : text.find(")")]
                meaning = text[: text.find("(")].strip()
                if (
                    len(meaning) < len(text_to_remove)
                    and len(text_to_remove.strip()) > 1
                ):
                    text = text_to_remove + " (" + meaning + ")"
            return text

        data_frame["fingerprint"] = data_frame["fingerprint"].map(
            invert_parenthesis_in_text
        )

        return data_frame

    data_frame = invert_terms_in_parenthesis(data_frame)

    # -------------------------------------------------------------------------------------------
    def remove_brackets(data_frame):
        #
        #  brackets from the word.
        #
        #   "regtech [regulatory technology]" -> "regtech"
        #
        data_frame = data_frame.copy()

        def remove_brackets_from_text(text):
            if "[" in text:
                text_to_remove = text[text.find("[") : text.find("]") + 1]
                text = text.replace(text_to_remove, "")
                text = " ".join([w.strip() for w in text.split()])
            return text

        data_frame["fingerprint"] = data_frame["fingerprint"].map(
            remove_brackets_from_text
        )

        return data_frame

    data_frame = remove_brackets(data_frame)

    # -------------------------------------------------------------------------------------------
    def remove_parenthesis(data_frame):
        #
        # Removes parenthesis from the column.
        #
        #    "regtech (regulatory technology)" -> "regtech"
        #

        data_frame = data_frame.copy()

        def remove_parenthesis_from_text(text):
            if "(" in text:
                text_to_remove = text[text.find("(") : text.find(")") + 1]
                text = text.replace(text_to_remove, "")
                text = " ".join([w.strip() for w in text.split()])
            return text

        data_frame["fingerprint"] = data_frame["fingerprint"].map(
            remove_parenthesis_from_text
        )

        return data_frame

    # In some cases, it is necessary to run this function several times
    data_frame = remove_parenthesis(data_frame)
    data_frame = remove_parenthesis(data_frame)
    data_frame = remove_parenthesis(data_frame)

    # -------------------------------------------------------------------------------------------
    def remove_initial_articles(data_frame):
        #
        # Removes initial terms from the keywords list.
        # For example:
        #   "and regtech" -> "regtech"
        #   "the regtech" -> "regtech"
        #   "a regtech" -> "regtech"
        #   "an regtech" -> "regtech"
        #
        data_frame = data_frame.copy()

        for word in [
            "^AND ",
            "^AND_",
            "^THE ",
            "^THE_",
            "^A ",
            "^A_",
            "^AN ",
            "^AN_",
        ]:
            data_frame["fingerprint"] = data_frame["fingerprint"].str.replace(
                word, "", regex=True
            )

        return data_frame

    data_frame = remove_initial_articles(data_frame)

    # -------------------------------------------------------------------------------------------
    def replace_sinonimous(data_frame):
        #
        # Replaces sinonimous terms

        module_path = os.path.dirname(__file__)
        file_path = os.path.join(
            module_path, "../../../word_lists/keywords_replacements.csv"
        )
        replacements = pd.read_csv(file_path, encoding="utf-8")

        data_frame = data_frame.copy()
        for _, row in replacements.iterrows():
            data_frame["fingerprint"] = data_frame["fingerprint"].str.replace(
                r"\b" + row.to_replace + r"\b", row.value, regex=True
            )

        data_frame["fingerprint"] = data_frame["fingerprint"].str.replace(
            "  +", " ", regex=True
        )

        return data_frame

    data_frame = replace_sinonimous(data_frame)

    # -------------------------------------------------------------------------------------------
    def british_to_american_spelling(root_dir, data_frame):
        #
        # Loads the thesaurus
        def load_br2am_dict():
            #
            br2am = {}
            file_path = os.path.join(root_dir, "thesauri/british2american.the.txt")
            with open(file_path, "r", encoding="utf-8") as file:
                for line in file.readlines():
                    if not line.startswith(" "):
                        british = line.strip().upper()
                    else:
                        american = line.strip().upper()
                        br2am[british] = american

            return br2am

        br2am = load_br2am_dict()

        #
        # Replaces british by american spelling
        data_frame = data_frame.copy()

        #
        # Replaces "_" by " "
        data_frame["fingerprint"] = data_frame["fingerprint"].str.replace(
            "_", " ", regex=False
        )
        data_frame["fingerprint"] = data_frame["fingerprint"].str.split(" ")
        data_frame["fingerprint"] = data_frame["fingerprint"].map(
            lambda x: [z.strip() for z in x]
        )
        data_frame["fingerprint"] = data_frame["fingerprint"].map(
            lambda x: [br2am.get(z, z) for z in x]
        )
        data_frame["fingerprint"] = data_frame["fingerprint"].str.join("_")

        return data_frame

    data_frame = british_to_american_spelling(root_dir, data_frame)

    # -------------------------------------------------------------------------------------------
    def apply_porter_stemmer(data_frame):
        #
        # Applies Porter Stemmer to the keywords list.

        data_frame = data_frame.copy()

        stemmer = PorterStemmer()

        #
        # Remove particles
        for particle in [
            "_APPLIED_TO_",
            "_AND_THE_",
            "_OF_USING_",
            "_OF_THE_",
            "_AND_",
            "_AT_",
            "_IN_",
            "_ON_",
            "_OF_",
            "_TO_",
            "_FOR_",
            "_BASED_",
            "_UNDER_",
            "_USING_",
        ]:
            data_frame["fingerprint"] = data_frame["fingerprint"].str.replace(
                particle,
                "_",
                regex=False,
            )

        data_frame["fingerprint"] = data_frame["fingerprint"].str.split("_")
        data_frame["fingerprint"] = data_frame["fingerprint"].map(
            lambda x: [z.strip() for z in x]
        )
        data_frame["fingerprint"] = data_frame["fingerprint"].map(
            lambda x: [stemmer.stem(z) for z in x]
        )
        data_frame["fingerprint"] = data_frame["fingerprint"].map(sorted)
        data_frame["fingerprint"] = data_frame["fingerprint"].str.join("_")

        return data_frame

    data_frame = apply_porter_stemmer(data_frame)

    # -------------------------------------------------------------------------------------------
    def compute_terms_by_key(data_frame):
        #
        data_frame = data_frame.copy()
        data_frame["n_terms"] = data_frame.groupby(["fingerprint", "key"]).transform(
            "count"
        )
        data_frame = data_frame.sort_values(
            ["fingerprint", "n_terms", "key"], ascending=True
        )
        return data_frame

    data_frame = compute_terms_by_key(data_frame)

    # -------------------------------------------------------------------------------------------
    def replace_fingerprint(data_frame):
        #
        # replace the fingerprint for the most frequent key (i.e., the key with the highest number of terms)
        #
        data_frame = data_frame.copy()
        repl = {row.fingerprint: row.key for _, row in data_frame.iterrows()}
        data_frame["fingerprint"] = data_frame["fingerprint"].map(repl)

        return data_frame

    data_frame = replace_fingerprint(data_frame)

    # -------------------------------------------------------------------------------------------
    # Creates a new thesaurus file
    #
    def save_thesaurus(data_frame, th_file):
        #
        data_frame = data_frame.copy()
        data_frame = data_frame[["fingerprint", "text"]]
        data_frame = data_frame.drop_duplicates()
        data_frame = data_frame.sort_values(["fingerprint", "text"], ascending=True)
        data_frame = data_frame.groupby("fingerprint").agg(list)

        with open(th_file, "w", encoding="utf-8") as file:
            for key, row in data_frame.iterrows():
                file.write(key + "\n")
                for value in row.text:
                    file.write("    " + value + "\n")

    save_thesaurus(data_frame, th_file)
