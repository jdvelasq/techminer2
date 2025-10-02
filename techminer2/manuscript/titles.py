# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

"""
Titles
===============================================================================

Example:

    >>> from techminer2.manuscript import Titles
    >>> (
    ...     Titles()
    ...     #
    ...     # TEXT:
    ...     .with_core_area("fintech")
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory_is("examples/fintech/")
    ...     #
    ...     .run()
    ... )



"""

import glob
import os

from openai import OpenAI

from techminer2._internals.load_template import internal_load_template
from techminer2._internals.mixins import ParamsMixin
from techminer2.database.tools import RecordMapping


class Titles(
    ParamsMixin,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def internal__load_abstract(self):

        filepath = os.path.join(
            self.params.root_directory,
            "outputs",
            "section_0_abstract",
            "abstract.txt",
        )

        with open(filepath, "r", encoding="utf-8") as f:
            self.abstract = f.read()

    # -------------------------------------------------------------------------
    def internal__load_examples(self):

        mapping = (
            RecordMapping()
            #
            .where_root_directory_is("./")
            .where_database_is("main")
            .where_record_years_range_is(None, None)
            .where_record_citations_range_is(None, None)
            .where_records_ordered_by(None)
            .where_records_match({"document_type": ["Review"]})
            .run()
        )

        mapping = [x["TI"].lower().replace("_", " ") for x in mapping]
        mapping = "\n".join(mapping)
        self.title_examples = mapping

    # -------------------------------------------------------------------------
    def internal__load_template(self):
        self.template = internal_load_template("internals.genai.titles.txt")

    # -------------------------------------------------------------------------
    def internal__generate_titles(self):

        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

        prompt = self.template.format(
            core_area=self.params.core_area,
            abstract=self.abstract,
            title_examples=self.title_examples,
        )

        try:
            response = client.responses.create(model="gpt-4.1", input=prompt)
            answer = response.output_text

            self.titles = answer

        except Exception as e:
            print(f"Error processing: {e}")

    # -------------------------------------------------------------------------
    def internal__save_titles(self):

        dirpath = os.path.join(
            self.params.root_directory,
            "outputs",
            "section_0_abstract",
        )

        os.makedirs(dirpath, exist_ok=True)

        filepath = os.path.join(
            dirpath,
            "titles.txt",
        )

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(self.titles)

    # -------------------------------------------------------------------------
    def run(self):

        self.internal__load_abstract()
        self.internal__load_examples()
        self.internal__load_template()
        self.internal__generate_titles()
        self.internal__save_titles()
        print("INFO  Done!")
