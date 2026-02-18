"""
Transform Column
===============================================================================

Smoke test:
    >>> from techminer2 import CorpusField
    >>> from techminer2.ingest.operations import TransformColumn
    >>> (
    ...     TransformColumn()
    ...     .with_source_field(CorpusField.AUTH_KEY_RAW)
    ...     .with_target_field(CorpusField.USER_0)
    ...     .with_transformation_function(lambda x: x.str.lower())
    ...     .where_root_directory("examples/fintech-with-references/")
    ...     .run()
    ... )
    22

    >>> from techminer2.ingest.operations import Query
    >>> (
    ...     Query()
    ...     .with_query_expression("SELECT USER_0 FROM database LIMIT 10;")
    ...     .where_root_directory("examples/fintech-with-references/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .run()
    ... )
                                                  USER_0
    0  banking; financial institution; financial serv...
    1  bank; blockchain; cryptocurrency; payment; tec...
    2  actor network theory; chinese telecom; fintech...
    3  content analysis; digitalization; fintech; inn...
    4  elaboration likelihood model; fintech; k pay; ...
    5                banking innovations; fintech; risks
    6  financial inclusion; financial scenarization; ...
    7  content analysis; digitalization; fintech; inn...
    8  bank 3.0; co-opetition theory; fintech; invest...
    9                                               None



"""

from techminer2._internals import ParamsMixin
from techminer2.ingest.extract._helpers.protected_fields import PROTECTED_FIELDS
from techminer2.ingest.sources._internals.operations.transform_column import (
    transform_column,
)


class TransformColumn(
    ParamsMixin,
):
    """:meta private:"""

    def run(self) -> int:

        if self.params.source_field == self.params.target_field:
            raise ValueError(
                f"Source and target fields must differ (got `{self.params.source_field}`)"
            )

        if self.params.other_field in PROTECTED_FIELDS:
            raise ValueError(f"Field `{self.params.other_field}` is protected")

        if self.params.transformation_function is None:
            raise ValueError("Transformation function must be provided")

        return transform_column(
            #
            # FIELD:
            source=self.params.source_field,
            target=self.params.target_field,
            function=self.params.transformation_function,
            root_directory=self.params.root_directory,
        )


#
