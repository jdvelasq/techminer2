# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-few-public-methods
"""
Process a Field
===============================================================================


Example:
    >>> import shutil
    >>> shutil.copy("examples/fintech/database.csv.zip", "examples/fintech/data/processed/database.csv.zip")
    'examples/fintech/data/processed/database.csv.zip'

    >>> # Creates, configures, and runs the operator
    >>> from techminer2.database.operators import TransformOperator
    >>> (
    ...     TransformOperator()
    ...     #
    ...     # FIELDS:
    ...     .with_field("author_keywords")
    ...     .with_other_field("author_keywords_copy")
    ...     #
    ...     # TRANSFORMATION:
    ...     .with_transformation_function(lambda x: x.str.lower())
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("examples/fintech/")
    ...     #
    ...     .run()
    ... )

    >>> # Query the database to test the operation
    >>> from techminer2.io import Query
    >>> (
    ...     Query()
    ...     .with_query_expression("SELECT author_keywords_copy FROM database LIMIT 10;")
    ...     .where_root_directory("examples/fintech/")
    ...     .where_database("main")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .run()
    ... )
                                    author_keywords_copy
    0  elaboration_likelihood_model; fintech; k_pay; ...
    1  actor_network_theory; chinese_telecom; fintech...
    2  financial_inclusion; financial_scenarization; ...
    3                 banking_innovations; fintech; risk
    4  behavioural_economics; digital_technologies; f...
    5            data_mining; fintech; privacy; security
    6  content_analysis; digitalization; fintech; inn...
    7  case_studies; ecosystem_development; financial...
    8  digitization; financial_services_industries; f...
    9  digital_finance; e_finance; fintech; future_re...


    >>> # Deletes the field
    >>> from techminer2.database.operators import DeleteOperator
    >>> DeleteOperator(
    ...     field="author_keywords_copy",
    ...     root_directory="examples/fintech/",
    ... ).run()


"""
from techminer2._internals.mixins import ParamsMixin
from techminer2.io._internals.operators.transform_column import transform_column
from techminer2.text.extract._helpers.protected_fields import PROTECTED_FIELDS


class TransformOperator(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        if self.params.other_field in PROTECTED_FIELDS:
            raise ValueError(f"Field `{self.params.other_field}` is protected")

        transform_column(
            #
            # FIELD:
            source=self.params.field,
            target=self.params.other_field,
            function=self.params.transformation_function,
            #
            # DATABASE:
            root_directory=self.params.root_directory,
        )


#
