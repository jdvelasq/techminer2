# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Highlight Nouns and Noun Phrases
===============================================================================


Example:
    >>> import textwrap
    >>> from techminer2.database.field_operators import (
    ...     CleanTextOperator,
    ...     DeleteFieldOperator,
    ...     HighlightNounAndPhrasesOperator,
    ... )
    >>> from techminer2.database.tools import Query

    >>> # Creates, configure, and run the cleaner to prepare the field
    >>> cleaner = (
    ...     CleanTextOperator()
    ...     #
    ...     # FIELDS:
    ...     .with_field("raw_abstract")
    ...     .with_other_field("cleaned_raw_abstract")
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory_is("example/")
    ... )
    >>> cleaner.run()

    >>> # Creates, configure, and run the highlighter
    >>> highlighter = (
    ...     HighlightNounAndPhrasesOperator()
    ...     #
    ...     # FIELDS:
    ...     .with_field("cleaned_raw_abstract")
    ...     .with_other_field("highlighted_raw_abstract")
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory_is("example/")
    ... )
    >>> highlighter.run()

    >>> # Query the database to test the cleaner
    >>> query = (
    ...     Query()
    ...     .with_query_expression("SELECT highlighted_raw_abstract FROM database LIMIT 10;")
    ...     .where_root_directory_is("example/")
    ...     .where_database_is("main")
    ...     .where_record_years_range_is(None, None)
    ...     .where_record_citations_range_is(None, None)
    ... )
    >>> df = query.run()
    >>> print(textwrap.fill(df.values[1][0], width=80))


    >>> # Deletes the fields
    >>> field_deleter = (
    ...     DeleteFieldOperator()
    ...     .where_root_directory_is("example/")
    ... )
    >>> field_deleter.with_field("cleaned_raw_abstract").run()
    >>> field_deleter.with_field("highlighted_raw_abstract").run()



"""
from ..._internals.mixins import ParamsMixin
from .._internals.protected_fields import PROTECTED_FIELDS
from ..ingest._internals.operators.highlight_nouns_and_phrases import (
    internal__highlight_nouns_and_phrases,
)


class HighlightNounAndPhrasesOperator(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        if self.params.other_field in PROTECTED_FIELDS:
            raise ValueError(f"Field `{self.params.other_field}` is protected")

        internal__highlight_nouns_and_phrases(
            source=self.params.field,
            dest=self.params.other_field,
            #
            # DATABASE PARAMS:
            root_directory=self.params.root_directory,
        )
