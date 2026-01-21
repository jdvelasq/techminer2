# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Copy a Field
===============================================================================


Example:
    >>> import shutil
    >>> shutil.copy("examples/fintech/database.csv.zip", "examples/fintech/data/processed/database.csv.zip")
    'examples/fintech/data/processed/database.csv.zip'

    >>> # Creates, configures, and runs the copy operator
    >>> from techminer2.database.operators import CopyOperator
    >>> (
    ...     CopyOperator()
    ...     #
    ...     # FIELDS:
    ...     .with_field("author_keywords")
    ...     .with_other_field("author_keywords_copy")
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("examples/fintech/")
    ...     #
    ...     .run()
    ... )


    >>> # Query the database to test the operator
    >>> from techminer2.database.tools import Query
    >>> (
    ...     Query()
    ...     .with_query_expression("SELECT author_keywords_copy FROM database LIMIT 5;")
    ...     .where_root_directory("examples/fintech/")
    ...     .where_database("main")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     #
    ...     .run()
    ... )
                                    author_keywords_copy
    0  ELABORATION_LIKELIHOOD_MODEL; FINTECH; K_PAY; ...
    1  ACTOR_NETWORK_THEORY; CHINESE_TELECOM; FINTECH...
    2  FINANCIAL_INCLUSION; FINANCIAL_SCENARIZATION; ...
    3                 BANKING_INNOVATIONS; FINTECH; RISK
    4  BEHAVIOURAL_ECONOMICS; DIGITAL_TECHNOLOGIES; F...

    >>> # Deletes the field
    >>> from techminer2.database.operators import DeleteOperator
    >>> DeleteOperator(
    ...     field="author_keywords_copy",
    ...     root_directory="examples/fintech/",
    ... ).run()


"""
from techminer2._internals.mixins import ParamsMixin
from techminer2.io._internals.extractors.protected_fields import PROTECTED_FIELDS
from techminer2.io._internals.operators.copy_column import internal__copy


class CopyOperator(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        if self.params.other_field in PROTECTED_FIELDS:
            raise ValueError(f"Field `{self.params.other_field}` is protected")

        internal__copy(
            source=self.params.field,
            target=self.params.other_field,
            #
            # DATABASE PARAMS:
            root_directory=self.params.root_directory,
        )


#
