"""
First Paragraph
===============================================================================

Smoke tests:

    >>> # Create, configure, and run the Text generator
    >>> from tm2p.report.manuscr.first_paragraph import FirstParagraph
    >>> (
    ...     FirstParagraph()
    ...     #
    ...     # TEXT:
    ...     .with_abstract_.having_text_matching(['FINTECH', 'FINANCIAL_TECHNOLOGIES'])
    ...     .with_word_length((200, 400))
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/tinyml-scopus/")
    ...     .where_database("main")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
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
from tm2p._intern import ParamsMixin
from tm2p._intern.data_access import load_filtered_main_csv_zip
from tm2p._intern.packag_data.templates.load_builtin_template import (
    load_builtin_template,
)
from tm2p.enum import Field  # type: ignore
from tqdm import tqdm  # type: ignore

REC_ID = Field.REC_ID
TITLE_RAW = Field.TITLE_RAW
ABSTR_RAW = Field.ABSTR_RAW
REC_NO = Field.REC_NO


class FirstParagraph(
    ParamsMixin,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def internal__load_the_database(self):
        self.records = load_filtered_main_csv_zip(params=self.params)

    # -------------------------------------------------------------------------
    def internal__set_record_index(self):
        self.records.index = pd.Index(
            self.records[REC_ID] + " / " + self.records[TITLE_RAW]
        )

    # -------------------------------------------------------------------------
    def internal__select_records_containing_patterns(self):

        patterns = self.params.pattern
        if isinstance(patterns, str):
            patterns = [patterns]

        self.records["_found_"] = False

        for search_for in patterns:

            self.records["_found_"] = self.records["_found_"] | (
                self.records[ABSTR_RAW]
                .astype(str)
                .str.contains(r"\b" + search_for + r"\b", regex=True)
            )

        self.records = self.records[self.records["_found_"]]

    # -------------------------------------------------------------------------
    def internal__select_phrases_containing_patterns(self):

        self.records[ABSTR_RAW] = self.records[ABSTR_RAW].str.replace(";", ".")
        self.records[ABSTR_RAW] = self.records[ABSTR_RAW].str.split(".")
        self.records = self.records.explode(ABSTR_RAW)  # type: ignore
        self.records[ABSTR_RAW] = self.records[ABSTR_RAW].str.strip()

        patterns = self.params.pattern
        if isinstance(patterns, str):
            patterns = [patterns]

        self.records["_found_"] = False

        for search_for in patterns:

            self.records["_found_"] = self.records["_found_"] | (
                self.records[ABSTR_RAW]
                .astype(str)
                .str.contains(r"\b" + search_for + r"\b", regex=True)
            )

        self.records = self.records[self.records["_found_"]]

    # -------------------------------------------------------------------------
    def internal__select_records_by_phrase_length(self):

        self.records = self.records[self.records[ABSTR_RAW].str.len() > 60]

    # -------------------------------------------------------------------------
    def internal__add_record_ut_to_phrases(self):

        self.records[ABSTR_RAW] = (
            self.records[ABSTR_RAW].astype(str)
            + " [UT "
            + self.records[REC_NO].astype(str)
            + "]"
        )

    # -------------------------------------------------------------------------
    def internal__set_context_phrases(self):

        phrases = self.records[ABSTR_RAW].to_list()
        phrases = phrases[:100]
        phrases = [phrases[i : i + 10] for i in range(0, len(phrases), 10)]
        self.context_phrases = phrases

    # -------------------------------------------------------------------------
    def internal__load_definition_template(self):

        self.definition_template = load_builtin_template(
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

        self.summarization_template = load_builtin_template(
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
