# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=import-outside-toplevel
"""
Text Clumping
===============================================================================


>>> from techminer2.thesaurus.descriptors import text_clumping
>>> text_clumping( # doctest: +SKIP
...     text="FINTECH",
...     #
...     # DATABASE PARAMS:
...     root_dir="example/", 
... )
--INFO-- The thesaurus example/thesauri/descriptors.the.txt was rewritten.

"""
import os.path

import pandas as pd  # type: ignore
import pkg_resources  # type: ignore
from nltk.stem import PorterStemmer  # type: ignore

from ..internals.thesaurus__read_as_dict import thesaurus__read_as_dict

THESAURUS_FILE = "thesauri/descriptors.the.txt"


def text_clumping(
    text,
    #
    # DATABASE PARAMS:
    root_dir="./",
):
    """:meta private:"""

    th_file = os.path.join(root_dir, THESAURUS_FILE)
    th_dict = thesaurus__read_as_dict(th_file)

    # -------------------------------------------------------------------------------------------
    def dict_to_dataframe(th_dict):
        reversed_th = {
            value: key for key, values in th_dict.items() for value in values
        }
        data_frame = pd.DataFrame(
            {
                "term": reversed_th.keys(),
                "key": reversed_th.values(),
            }
        )
        data_frame["fingerprint"] = data_frame["term"]
        return data_frame

    #
    data_frame = dict_to_dataframe(th_dict)

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
    def british_to_american_spelling(root_dir, data_frame):
        #
        # Loads the thesaurus
        def load_br2am_dict():
            #
            br2am = {}
            file_path = pkg_resources.resource_filename(
                "techminer2", "thesauri_data/british2american.the.txt"
            )
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
    def remove_separators(data_frame):
        #
        data_frame = data_frame.copy()
        data_frame["fingerprint"] = data_frame["fingerprint"].str.replace(
            "_", " ", regex=False
        )
        return data_frame

    data_frame = remove_separators(data_frame)

    # -------------------------------------------------------------------------------------------
    def apply_porter_stemmer(data_frame):
        #
        # Applies Porter Stemmer to the keywords list.

        data_frame = data_frame.copy()

        stemmer = PorterStemmer()

        #
        # Remove particles
        for particle in [
            "^AND THE ",
            " OF USING ",
            " OF THE ",
            "^AND ",
            " AND THE ",
            " AND ",
            " AT ",
            " IN ",
            " ON ",
            " OF ",
            " FOR ",
            " BASED ",
            " TO ",
            " UNDER ",
            " USING ",
        ]:
            data_frame["fingerprint"] = data_frame["fingerprint"].str.replace(
                particle,
                " ",
                regex=True,
            )

        data_frame["fingerprint"] = data_frame["fingerprint"].str.split(" ")
        data_frame["fingerprint"] = data_frame["fingerprint"].map(
            lambda x: [z.strip() for z in x]
        )
        data_frame["fingerprint"] = data_frame["fingerprint"].map(
            lambda x: [stemmer.stem(z) for z in x]
        )
        data_frame["fingerprint"] = data_frame["fingerprint"].map(sorted)
        data_frame["fingerprint"] = data_frame["fingerprint"].str.join(" ")

        return data_frame

    data_frame = apply_porter_stemmer(data_frame)

    # -------------------------------------------------------------------------------------------
    def compute_key_lengths(data_frame):
        data_frame = data_frame.copy()

        data_frame["len_fingerprint"] = (
            data_frame["fingerprint"].str.split(" ").map(len)
        )
        data_frame = data_frame.sort_values(
            ["len_fingerprint", "fingerprint"], ascending=[False, True]
        )

        return data_frame

    data_frame = compute_key_lengths(data_frame)

    # -------------------------------------------------------------------------------------------
    def extract_words_from_user_text(text):
        #
        stemmer = PorterStemmer()

        #
        # Remove particles
        for particle in [
            "_AND_THE_",
            "_AND_",
            "_AT_",
            "_IN_",
            "_ON_",
        ]:
            text = text.replace(particle, "_")

        words = text.split("_")
        words = [w.strip() for w in words]
        words = [stemmer.stem(w) for w in words]

        return words

    words = extract_words_from_user_text(text)

    # -------------------------------------------------------------------------------------------
    def filter_terms_from_dataframe(words, data_frame):
        #
        data_frame = data_frame.copy()

        data_frame = data_frame.loc[
            data_frame.len_fingerprint.map(lambda x: x >= len(words)), :
        ]

        data_frame["found"] = True
        for word in words:
            data_frame["found"] = data_frame["found"] & data_frame[
                "fingerprint"
            ].str.contains(r"\b" + word + r"\b", case=True)

        data_frame = data_frame.loc[data_frame.found, :]

        return data_frame

    data_frame = filter_terms_from_dataframe(words, data_frame)

    # -------------------------------------------------------------------------------------------
    def save_thesaurus(data_frame, th_dict, th_file):
        #
        data_frame = data_frame.copy()

        data_frame = data_frame[["term", "key"]]
        data_frame = data_frame.groupby("key", as_index=False).agg(list)
        data_frame = data_frame.sort_values("key")

        with open(th_file, "w", encoding="utf-8") as file:
            #
            # write found terms
            for _, row in data_frame.iterrows():
                file.write(row.key + "\n")
                for value in row.term:
                    file.write(f"    {value}\n")

            #
            # write the rest of terms in dictionary
            for key in sorted(th_dict.keys()):
                if key not in data_frame.key.to_list():
                    #
                    file.write(key + "\n")

                    for value in th_dict[key]:
                        file.write(f"    {value}\n")

    save_thesaurus(data_frame, th_dict, th_file)
    print(f"--INFO-- The thesaurus {th_file} was rewritten.")
