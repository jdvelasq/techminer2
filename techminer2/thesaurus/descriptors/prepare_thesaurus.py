# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Prepare Thesaurus
===============================================================================


>>> from techminer2.thesaurus.descriptors import prepare_thesaurus
>>> prepare_thesaurus(
...     #
...     # DATABASE PARAMS:
...     root_dir="example/", 
... )
--INFO-- The file example/thesauri/descriptors.the.txt has been prepared.

"""
import os.path

import pandas as pd
from tqdm import tqdm

THESAURUS_FILE = "thesauri/descriptors.the.txt"


def prepare_thesaurus(
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

        data_frame["fingerprint"] = data_frame["fingerprint"].map(remove_parenthesis_from_text)

        return data_frame

    data_frame = remove_parenthesis(data_frame)

    # -------------------------------------------------------------------------------------------
    def process_hypened_words(data_frame):
        #
        # Replace non hyppend words by its hypenned version.

        data_frame = data_frame.copy()

        #
        # Loads a generic list of hypened words
        module_path = os.path.dirname(__file__)
        file_path = os.path.join(module_path, "../../../word_lists/hypened_words.txt")
        with open(file_path, "r", encoding="utf-8") as file:
            hypened_words = file.read().split("\n")
        hypened_words = [word.strip() for word in hypened_words]

        for word in tqdm(hypened_words, desc="Processing hypened words"):
            #
            data_frame["fingerprint"] = data_frame["fingerprint"].str.replace(
                r"^" + word.replace("_", "") + "$",
                word,
                regex=True,
            )
            #
            data_frame["fingerprint"] = data_frame["fingerprint"].str.replace(
                r"^" + word.replace("_", "") + "_",
                word + "_",
                regex=True,
            )
            #
            data_frame["fingerprint"] = data_frame["fingerprint"].str.replace(
                r"_" + word.replace("_", "") + "$",
                "_" + word,
                regex=True,
            )
            #
            data_frame["fingerprint"] = data_frame["fingerprint"].str.replace(
                r"_" + word.replace("_", "") + "_",
                "_" + word + "_",
                regex=True,
            )
            #
            data_frame["fingerprint"] = data_frame["fingerprint"].str.replace(
                r"_" + word.replace("_", "") + r"\b",
                "_" + word,
                regex=True,
            )
            #
            data_frame["fingerprint"] = data_frame["fingerprint"].str.replace(
                r"\b" + word.replace("_", "") + "_",
                word + "_",
                regex=True,
            )
            #
            data_frame["fingerprint"] = data_frame["fingerprint"].str.replace(
                r"\b" + word.replace("_", "") + r"\b",
                word,
                regex=True,
            )
            #

        return data_frame

    data_frame = process_hypened_words(data_frame)

    # -------------------------------------------------------------------------------------------
    def replace_common_sinonimous(data_frame):
        #
        # Replaces sinonimous terms

        module_path = os.path.dirname(__file__)
        file_path = os.path.join(module_path, "../../../word_lists/descriptor_replacements.csv")
        pdf = pd.read_csv(file_path, encoding="utf-8")

        for _, row in tqdm(pdf.iterrows(), total=pdf.shape[0], desc="Processing sinonimous terms"):
            #
            pattern = row.to_replace
            repl = row.value
            #
            data_frame["fingerprint"] = data_frame["fingerprint"].str.replace(
                r"^" + pattern + "$",
                repl,
                regex=True,
            )
            #
            data_frame["fingerprint"] = data_frame["fingerprint"].str.replace(
                r"^" + pattern + "_",
                repl + "_",
                regex=True,
            )
            #
            data_frame["fingerprint"] = data_frame["fingerprint"].str.replace(
                r"_" + pattern + "$",
                "_" + repl,
                regex=True,
            )
            #
            data_frame["fingerprint"] = data_frame["fingerprint"].str.replace(
                r"_" + pattern + "_",
                "_" + repl + "_",
                regex=True,
            )
            #
            data_frame["fingerprint"] = data_frame["fingerprint"].str.replace(
                r"_" + pattern + r"\b",
                "_" + repl,
                regex=True,
            )
            #
            data_frame["fingerprint"] = data_frame["fingerprint"].str.replace(
                r"\b" + pattern + "_",
                repl + "_",
                regex=True,
            )
            #
            data_frame["fingerprint"] = data_frame["fingerprint"].str.replace(
                r"\b" + pattern + r"\b",
                repl,
                regex=True,
            )
            #

        return data_frame

    data_frame = replace_common_sinonimous(data_frame)

    # -------------------------------------------------------------------------------------------
    def remove_common_starting_words(data_frame):
        #

        module_path = os.path.dirname(__file__)
        file_path = os.path.join(module_path, "../../../word_lists/common_starting_words.txt")
        with open(file_path, "r", encoding="utf-8") as file:
            words = file.read().split("\n")
        words = [word.strip() for word in words]

        for word in tqdm(words, desc="Removing common starting words"):
            data_frame["fingerprint"] = data_frame["fingerprint"].str.replace("^" + word + "_", "", regex=True)

        return data_frame

    data_frame = remove_common_starting_words(data_frame)

    # -------------------------------------------------------------------------------------------
    def remove_common_ending_words(data_frame):
        #
        module_path = os.path.dirname(__file__)
        file_path = os.path.join(module_path, "../../../word_lists/common_ending_words.txt")
        with open(file_path, "r", encoding="utf-8") as file:
            words = file.read().split("\n")
        words = [word.strip() for word in words]

        for word in tqdm(words, desc="Removing common ending words"):
            data_frame["fingerprint"] = data_frame["fingerprint"].str.replace("_" + word + "$", "", regex=True)

        return data_frame

    data_frame = remove_common_ending_words(data_frame)

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
