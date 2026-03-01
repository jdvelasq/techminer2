"""
CopyColumn
===============================================================================

Smoke Test:
    >>> from tm2p import CorpusField
    >>> from tm2p.ingest.operations import CopyColumn
    >>> (
    ...     CopyColumn()
    ...     .with_source_field(CorpusField.AUTH_KEY_RAW)
    ...     .with_target_field(CorpusField.USER_0)
    ...     .where_root_directory("tests/fintech/")
    ...     .run()
    ... )
    22

    >>> from tm2p.ingest.operations import Query
    >>> (
    ...     Query()
    ...     .with_query_expression("SELECT USER_0 FROM database LIMIT 5;")
    ...     .where_root_directory("tests/fintech/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     #
    ...     .run()
    ... )
                                                  USER_0
    0  Banking; Financial institution; Financial serv...
    1  Bank; Blockchain; Cryptocurrency; Payment; Tec...
    2  Actor network theory; Chinese telecom; Fintech...
    3  Content analysis; Digitalization; FinTech; Inn...
    4  Elaboration likelihood model; Fintech; K pay; ...


"""

from tm2p._intern import ParamsMixin
from tm2p.ingest.data_sourc._intern.oper.copy_column import copy_column
from tm2p.ingest.extr._helpers._protected_fields import PROTECTED_FIELDS


class CopyColumn(
    ParamsMixin,
):
    """:meta private:"""

    def run(self) -> int:

        if self.params.source_field == self.params.target_field:
            raise ValueError(
                f"Source and target fields must differ (got `{self.params.source_field}`)"
            )

        if self.params.target_field in PROTECTED_FIELDS:
            raise ValueError(
                f"Cannot overwrite protected field `{self.params.target_field}`"
            )

        return copy_column(
            source=self.params.source_field,
            target=self.params.target_field,
            root_directory=self.params.root_directory,
        )


#
