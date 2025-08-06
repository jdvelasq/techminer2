# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Clean text
===============================================================================

This module demonstrates how to clean text in a specified field using the CleanTextOperator
class. The process involves configuring the fields and database parameters.

Example:
    >>> import textwrap
    >>> from techminer2.database.field_operators import CleanTextOperator, DeleteFieldOperator
    >>> from techminer2.tools import Query

    >>> # Creates, configure, and run the clean_operator
    >>> clean_operator = (
    ...     CleanTextOperator()
    ...     #
    ...     # FIELDS:
    ...     .with_field("raw_abstract")
    ...     .with_other_field("cleaned_raw_abstract")
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory_is("examples/fintech/")
    ... )
    >>> clean_operator.run()

    >>> # Query the database to test the clean_operator
    >>> query = (
    ...     Query()
    ...     .with_query_expression("SELECT cleaned_raw_abstract FROM database LIMIT 10;")
    ...     .where_root_directory_is("examples/fintech/")
    ...     .where_database_is("main")
    ...     .where_record_years_range_is(None, None)
    ...     .where_record_citations_range_is(None, None)
    ... )
    >>> df = query.run()
    >>> print(textwrap.fill(df.values[1][0], width=80))
    the rapid development of information and communications technology is
    transforming the entire industry landscape , heralding a new era of convergence
    services . as one of the developing countries in the financial sector , china is
    experiencing an unprecedented level of convergence between finance and
    technology . this study applies the lens of actor network theory ( ant ) to
    conduct a multi level analysis of the historical development of china financial
    technology ( fintech ) industry . it attempts to elucidate the process of
    building and disrupting a variety of networks comprising heterogeneous actors
    involved in the newly emerging convergence industry . this research represents a
    stepping stone in exploring the interaction between fintech and its yet
    unfolding social and political context . it also discusses policy implications
    for china fintech industry , focusing on the changing role of the state in
    fostering the growth of national industry within and outside of china . 2015
    elsevier ltd .


    >>> # Deletes the field
    >>> field_deleter = (
    ...     DeleteFieldOperator()
    ...     .with_field("cleaned_raw_abstract")
    ...     .where_root_directory_is("examples/fintech/")
    ... )
    >>> field_deleter.run()


"""
from ..._internals.mixins import ParamsMixin
from .._internals.protected_fields import PROTECTED_FIELDS
from ..ingest._internals.operators.clean_text import internal__clean_text


class CleanTextOperator(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        if self.params.other_field in PROTECTED_FIELDS:
            raise ValueError(f"Field `{self.params.other_field}` is protected")

        internal__clean_text(
            source=self.params.field,
            dest=self.params.other_field,
            #
            # DATABASE PARAMS:
            root_dir=self.params.root_directory,
        )
