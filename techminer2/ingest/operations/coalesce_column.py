"""
Coalesce Column
===============================================================================

Smoke test:
    >>> from techminer2 import CorpusField
    >>> from techminer2.ingest.operations import CopyColumn
    >>> (
    ...     CopyColumn()
    ...     .with_source_field(CorpusField.SRC_TITLE_ABBR_RAW)
    ...     .with_target_field(CorpusField.USER_0)
    ...     .where_root_directory("examples/fintech-with-references/")
    ...     .run()
    ... )
    37

    >>> from techminer2.ingest.operations import TransformColumn
    >>> (
    ...     TransformColumn()
    ...     .with_source_field(CorpusField.USER_0)
    ...     .with_target_field(CorpusField.USER_1)
    ...     .with_transformation_function(lambda x: None)
    ...     .where_root_directory("examples/fintech-with-references/")
    ...     .run()
    ... )

    >>> from techminer2.ingest.operations import CoalesceColumn
    >>> (
    ...     CoalesceColumn()
    ...     .with_source_field(CorpusField.SRC_TITLE_ABBR_RAW)
    ...     .with_target_field(CorpusField.USER_1)
    ...     .where_root_directory("examples/fintech-with-references/")
    ...     .with_transformation_function(lambda x: pd.NA)
    ...     .run()
    ... )

    >>> from techminer2.ingest.operations import Query
    >>> (
    ...     Query()
    ...     .with_query_expression("SELECT USER_1 FROM database LIMIT 5;")
    ...     .where_root_directory("examples/fintech-with-references/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...    .run()
    ... )
                                                  USER_1
    0                                   J. Innov. Manag.
    1  Proc. - Int. Conf. Green Technol. Sustain. Dev...
    2                                  Telecommun Policy
    3                                   Financial Innov.
    4                            Int. J. Appl. Eng. Res.


"""

from techminer2._internals import ParamsMixin
from techminer2.ingest.extract._helpers.protected_fields import PROTECTED_FIELDS
from techminer2.ingest.sources._internals.operations.coalesce_column import (
    coalesce_column,
)


class CoalesceColumn(
    ParamsMixin,
):

    def run(self):

        if self.params.source_field == self.params.target_field:
            raise ValueError(
                f"Source and target fields must differ (got `{self.params.source_field}`)"
            )

        if self.params.target_field in PROTECTED_FIELDS:
            raise ValueError(
                f"Cannot fill a protected field `{self.params.target_field}`"
            )

        coalesce_column(
            source=self.params.source_field,
            target=self.params.target_field,
            root_directory=self.params.root_directory,
        )
