# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Tokenize
===============================================================================

This module demonstrates how to tokenize text in a specified field using the TokenizeOperator
class. The process involves configuring the fields and database parameters.

Example:
    >>> from techminer2.database.field_operators import TokenizeOperator
    >>> # Creates, configure, and run the tokenize_
    >>> (
    ...     TokenizeOperator()
    ...     #
    ...     # FIELDS:
    ...     .with_field("raw_abstract")
    ...     .with_other_field("tokenized_raw_abstract")
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory_is("examples/fintech/")
    ...     #
    ...     .run()
    ... )

    >>> # Query the database to test the TokenizeOperator
    >>> from techminer2.tools import Query
    >>> df = (
    ...     Query()
    ...     .with_query_expression("SELECT tokenized_raw_abstract FROM database LIMIT 10;")
    ...     .where_root_directory_is("examples/fintech/")
    ...     .where_database_is("main")
    ...     .where_record_years_range_is(None, None)
    ...     .where_record_citations_range_is(None, None)
    ...     .run()
    ... )

    >>> import textwrap
    >>> print(textwrap.fill(df.values[1][0], width=90))
    the rapid development of information and communications technology is transforming the
    entire industry landscape , heralding a new era of convergence services . as one of the
    developing countries in the financial sector , china is experiencing an unprecedented
    level of convergence between finance and technology . this study applies the lens of actor
    network theory ( ant ) to conduct a multi level analysis of the historical development of
    china ' s financial technology ( fintech ) industry . it attempts to elucidate the process
    of building and disrupting a variety of networks comprising heterogeneous actors involved
    in the newly emerging convergence industry . this research represents a stepping stone in
    exploring the interaction between fintech and its yet unfolding social and political
    context . it also discusses policy implications for china ' s fintech industry , focusing
    on the changing role of the state in fostering the growth of national industry within and
    outside of china . 2015 elsevier ltd .


    >>> # Deletes the field
    >>> from techminer2.database.field_operators import DeleteFieldOperator
    >>> field_deleter = (
    ...     DeleteFieldOperator()
    ...     .with_field("tokenized_raw_abstract")
    ...     .where_root_directory_is("examples/fintech/")
    ... )
    >>> field_deleter.run()


"""
from techminer2._internals.mixins import ParamsMixin

from .._internals.protected_fields import PROTECTED_FIELDS
from ..ingest._internals.operators.tokenize import internal__tokenize


class TokenizeOperator(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        if self.params.other_field in PROTECTED_FIELDS:
            raise ValueError(f"Field `{self.params.other_field}` is protected")

        internal__tokenize(
            source=self.params.field,
            dest=self.params.other_field,
            #
            # DATABASE PARAMS:
            root_dir=self.params.root_directory,
        )
