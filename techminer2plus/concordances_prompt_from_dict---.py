# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""Concordances Prompt from dict"""

import os.path
import textwrap

import pandas as pd

# from ._chatbot import format_prompt_for_paragraphs
from ._read_records import read_records


def concordances_prompt_from_dict(
    #
    # FUNCTION PARAMS:
    search_for,
    top_n,
    #
    # DATABASE PARAMS:
    root_dir: str = "./",
    database: str = "main",
    year_filter: tuple = (None, None),
    cited_by_filter: tuple = (None, None),
    **filters,
):
    """Checks the occurrence contexts of a given text in the abstract's phrases."""

    records = read_records(
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    return concordance_prompt_from_records


def concordances_from_records(
    search_for,
    top_n,
    report_file,
    prompt_file,
    root_dir,
    records,
):
    def get_phrases(records):
        """Gets the phrases with the searched text."""

        records = records.set_index(
            pd.Index(records.article + " / " + records.title)
        )

        records = records.sort_values(
            ["global_citations", "local_citations", "year"],
            ascending=[False, False, True],
        )

        records["_found_"] = (
            records["abstract"]
            .astype(str)
            .str.contains(r"\b" + search_for + r"\b", regex=True)
        )
        records = records[records["_found_"]].head(top_n)

        abstracts = records["abstract"]
        abstracts = (
            abstracts.str.replace(";", ".")
            .str.split(".")
            .explode()
            .str.strip()
        )
        abstracts = abstracts[abstracts.map(lambda x: search_for in x)]

        return abstracts

    def create_contexts_table(phrases):
        """Extracts the contexts table."""

        regex = r"\b" + search_for + r"\b"
        contexts = phrases.str.extract(
            r"(?P<left_context>[\s \S]*)"
            + regex
            + r"(?P<right_context>[\s \S]*)"
        )

        contexts["left_context"] = contexts["left_context"].fillna("")
        contexts["left_context"] = contexts["left_context"].str.strip()

        contexts["right_context"] = contexts["right_context"].fillna("")
        contexts["right_context"] = contexts["right_context"].str.strip()

        contexts = contexts[
            contexts["left_context"].map(lambda x: x != "")
            | contexts["right_context"].map(lambda x: x != "")
        ]

        return contexts

    def transform_context_to_text(contexts):
        """Transforms the contexts table to a text."""

        contexts = contexts.copy()

        contexts["left_r"] = contexts["left_context"].str[::-1]

        contexts = contexts.sort_values(["left_r", "right_context"])

        contexts["left_context"] = contexts["left_context"].map(
            lambda x: "<<< " + x[-56:] if len(x) > 60 else x
        )
        contexts["right_context"] = contexts["right_context"].map(
            lambda x: x[:56] + " >>>" if len(x) > 60 else x
        )

        texts = []
        for _, row in contexts.iterrows():
            text = f"{row['left_context']:>60} {search_for.upper()} {row['right_context']}"
            texts.append(text)

        return "\n".join(texts)

    def generate_prompt(phrases):
        """Generates the chatgpt prompt."""

        phrases = phrases.copy()
        phrases["text"] = (
            phrases["left_context"]
            + f" {search_for.upper()} "
            + phrases["right_context"]
        )
        phrases["article"] = phrases.index.to_list()
        phrases = phrases[["text", "article"]]
        phrases = phrases.groupby("article").agg({"text": list})
        phrases = phrases.text.str.join(".  ")

        main_text = (
            "Your task is to generate a short summary of a term for a research "
            "paper. Summarize the paragraphs below, delimited by triple backticks, "
            "in one unique paragraph, in at most 30 words, focusing on the any aspect contributing "
            f"to the definition and characteristics of the term '{search_for.upper()}'."
        )

        paragraphs = phrases.to_list()

        return format_prompt_for_paragraphs(main_text, paragraphs)

    def fill(text):
        if isinstance(text, str):
            return textwrap.fill(
                text,
                width=87,
                initial_indent=" " * 0,
                subsequent_indent=" " * 0,
                fix_sentence_endings=True,
            )
        return ""

    def write_report(phrases, report_file):
        """Writes the report."""

        phrases = phrases.copy()
        phrases = phrases.to_frame()
        phrases["doc"] = phrases.index
        phrases = phrases.groupby("doc")["abstract"].apply(list)
        # phrases = phrases.map(lambda x: ".  ".join(x))
        phrases = phrases.str.join(".  ")

        file_path = os.path.join(root_dir, "reports", report_file)
        with open(file_path, "w", encoding="utf-8") as file:
            counter = 0
            for title, phrase in zip(phrases.index, phrases):
                print(f"-- {counter:03d} " + "-" * 83, file=file)
                print("AR: ", end="", file=file)
                print(fill(title), file=file)
                print("", file=file)
                print(fill(phrase), file=file)
                print("\n", file=file)
                counter += 1

    def write_prompt_file():
        file_path = os.path.join(root_dir, "reports", prompt_file)
        with open(file_path, "w", encoding="utf-8") as file:
            print(prompt_, file=file)

    #
    # Main code:
    #
    phrases = get_phrases(records)
    frame_ = create_contexts_table(phrases)
    contexts_ = transform_context_to_text(frame_)
    prompt_ = generate_prompt(frame_)

    write_report(phrases, report_file)
    write_prompt_file()

    return contexts_, frame_, prompt_
