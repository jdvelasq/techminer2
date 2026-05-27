"""
Literature Review
===============================================================================

Smoke tests:

    >>> # Create, configure, and run the Text generator
    >>> from tm2p.report.manuscript.literature_review import LiteratureReview
    >>> (
    ...     LiteratureReview()
    ...     #
    ...     # TEXT:
    ...     .with_core_area("fintech")
    ...     .with_word_length(150)
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
    ... )






"""

import os

from openai import OpenAI
from tqdm import tqdm  # type: ignore

from tm2p._intern import ParamsMixin  # type: ignore
from tm2p._intern.packag_data.templates.load_builtin_template import (
    load_builtin_template,
)
from tm2p.enum import Field  # type: ignore
from tm2p.ingest.rec import FilteredRecords  # type: ignore
from tm2p.ingest.rec import RecordViewer  # type: ignore

DOCTYPE = Field.DOCTYPE
TITLE_RAW = Field.TITLE_RAW
REC_NO = Field.REC_NO


class LiteratureReview(
    ParamsMixin,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def internal_load_records(self):

        frame = FilteredRecords().update(**self.params.__dict__).run()

        frame = frame[
            (frame[DOCTYPE] == "Review")
            | (frame[TITLE_RAW].str.lower().str.contains("review"))
        ]
        frame = frame.reset_index(drop=True)

        return frame

    # -------------------------------------------------------------------------
    def internal_get_documents(self, frame):

        titles = frame[TITLE_RAW].to_list()

        documents = (
            RecordViewer()
            .update(**self.params.__dict__)
            .with_source_field(Field.ABSTR_RAW)
            .where_records_match(
                {
                    TITLE_RAW: titles,  # type: ignore
                }
            )
        ).run()

        return documents

    # -------------------------------------------------------------------------

    def run(self):

        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

        template = load_builtin_template("internals.genai.review.summarize.txt")
        records = self.internal_load_records()
        documents = self.internal_get_documents(records)

        dir_path = os.path.join(
            self.params.root_directory,
            "outputs",
            "section_2_literature_review",
        )
        os.makedirs(dir_path, exist_ok=True)

        with open(
            f"{dir_path}/reviews.txt",
            "w",
            encoding="utf-8",
        ) as file:

            for i, (document, ut) in tqdm(
                enumerate(zip(documents, records[REC_NO.value])),
                total=len(documents),
                desc="  Document",
                ncols=73,
            ):

                prompt = template.format(
                    core_area=self.params.core_area,
                    word_length=self.params.word_length,
                    record=document,
                )

                try:
                    response = client.responses.create(
                        model="gpt-4.1",
                        input=prompt,
                    )
                    answer = response.output_text
                    # answer = eval(answer)

                except Exception as e:
                    print(f"Error processing: {e}")

                file.write(answer)
                file.write("\n\n---\n\n")
