"""
Document types
=========================================================================================

Smoke test:
    >>> import pandas as pd
    >>> from techminer2.discover.overview import DocumentTypes
    >>> types = (
    ...     DocumentTypes()
    ...     #
    ...     .where_root_directory("tests/fintech/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> assert isinstance(types, pd.Series)
    >>> assert len(types) > 0
    >>> types
    DOC_TYPE_NORM
    Article             142
    Review               14
    Book                  8
    Conference paper      7
    Book chapter          3
    Editorial             3
    Note                  1
    Retracted             1
    Short survey          1
    Name: count, dtype: int64

"""

from techminer2._internals import ParamsMixin
from techminer2.enums import CorpusField

__reviewed__ = "2026-01-29"


class DocumentTypes(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        from techminer2.ingest.operations.query import Query  # type: ignore

        return (
            (
                Query()
                #
                .update(**self.params.__dict__)
                .with_query_expression(
                    f"SELECT {CorpusField.PUBTYPE_NORM.value} FROM database;"
                )
                .run()
            )[CorpusField.PUBTYPE_NORM.value]
            .value_counts()
            .sort_index()
            .sort_values(ascending=False)
        )


if __name__ == "__main__":

    import argparse
    from pprint import pprint

    parser = argparse.ArgumentParser(description="Document Types Analysis")
    parser.add_argument(
        "--root-directory",
        type=str,
        default="tests/fintech/",
        help="Root directory path for the corpus",
    )
    args = parser.parse_args()

    pprint(DocumentTypes().where_root_directory(args.root_directory).run())
