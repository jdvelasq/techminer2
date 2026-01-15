# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Second Paragraph
===============================================================================

Example:

    >>> # Create, configure, and run the Text generator
    >>> from techminer2.manuscript.introduction.second_paragraph import SecondParagraph
    >>> (
    ...     SecondParagraph()
    ...     #
    ...     # TEXT:
    ...     .with_core_area("fintech")
    ...     .with_word_length(300)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("examples/fintech/")
    ...     .where_database("main")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     .where_records_ordered_by(None)
    ...     #
    ...     .run()
    ... )






"""
import os
import sys

from openai import OpenAI

from techminer2._internals.mixins import ParamsMixin
from techminer2._internals.package_data.templates.load_template import (
    internal__load_template,
)
from techminer2.database.tools import RecordViewer  # type: ignore


class SecondParagraph(
    ParamsMixin,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def internal__get_reviews(self):

        documents = (
            RecordViewer()
            .update(**self.params.__dict__)
            .where_records_match({"document_type": ["Review"]})
        ).run()

        documents = "\n\n---\n\n".join(documents)

        self.reviews = documents

    # -------------------------------------------------------------------------
    def internal__load_template(self):

        self.template = internal__load_template("internals.genai.second_paragraph.txt")

    # -------------------------------------------------------------------------
    def internal__generate_prompt(self):

        prompt = self.template.format(
            core_area=self.params.core_area,
            word_length=self.params.word_length,
            reviews=self.reviews,
        )

        self.prompt = prompt

    # -------------------------------------------------------------------------
    def internal__run_prompt(self):

        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        try:
            response = client.responses.create(
                model="gpt-4.1",
                input=self.prompt,
            )
            self.paragraph = response.output_text

        except Exception as e:
            print(f"Error processing: {e}")

    # -------------------------------------------------------------------------
    def internal__save_paragraph(self):

        dir_path = os.path.join(
            self.params.root_directory,
            "outputs",
            "section_1_introduction",
        )
        os.makedirs(dir_path, exist_ok=True)

        filename = os.path.join(dir_path, "second_paragraph.txt")

        with open(filename, "w") as file:
            file.write(self.paragraph)

    # -------------------------------------------------------------------------
    def run(self):

        sys.stderr.write("\nINFO  Generating second paragraph\n")
        sys.stderr.flush()

        self.internal__get_reviews()
        self.internal__load_template()
        self.internal__generate_prompt()
        self.internal__run_prompt()
        self.internal__save_paragraph()

        sys.stderr.write("INFO: Done\n")
        sys.stderr.flush()
