# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Merge Columns
===============================================================================


Example:
    >>> import shutil
    >>> shutil.copy("examples/fintech/database.csv.zip", "examples/fintech/data/processed/database.csv.zip")
    'examples/fintech/data/processed/database.csv.zip'

    >>> # Creates, configure, and run the merger
    >>> from techminer2.database.operators import MergeOperator
    >>> merger = (
    ...     MergeOperator()
    ...     #
    ...     # FIELDS:
    ...     .with_field(["author_keywords", "index_keywords"])
    ...     .with_other_field("merged_keywords")
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("examples/fintech/")
    ... )
    >>> merger.run()

    >>> # Query the database to test the merger
    >>> from techminer2.io import Query
    >>> query = (
    ...     Query()
    ...     .with_query_expression("SELECT merged_keywords FROM database LIMIT 10;")
    ...     .where_root_directory("examples/fintech/")
    ...     .where_database("main")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ... )
    >>> df = query.run()
    >>> df
                                         merged_keywords
    0  ELABORATION_LIKELIHOOD_MODEL; FINTECH; K_PAY; ...
    1  ACTOR_NETWORK_THEORY; CHINESE_TELECOM; CONVERG...
    2  FINANCIAL_INCLUSION; FINANCIAL_SCENARIZATION; ...
    3                 BANKING_INNOVATIONS; FINTECH; RISK
    4  BEHAVIOURAL_ECONOMICS; DIGITAL_TECHNOLOGIES; E...
    5  DATA_MINING; DATA_PRIVACY; FINANCE; FINANCIAL_...
    6  CONCEPTUAL_FRAMEWORKS; CONTENT_ANALYSIS; DIGIT...
    7  CASE_STUDIES; COMMERCE; DIGITAL_TECHNOLOGIES; ...
    8  DIGITIZATION; FINANCIAL_SERVICES_INDUSTRIES; F...
    9  DIGITAL_FINANCE; E_FINANCE; FINTECH; FUTURE_RE...


    >>> # Deletes the fields
    >>> from techminer2.database.operators import DeleteOperator
    >>> field_deleter = (
    ...     DeleteOperator()
    ...     .with_field("merged_keywords")
    ...     .where_root_directory("examples/fintech/")
    ... )
    >>> field_deleter.run()


"""
from techminer2._internals.mixins import ParamsMixin
from techminer2.io._internals.operations.merge_columns import merge_columns
from techminer2.text.extract._helpers.protected_fields import PROTECTED_FIELDS


class MergeColumns(
    ParamsMixin,
):

    def run(self) -> int:

        for source_field in self.params.source_fields:
            if source_field == self.params.target_field:
                raise ValueError(
                    f"Source and target fields must differ (got `{source_field}`)"
                )

        if self.params.target_field in PROTECTED_FIELDS:
            raise ValueError(
                f"Cannot overwrite protected field `{self.params.target_field}`"
            )

        return merge_columns(
            sources=self.params.source_fields,
            target=self.params.target_field,
            root_directory=self.params.root_directory,
        )
