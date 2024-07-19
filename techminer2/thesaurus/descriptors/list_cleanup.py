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

>>> from techminer2.thesaurus.descriptors import list_cleanup
>>> list_cleanup(
...     #
...     # DATABASE PARAMS:
...     root_dir="example/", 
... )
--INFO-- The keys in file example/thesauri/descriptors.the.txt has been grouped.

"""
import os.path

import pandas as pd
import pkg_resources
from nltk.stem import PorterStemmer  # type: ignore

THESAURUS_FILE = "thesauri/descriptors.the.txt"


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
                if len(meaning) < len(text_to_remove) and len(text_to_remove.strip()) > 1:
                    text = text_to_remove + " (" + meaning + ")"
            return text

        data_frame["fingerprint"] = data_frame["fingerprint"].map(invert_parenthesis_in_text)

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

        data_frame["fingerprint"] = data_frame["fingerprint"].map(remove_brackets_from_text)

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

        data_frame["fingerprint"] = data_frame["fingerprint"].map(remove_parenthesis_from_text)

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
            "_S_",
        ]:
            data_frame["fingerprint"] = data_frame["fingerprint"].str.replace(word, "", regex=True)

        return data_frame

    data_frame = remove_initial_articles(data_frame)

    # -------------------------------------------------------------------------------------------
    def british_to_american_spelling(data_frame):
        #
        # Loads the thesaurus
        def load_br2am_dict():
            #
            br2am = {}

            file_path = pkg_resources.resource_filename("techminer2", "thesauri_data/british2american.the.txt")
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
        data_frame["fingerprint"] = data_frame["fingerprint"].str.replace("_", " ", regex=False)
        data_frame["fingerprint"] = data_frame["fingerprint"].str.split(" ")
        data_frame["fingerprint"] = data_frame["fingerprint"].map(lambda x: [z.strip() for z in x])
        data_frame["fingerprint"] = data_frame["fingerprint"].map(lambda x: [br2am.get(z, z) for z in x])
        data_frame["fingerprint"] = data_frame["fingerprint"].str.join("_")

        return data_frame

    data_frame = british_to_american_spelling(data_frame)

    # -------------------------------------------------------------------------------------------
    def apply_porter_stemmer(data_frame):
        #
        # Applies Porter Stemmer to the keywords list.

        data_frame = data_frame.copy()

        stemmer = PorterStemmer()

        #
        # Remove intermediate particles
        for particle in [
            "_AIDED_",
            "_AND_",
            "_AND_THE_",
            "_APPLIED_TO_",
            "_AT_",
            "_BASED_",
            "_FOR_",
            "_IN_",
            "_LIKE_",
            "_OF_",
            "_OF_THE_",
            "_OF_USING_",
            "_ON_",
            "_S_",
            "_TO_",
            "_UNDER_",
            "_USING_",
        ]:
            data_frame["fingerprint"] = data_frame["fingerprint"].str.replace(
                particle,
                "_",
                regex=False,
            )

        data_frame["fingerprint"] = data_frame["fingerprint"].str.split("_")
        data_frame["fingerprint"] = data_frame["fingerprint"].map(lambda x: [z.strip() for z in x])
        data_frame["fingerprint"] = data_frame["fingerprint"].map(lambda x: [stemmer.stem(z) for z in x])
        data_frame["fingerprint"] = data_frame["fingerprint"].map(sorted)
        data_frame["fingerprint"] = data_frame["fingerprint"].str.join("_")

        return data_frame

    data_frame = apply_porter_stemmer(data_frame)

    # -------------------------------------------------------------------------------------------
    def compute_terms_by_key(data_frame):
        #
        data_frame = data_frame.copy()
        data_frame["n_terms"] = data_frame.groupby(["fingerprint", "key"]).transform("count")
        data_frame = data_frame.sort_values(["fingerprint", "n_terms", "key"], ascending=True)
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
    print(f"--INFO-- The keys in file {th_file} has been grouped.")
