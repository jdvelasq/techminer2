# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
First Paragraph
===============================================================================

Example:

    >>> # Create, configure, and run the Text generator
    >>> from techminer2.manuscript.introduction.first_paragraph import FirstParagraph
    >>> (
    ...     FirstParagraph()
    ...     #
    ...     # TEXT:
    ...     .with_abstract_having_pattern(['FINTECH', 'FINANCIAL_TECHNOLOGIES'])
    ...     .with_word_length((200, 400))
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory_is("examples/fintech/")
    ...     .where_database_is("main")
    ...     .where_record_years_range_is(None, None)
    ...     .where_record_citations_range_is(None, None)
    ...     .where_records_match(None)
    ...     .where_records_ordered_by(None)
    ...     #
    ...     .run()
    ... ) # doctest: +SKIP






"""

import os
import sys

import pandas as pd  # type: ignore
from openai import OpenAI
from tqdm import tqdm  # type: ignore

from techminer2._internals.load_template import internal_load_template
from techminer2._internals.mixins import ParamsMixin
from techminer2.database._internals.io import (
    internal__load_filtered_records_from_database,
)


class FirstParagraph(
    ParamsMixin,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def internal__load_the_database(self):
        self.records = internal__load_filtered_records_from_database(params=self.params)

    # -------------------------------------------------------------------------
    def internal__set_record_index(self):
        self.records.index = pd.Index(
            self.records.record_id + " / " + self.records.raw_document_title
        )

    # -------------------------------------------------------------------------
    def internal__select_records_containing_patterns(self):

        patterns = self.params.pattern
        if isinstance(patterns, str):
            patterns = [patterns]

        self.records["_found_"] = False

        for search_for in patterns:

            self.records["_found_"] = self.records["_found_"] | (
                self.records["abstract"]
                .astype(str)
                .str.contains(r"\b" + search_for + r"\b", regex=True)
            )

        self.records = self.records[self.records["_found_"]]

    # -------------------------------------------------------------------------
    def internal__select_phrases_containing_patterns(self):

        self.records["abstract"] = self.records["abstract"].str.replace(";", ".")
        self.records["abstract"] = self.records["abstract"].str.split(".")
        self.records = self.records.explode("abstract")
        self.records["abstract"] = self.records["abstract"].str.strip()

        patterns = self.params.pattern
        if isinstance(patterns, str):
            patterns = [patterns]

        self.records["_found_"] = False

        for search_for in patterns:

            self.records["_found_"] = self.records["_found_"] | (
                self.records["abstract"]
                .astype(str)
                .str.contains(r"\b" + search_for + r"\b", regex=True)
            )

        self.records = self.records[self.records["_found_"]]

    # -------------------------------------------------------------------------
    def internal__select_records_by_phrase_length(self):

        self.records = self.records[self.records["abstract"].str.len() > 60]

    # -------------------------------------------------------------------------
    def internal__add_record_ut_to_phrases(self):

        self.records["abstract"] = (
            self.records["abstract"].astype(str)
            + " [UT "
            + self.records["record_no"].astype(str)
            + "]"
        )

    # -------------------------------------------------------------------------
    def internal__set_context_phrases(self):

        phrases = self.records["abstract"].to_list()
        phrases = phrases[:100]
        phrases = [phrases[i : i + 10] for i in range(0, len(phrases), 10)]
        self.context_phrases = phrases

    # -------------------------------------------------------------------------
    def internal__load_definition_template(self):

        self.definition_template = internal_load_template(
            "internals.genai.first_paragraph_define.txt"
        )

    # -------------------------------------------------------------------------
    def internal__generate_definitions(self):

        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

        list_of_terms = self.params.pattern
        if isinstance(list_of_terms, list):
            list_of_terms = ", ".join(list_of_terms)

        definitions = []

        word_length = self.params.word_length
        if isinstance(word_length, tuple):
            word_length = word_length[0]

        for phrases in tqdm(
            self.context_phrases,
            total=len(self.context_phrases),
            desc="INFO: Generating definitions ",
        ):

            prompt = self.definition_template.format(
                list_of_terms=list_of_terms,
                word_length=word_length,
                context_phrases="\n".join(phrases),
            )

            try:
                response = client.responses.create(
                    model="gpt-4.1",
                    input=prompt,
                )
                definitions.append(response.output_text)

            except Exception as e:
                print(f"Error processing: {e}")

        self.definitions = definitions

    # -------------------------------------------------------------------------
    def internal__load_summarization_template(self):

        self.summarization_template = internal_load_template(
            "internals.genai.first_paragraph_summarize.txt"
        )

    # -------------------------------------------------------------------------
    def internal__summarize_definitions(self):

        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

        word_length = self.params.word_length
        if isinstance(word_length, tuple):
            word_length = word_length[1]

        prompt = self.summarization_template.format(
            word_length=word_length,
            paragraphs_to_combine="\n\n---\n\n".join(self.definitions),
        )

        sys.stderr.write("INFO: Summarizing definitions\n")
        sys.stderr.flush()

        try:
            response = client.responses.create(
                model="gpt-4.1",
                input=prompt,
            )
            answer = response.output_text

        except Exception as e:
            print(f"Error processing: {e}")

        sys.stderr.write("INFO: Done\n")
        sys.stderr.flush()
        self.summary = answer

    # -------------------------------------------------------------------------
    def internal__save_summary(self):

        dir_path = os.path.join(
            self.params.root_directory,
            "outputs",
            "section_1_introduction",
        )
        os.makedirs(dir_path, exist_ok=True)

        filename = os.path.join(dir_path, "first_paragraph.txt")

        with open(filename, "w") as file:

            file.write(self.summary)

    # -------------------------------------------------------------------------
    def run(self):

        self.internal__load_the_database()
        self.internal__set_record_index()
        self.internal__select_records_containing_patterns()
        self.internal__select_phrases_containing_patterns()
        self.internal__select_records_by_phrase_length()
        self.internal__add_record_ut_to_phrases()
        self.internal__set_context_phrases()
        self.internal__load_definition_template()
        self.internal__generate_definitions()
        self.internal__load_summarization_template()
        self.internal__summarize_definitions()
        self.internal__save_summary()
