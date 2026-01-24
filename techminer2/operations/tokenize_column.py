# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Tokenize Column
===============================================================================



Example:
    >>> import shutil
    >>> shutil.copy("examples/fintech/database.csv.zip", "examples/fintech/data/processed/database.csv.zip")
    'examples/fintech/data/processed/database.csv.zip'

    >>> from techminer2.database.operators import TokenizeOperator
    >>> # Creates, configure, and run the tokenize_
    >>> (
    ...     TokenizeOperator()
    ...     #
    ...     # FIELDS:
    ...     .with_field("raw_abstract")
    ...     .with_other_field("tokenized_raw_abstract")
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("examples/fintech/")
    ...     #
    ...     .run()
    ... )

    >>> # Query the database to test the TokenizeOperator
    >>> from techminer2.io import Query
    >>> df = (
    ...     Query()
    ...     .with_query_expression("SELECT tokenized_raw_abstract FROM database LIMIT 10;")
    ...     .where_root_directory("examples/fintech/")
    ...     .where_database("main")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
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
    >>> from techminer2.database.operators import DeleteOperator
    >>> field_deleter = (
    ...     DeleteOperator()
    ...     .with_field("tokenized_raw_abstract")
    ...     .where_root_directory("examples/fintech/")
    ... )
    >>> field_deleter.run()


"""
from techminer2._internals.mixins import ParamsMixin
from techminer2.io._internals.operations.tokenize_column import tokenize_column
from techminer2.text.extract._helpers.protected_fields import PROTECTED_FIELDS


class TokenizeColumn(
    ParamsMixin,
):

    def run(self) -> int:

        if self.params.source_field == self.params.target_field:
            raise ValueError(
                f"Source and target fields must differ (got `{self.params.source_field}`)"
            )

        if self.params.target_field in PROTECTED_FIELDS:
            raise ValueError(
                f"Cannot overwrite protected field `{self.params.target_field}`"
            )

        return tokenize_column(
            source=self.params.source_field,
            target=self.params.target_field,
            root_directory=self.params.root_directory,
        )


#
