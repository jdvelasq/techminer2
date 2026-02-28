"""
CoalesceColumn
===============================================================================

Smoke test:
    >>> from tm2p import CorpusField
    >>> from tm2p.ingest.operations import CopyColumn
    >>> (
    ...     CopyColumn()
    ...     .with_source_field(CorpusField.SRC_TITLE_ABBR_RAW)
    ...     .with_target_field(CorpusField.USER_0)
    ...     .where_root_directory("tests/fintech/")
    ...     .run()
    ... )
    37

    >>> from tm2p.ingest.operations import TransformColumn
    >>> (
    ...     TransformColumn()
    ...     .with_source_field(CorpusField.USER_0)
    ...     .with_target_field(CorpusField.USER_1)
    ...     .with_transformation_function(lambda x: None)
    ...     .where_root_directory("tests/fintech/")
    ...     .run()
    ... )

    >>> from tm2p.ingest.operations import CoalesceColumn
    >>> (
    ...     CoalesceColumn()
    ...     .with_source_field(CorpusField.SRC_TITLE_ABBR_RAW)
    ...     .with_target_field(CorpusField.USER_1)
    ...     .where_root_directory("tests/fintech/")
    ...     .with_transformation_function(lambda x: pd.NA)
    ...     .run()
    ... )

    >>> from tm2p.ingest.operations import Query
    >>> (
    ...     Query()
    ...     .with_query_expression("SELECT USER_1 FROM database LIMIT 5;")
    ...     .where_root_directory("tests/fintech/")
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

from tm2p._intern import ParamsMixin
from tm2p.ingest.data_sourc._intern.operations.coalesce_column import coalesce_column
from tm2p.ingest.extr._helpers._protected_fields import PROTECTED_FIELDS


class CoalesceColumn(
    ParamsMixin,
):
    """:meta private:"""

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
