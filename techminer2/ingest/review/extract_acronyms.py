"""
ExtractAcronyms
===============================================================================


Smoke test:
    >>> from techminer2.ingest.review import ExtractAcronyms
    >>> acronyms = (
    ...     ExtractAcronyms()
    ...     .where_root_directory("examples/fintech-with-references/")
    ...     .run()
    ... )
    >>> len(acronyms)
    12
    >>> "crm" in acronyms
    True
    >>> acronyms["crm"]
    {'customer relationship management'}


"""

from pathlib import Path

import pandas as pd  # type: ignore
from textblob import TextBlob  # type: ignore

from techminer2 import CorpusField
from techminer2._internals import ParamsMixin
from techminer2._internals.data_access import load_main_data
from techminer2._internals.package_data import load_builtin_mapping

_EXCLUDED_COMMON_WORDS = [
    "classification",
    "computer",
    "consumers",
    "economics",
    "electronic",
    "electronics",
    "irrational",
    "online",
    "personnel",
]

_EXCLUDED_ENUMERATIONS = ["i", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix", "x"]

TRUNCATION_MARKER = "... "
MAX_VALUE_DISPLAY_LENGTH = 100
MIN_ACRONYM_LENGTH = 2
TRUNCATION_SUFFIX_LENGTH = 96


class ExtractAcronyms(
    ParamsMixin,
):
    """:meta private:"""

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.acronyms: dict[str, set[str]] = {}

    # -------------------------------------------------------------------------
    def extract_acronyms_from_keywords_with_parentheses(self):

        dataframe = load_main_data(
            root_directory=self.params.root_directory,
            usecols=[
                CorpusField.AUTH_KEY_TOK.value,
                CorpusField.IDX_KEY_TOK.value,
            ],
        )

        for col in [
            CorpusField.AUTH_KEY_TOK.value,
            CorpusField.IDX_KEY_TOK.value,
        ]:
            keywords = dataframe[col].dropna().str.split("; ")
            keywords = keywords.explode().str.strip()
            keywords = keywords[keywords.str.contains("(", regex=False)]
            keywords = keywords[keywords.str.endswith(")")]
            keywords = keywords[~keywords.str.startswith("(")]

            if not keywords.empty:

                for _, text in keywords.items():

                    text = text[:-1]
                    definition, acronym = text.split(" ( ")
                    if len(acronym.split()) > 1:
                        continue
                    if len(definition.split()) == 1:
                        continue
                    if acronym.isdigit():
                        continue
                    if len(acronym) < MIN_ACRONYM_LENGTH:
                        continue
                    if acronym in _EXCLUDED_ENUMERATIONS:
                        continue
                    if acronym in _EXCLUDED_COMMON_WORDS:
                        continue
                    if acronym[0] != definition[0]:
                        continue

                    acronym = acronym.lower().strip()
                    definition = definition.lower().strip()
                    if acronym in self.acronyms:
                        self.acronyms[acronym].add(definition)
                    else:
                        self.acronyms[acronym] = {definition}

    # -------------------------------------------------------------------------
    def extract_acronyms_in_keywords(self):

        dataframe = load_main_data(root_directory=self.params.root_directory)

        for col in [
            CorpusField.AUTH_KEY_TOK.value,
            CorpusField.IDX_KEY_TOK.value,
        ]:
            keywords = dataframe[col].dropna().str.split("; ")
            keywords = keywords.explode().str.strip()
            keywords = keywords.str.replace(r"\([^)]*\)", "", regex=True).str.strip()

            single_words = keywords[keywords.str.split().map(len) == 1]
            single_words = single_words.str.strip().str.lower().drop_duplicates()

            multi_words = keywords[keywords.str.split().map(len) > 1]
            multi_words = multi_words.str.strip().str.lower().drop_duplicates()

            if not multi_words.empty and not single_words.empty:

                for _, definition in multi_words.items():

                    acronym = "".join([word[0] for word in definition.split()])
                    if len(acronym) < MIN_ACRONYM_LENGTH:
                        continue

                    if acronym in single_words.values:
                        acronym = acronym.strip()
                        definition = definition.strip()
                        if acronym in self.acronyms:
                            self.acronyms[acronym].add(definition)
                        else:
                            self.acronyms[acronym] = {definition}

    # -------------------------------------------------------------------------
    def extract_acronyms_from_abstracts(self):

        abs_col = CorpusField.ABS_TOK.value

        dataframe = load_main_data(
            root_directory=self.params.root_directory,
            usecols=[abs_col],
        ).dropna()

        sentences = (
            dataframe[abs_col]
            .str.replace(r"\)(?!\.)", ") .", regex=True)
            .apply(lambda x: [str(s) for s in TextBlob(x).sentences])  # type: ignore
            .explode()
            .str.strip()
        )

        sentences = sentences[sentences.str.contains("(", regex=False)]
        sentences = sentences[sentences.str.contains(")", regex=False)]
        sentences = sentences.str.replace(r"\)[^)]*$", ")", regex=True)

        acronyms = sentences.str.extract(r"\(([^)]+)\)")[0]

        builtin_acronyms = load_builtin_mapping("acronyms.json")

        for definition, acronym in zip(sentences.values, acronyms.values):

            if pd.isna(acronym):
                continue

            if pd.isna(definition):
                continue

            acronym = acronym.lower().strip()
            definition = definition.lower().strip()
            definition = definition[-90:]

            if definition == "":
                continue

            if acronym in _EXCLUDED_ENUMERATIONS:
                continue
            if acronym in _EXCLUDED_COMMON_WORDS:
                continue
            if acronym.isdigit():
                continue
            if len(acronym.split()) > 1:
                continue
            if len(acronym) < MIN_ACRONYM_LENGTH:
                continue
            if acronym.isdigit():
                continue

            text = definition.split("(")[0].strip()
            full_words = text.split()
            words = [w for w in full_words if w != "and"]
            first_letters = "".join(word[0] for word in words)

            if first_letters.endswith(acronym):

                if "and" in words[-len(acronym) :]:
                    definition = full_words[-len(acronym) + 1 :]
                else:
                    definition = full_words[-len(acronym) :]
                definition = " ".join(definition)

            elif acronym[-1] == "s" and first_letters.endswith(acronym[:-1]):

                if "and" in full_words[-(len(acronym) - 1) :]:
                    definition = full_words[-len(acronym) :]
                else:
                    definition = full_words[-(len(acronym) - 1) :]
                definition = " ".join(definition)
            elif acronym in builtin_acronyms:
                for acronym_definition in builtin_acronyms[acronym]:
                    if acronym_definition in definition:
                        definition = acronym_definition
            else:
                pass

            if acronym in self.acronyms:
                self.acronyms[acronym].add(definition)
            else:
                self.acronyms[acronym] = {definition}

    # -------------------------------------------------------------------------
    def run(self):

        self.extract_acronyms_from_keywords_with_parentheses()
        self.extract_acronyms_in_keywords()
        self.extract_acronyms_from_abstracts()
        return self.acronyms


if __name__ == "__main__":

    acronyms = ExtractAcronyms().where_root_directory("./").run()

    filepath = Path("./") / "refine" / "word_lists" / "acronyms.txt"

    with open(filepath, "w", encoding="utf-8") as file:
        sorted_acronyms = sorted(acronyms.keys())
        for acronym in sorted_acronyms:
            print(acronym, file=file)
            for definition in sorted(acronyms[acronym]):
                print(f"    {definition}", file=file)
